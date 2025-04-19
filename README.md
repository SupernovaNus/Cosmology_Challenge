# FAIR Universe - Cosmology Challenge

This repository consists of material for the Weak Lensing Cosmology ML Challenge. The competition is expected to launch in **June 2025**.

***

## Overview: Weak Gravitational Lensing and ML Challenge
Weak gravitational lensing reveals the large-scale structure of the universe by observing subtle distortions in galaxy shapes due to intervening matter. Traditional methods mainly capture Gaussian information through two-point statistics. However, non-Gaussian features present in the cosmic web are crucial for studying the underlying physics of structure formation, dark matter distributions, and cosmological parameters, motivating the use of higher-order statistics and advanced machine learning (ML) techniques to extract richer information from the weak lensing data. The primary difficulty is handling systematic uncertainties arising from simulation inaccuracies and observational biases.

Through this challenge, participants will analyze a suite of carefully designed mock weak lensing maps with known cosmological parameters, constructed to include variations in simulation fidelity and observational systematics. By comparing the performance and robustness of different methods in a controlled setting, the challenge aims to systematically assess their ability to extract cosmological information while quantifying their sensitivity to modeling assumptions and systematics.

The outcomes of this challenge are expected to guide the development of next-generation weak lensing analysis pipelines, foster cross-disciplinary collaboration between the astrophysics and machine learning communities, and ultimately improve the reliability of cosmological inference from current and upcoming surveys such as LSST, Euclid, and the Roman Space Telescope. By explicitly addressing simulation-model mismatch and the need to quantify systematic uncertainties, this challenge emphasizes scientific robustness and interpretability, aligning with the growing emphasis on trustworthy ML in scientific domains.


## Data
Participants will work with simulated datasets mimicking observations from the Hyper Suprime-Cam (HSC) survey:
1. Weak lensing shear maps generated from cosmological simulations with 101 different cosmological models (parameters: $\Omega_m$ and $S_8$).
2. Realistic systematic effects included: baryonic effects, intrinsic alignment, photometric redshift uncertainties, shear measurement bias, and more.
3. Dataset organized into four redshift bins per observational field, pixelized with a resolution of 2 arcmin.


<img width="875" alt="image" src="https://github.com/user-attachments/assets/dfc3cab0-6453-4ae3-b4c8-59652ef7056c" />


## Competition Tasks
The competition will be structured into two phases:

### Phase 1: Cosmological Parameter Estimation
Participants develop models that:
1. Accurately infer cosmological parameters ($\Omega_m$, $S_8$) from weak lensing data.
2. Quantify uncertainties via 68% confidence intervals.

### Phase 2: Out-of-Distribution Detection
Participants enhance their models to:
1. Identify test data samples inconsistent with training distribution (OoD detection).
2. Provide probability estimates indicating data conformity to training distributions.
   
The developed methods are expected to directly inform analysis pipelines for upcoming cosmological surveys (e.g., LSST, Euclid, Roman Space Telescope), potentially addressing open questions such as the *$S_8$ tension*.


## Getting Started

A Starting Kit will be provided, including:
Setup and installation instructions.
Code examples for data loading, model training, evaluation, and submission preparation.
Baseline methods employing standard power spectrum analysis and basic CNN emulators.







## Challenge Website
The challenge website is available here: https://www.codabench.org/. Details about how to join the challenge and the challenge description will be available on the website soon.

## Contact
Visit our website: https://fair-universe.lbl.gov/

Email: fair-universe@lbl.gov
