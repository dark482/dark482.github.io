---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am **Dongxu Shen** (沈东旭), an undergraduate student in **Artificial Intelligence** at [Hong Kong University of Science and Technology (Guangzhou)](https://www.hkust-gz.edu.cn/). I was also an exchange student at the [University of California, Berkeley](https://www.berkeley.edu/) (Fall 2025).

My research interests lie in **3D vision** and **neural rendering**, with a long-term goal of building scalable and photorealistic 3D representations for real-world scene reconstruction. I am particularly interested in:

- High-fidelity **3D Gaussian head avatars** and speech-driven facial animation
- **Large-scale 3D Gaussian Splatting SLAM** for outdoor scenes
- **Whole slide image (WSI)** analysis and efficient high-resolution patch representation

Feel free to reach me at [sdx13431026699@gmail.com](mailto:sdx13431026699@gmail.com).

<span class='anchor' id='-education'></span>

# Education

- *2023.09 – Present*, [HKUST (Guangzhou)](https://www.hkust-gz.edu.cn/) — B.S. in Artificial Intelligence (GPA: 3.3 / 4.3)  
  Relevant coursework: Data Structures and Algorithms (A), Machine Learning (A-), Introduction to AI (A), Mathematics for AI (A)
- *2025.09 – 2025.12*, [UC Berkeley](https://www.berkeley.edu/) — Exchange Student (GPA: 3.9 / 4.0)  
  Relevant coursework: Computer Vision (A), Natural Language Processing (A)

<span class='anchor' id='-experience'></span>

# Experience

- *2026.04 – Present*, **Research Intern**, supervised by Dr. Xiaoli Liu  
  Phoneme-aware audio-to-mesh facial animation; developing semantically meaningful viseme-aware 3DMM mouth bases and phoneme-conditioned models.
- *2026.01 – 2026.04*, **Research Intern**, supervised by Dr. Xiaoli Liu  
  Unposed 3D Gaussian head avatar reconstruction (AnyAvatar).
- *2025.09 – 2026.02*, **Research Assistant**, advised by Prof. Hao Wang, HKUST(GZ)  
  Monocular 3DGS-SLAM for kilometer-scale outdoor scenes (KiloGS-SLAM).
- *2025.05 – 2025.08*, **Research Intern**, with Prof. Shidang Xu, South China University of Technology  
  Whole slide image classification via large-patch feature representation (CDSR).

<span class='anchor' id='-research-projects'></span>

# Research Projects

<div class='paper-box'><div class='paper-box-image'><div><img src='images/projects/anyavatar.png' alt="Fig. 1 AnyAvatar" width="100%"><div class="badge">ACM MM 2026 · Under Review</div></div></div>
<div class='paper-box-text' markdown="1">

**AnyAvatar: High-Fidelity Gaussian Head Avatars under Uncalibrated Camera Settings**

Yujian Liu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Haoran Li<sup>*</sup>, Yuting Liu, Chuang Chen, Xinyi Jiang, Zhupeng Jiang, Peng Cao, Shidang Xu, Xiaoli Liu<sup>&dagger;</sup>

Reconstructs animatable 3D Gaussian head avatars from uncalibrated multi-view images by jointly refining camera poses, FLAME geometry, and Gaussian appearance. Surpasses existing baselines on novel view synthesis by over 5 dB PSNR.

<sup>*</sup> Equal contribution. <sup>&dagger;</sup> Corresponding author.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026 · Under Review</div></div></div>
<div class='paper-box-text' markdown="1">

**Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes**

Sicheng Yu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Beizheng Zhao, Guanzhi Ding, Hao Wang<sup>&dagger;</sup>

KiloGS-SLAM: a monocular 3DGS-SLAM framework for kilometer-scale outdoor scenes, addressing pose tracking failure and memory overhead via texture-complexity-aware Gaussian initialization and multi-view-consistency-guided densification/pruning.

<sup>*</sup> Equal contribution. <sup>&dagger;</sup> Corresponding author.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><img src='images/projects/cdsr.png' alt="Fig. 1 CDSR" width="100%"><div class="badge">PRCV · Under Review</div></div></div>
<div class='paper-box-text' markdown="1">

**Minimal High-Resolution Patches Are Sufficient for Whole Slide Image Representation via Cascaded Dual-Scale Reconstruction**

Yujian Liu<sup>*</sup>, Yuechuan Lin<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Haoran Li, Yutong Wang, Xiaoli Liu, Shidang Xu<sup>&dagger;</sup>

Shows that a small set of informative high-resolution patches, selected and reconstructed through cascaded dual-scale learning, is sufficient for robust WSI representation.

<sup>*</sup> Equal contribution. <sup>&dagger;</sup> Corresponding author.

[arXiv](https://arxiv.org/abs/2508.01641)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><img src='images/projects/mogaface.png' alt="Fig. 1 MoGaFace" width="100%"><div class="badge">PRCV · Under Review</div></div></div>
<div class='paper-box-text' markdown="1">

**MoGaFace: Momentum-Guided and Texture-Aware Gaussian Avatars for Consistent Facial Geometry**

Yujian Liu<sup>*</sup>, **Dongxu Shen**<sup>*</sup>, Chuang Chen, Zairan Wang, Linlang Cao, Fanyu Geng, Peng Cao, Shidang Xu, Xiaoli Liu

Improves 3D Gaussian head avatars by jointly correcting facial geometry and recovering texture during rendering, instead of relying on a frozen tracked mesh.

<sup>*</sup> Equal contribution.

[arXiv](https://arxiv.org/abs/2508.01218)

</div>
</div>
