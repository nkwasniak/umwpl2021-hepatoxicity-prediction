# hepatoxicity-prediction

Project for subject: Uczenie Maszynowe w Projektowaniu Leków

## Environment Setup

Python will be used to predict hepatoxicity. The environment setup steps are shown below:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) following the instructions for your operating system.
2. Download this repository: `git clone https://github.com/nkwasniak/umwpl2021-hepatoxicity-prediction`.
3. Install environment from the YAML file: `conda env create -f environment.yml`

In the `environment-versions.yml` file, the exact versions of each package are listed. They may not be compatible with all operating systems.

_Important! If you would like to use your GPU to train neural networks, add `cudatoolkit` in a correct version (e.g. `cudatoolkit=10.2`) to the `environment.yml` file._

_If you plan to use our computational cluster, ask us about a configured environment on the server. We have a singularity image with all the packages installed._

Source evironment setup text from : https://github.com/gmum/umwpl2021
