# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
import json
import os
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

# Set the default timeout, in seconds
TIMEOUT = 5
CACHE_FILE = ".geocode_cache.json"
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Load geocoding cache to avoid redundant API calls
def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

# Save geocoding cache
def save_cache(cache):
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f, indent=2)
    except IOError as e:
        print(f"Warning: Failed to save cache: {e}")

# Geocode with retries and caching
def geocode_with_retry(geocoder, location, cache):
    # Check cache first
    if location in cache:
        print(f"Using cached result for: {location}")
        # Return a simple dict that mimics the geocode result
        return cache[location]
    
    # Try geocoding with retries
    for attempt in range(MAX_RETRIES):
        try:
            result = geocoder.geocode(location, timeout=TIMEOUT)
            if result:
                # Cache the result (store as dict for JSON serialization)
                cache[location] = {
                    'latitude': result.latitude,
                    'longitude': result.longitude,
                    'address': result.address
                }
                return result
            else:
                print(f"Warning: No geocoding result for {location}")
                return None
        except GeocoderTimedOut:
            if attempt < MAX_RETRIES - 1:
                print(f"Timeout for {location}, retrying in {RETRY_DELAY}s... (attempt {attempt + 1}/{MAX_RETRIES})")
                sleep(RETRY_DELAY)
            else:
                print(f"Error: Geocode timed out on {location} after {MAX_RETRIES} attempts")
                return None
        except Exception as ex:
            print(f"Error: Geocode failed on {location}: {ex}")
            return None
    return None

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
geocode_cache = load_cache()

# Batch read all files first to minimize I/O
talk_data = []
for file in g:
    try:
        data = frontmatter.load(file)
        data = data.to_dict()
        if 'location' in data:
            talk_data.append(data)
    except Exception as ex:
        print(f"Error reading file {file}: {ex}")

# Perform geolocation
for data in talk_data:
    # Prepare the description
    title = data.get('title', '').strip()
    venue = data.get('venue', '').strip()
    location = data.get('location', '').strip()
    
    if not location:
        continue
        
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location with caching and retry logic
    result = geocode_with_retry(geocoder, location, geocode_cache)
    if result:
        location_dict[description] = result
        print(f"✓ {description}")
    
    # Add a small delay to be respectful to the geocoding service
    sleep(1)

# Save the cache for future runs
save_cache(geocode_cache)

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
