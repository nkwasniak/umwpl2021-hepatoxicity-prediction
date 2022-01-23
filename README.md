# Hepatoxicity-prediction

Project for subject: Uczenie Maszynowe w Projektowaniu Leków

## About project

Main goal of project is to help find bits of fingerprints, which have important and unimportant impact to decide if combination is hepatotoxicity. 
In project there was used Klekota-Roth fingerprints in `.csv` files, stored in [`data`](/data). To find best hyperparams for 4 regression models I use grid search with 5-Kfold cross validation [`Searching best hyperparams`](/notebooks/gridsearch_hyperparameters.ipynb).  


Each model got r^2 score: 
![R2 score foreach model](/explonations/r2_score_for_each_model.png "R2 score for each model").
To sum up I used LIME to explanation results for SVR (the best model of all). 



## Environment Setup

Python will be used to predict hepatoxicity. The environment setup steps are shown below:

If you would like to run python scripts from _/src_ directory you must install requirements by: `pip install -r requirements.txt`

If you would like to run jupyter notebook, then at beginning you must do a few steps:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) following the instructions for your operating system.
2. Download this repository: `git clone https://github.com/nkwasniak/umwpl2021-hepatoxicity-prediction`.
3. Install environment from the YAML file: `conda env create -f environment.yml`

In the `environment-versions.yml` file, the exact versions of each package are listed. They may not be compatible with all operating systems.

_Important! If you would like to use your GPU to train neural networks, add `cudatoolkit` in a correct version (e.g. `cudatoolkit=10.2`) to the `environment.yml` file._

_If you plan to use our computational cluster, ask us about a configured environment on the server. We have a singularity image with all the packages installed._

Source evironment setup text from : https://github.com/gmum/umwpl2021
