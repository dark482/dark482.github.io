---
layout: archive
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can also download a PDF version of my CV: [DongxuShen_CV.pdf]({{ base_path }}/files/DongxuShen_CV.pdf).

## Education

- **Hong Kong University of Science and Technology (Guangzhou)**  
  *B.S. in Artificial Intelligence*  
  Sep 2023 – Present

- **University of California, Berkeley**  
  *Exchange Student*  
  Sep 2025 – Dec 2025

---

## Research Interests

3D vision and neural rendering, with a long-term goal of building scalable and photorealistic 3D representations for real-world scene reconstruction. I am particularly interested in:

- **3D Gaussian scene rendering**: 3DGS reconstruction, visual SLAM, and novel view synthesis
- **Digital humans**: 3D Gaussian head avatars and speech-driven facial animation

---

## Research Experience

### Phoneme-Aware Audio-to-Mesh Facial Animation  
*Apr 2026 – Present* · Research Intern under Dr. Xiaoli Liu  
- Developing phoneme-aware models for speech-driven 3D facial animation.  
- Aiming to build semantically meaningful viseme-aware 3DMM mouth bases and phoneme-conditioned audio-to-mesh models beyond PCA-derived expression spaces.

### Unposed 3D Gaussian Head Avatar Reconstruction (AnyAvatar)  
*Jan 2026 – Apr 2026* · Research Intern under Dr. Xiaoli Liu  
- Proposed the first calibration-free framework for reconstructing animatable 3D Gaussian head avatars from unposed multi-view data.  
- Designed a robust FLAME pose initialization strategy for unposed multi-view training.  
- Implemented joint optimization of Gaussians, FLAME parameters, and camera poses, with a tri-plane-based view-consistent color representation (>+5 dB PSNR over baselines).

### Large-Scale 3DGS SLAM (KiloGS-SLAM)  
*Sep 2025 – Feb 2026* · Advised by Prof. Hao Wang, HKUST(GZ)  
- Proposed KiloGS-SLAM for monocular 3DGS-SLAM on kilometer-scale outdoor scenes.  
- Designed texture-complexity-aware Gaussian initialization and multi-view-consistency-guided densification/pruning.

### Whole Slide Image Classification (CDSR)  
*May 2025 – Aug 2025* · Research Intern with Prof. Shidang Xu, SCUT  
- Designed a large-patch feature extractor to address domain gaps in small-patch WSI representations.  
- Led baseline reproduction, experimental evaluation, ablation studies, and paper figure visualization.

---

## Publications & Manuscripts

1. **AnyAvatar: High-Fidelity Gaussian Head Avatars under Uncalibrated Camera Settings**  
   Yujian Liu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Haoran Li<sup>*</sup>, et al.  
   *ACM MM 2026* · [Project](https://aishiweilai.github.io/AnyAvatar.github.io/) · [Code](https://github.com/AISHIWEILAI/AnyAvatar)

2. **Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes**  
   Sicheng Yu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Beizheng Zhao, Guanzhi Ding, Hao Wang<sup>&dagger;</sup>  
   *ECCV 2026* · [Project](https://3dagentworld.github.io/KiloGS-SLAM/) · [arXiv](https://arxiv.org/abs/2606.30436)

3. **Minimal High-Resolution Patches Are Sufficient for Whole Slide Image Representation via Cascaded Dual-Scale Reconstruction**  
   Yujian Liu<sup>*</sup>, Yuechuan Lin<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, et al.  
   *PRCV* · [arXiv](https://arxiv.org/abs/2508.01641)

4. **MoGaFace: Momentum-Guided and Texture-Aware Gaussian Avatars for Consistent Facial Geometry**  
   Yujian Liu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Chuang Chen, et al.  
   *PRCV* · [Project](https://mogaface.github.io/) · [arXiv](https://arxiv.org/abs/2508.01218)

5. **DXTalker: Factorizing Speech-Driven 3D Facial Animation via Articulatory Prototypes and Personalized Dynamics**  
   **Dongxu Shen**<sup>*</sup>, Yujian Liu<sup>*</sup>, Shidang Xu, Xiaoli Liu, et al.  
   *AAAI (Submitted)*

---

## Skills

- **Programming**: Python, C++, JavaScript (TypeScript), Bash/Shell, CUDA  
- **Mathematics**: Calculus, Linear Algebra, Complex Functions, Convex Optimization  
- **Tools**: Windows, Linux; VSCode, Git, LaTeX, Markdown, Blender, MeshLab  
- **Research Areas**: 3D Gaussian Splatting, 3D Reconstruction, Neural Rendering, 3D Head Avatars, Visual SLAM, Speech-driven Facial Animation

---

_Last updated: {{ site.time | date: '%B %Y' }}_
