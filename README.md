# course-pharmacokinetic-modelling

## Setup

Create a virtual environment
```
conda create -n mb19
```
conda activate mb19
conda install -c anaconda anaconda-navigator
conda install nb_conda_kernels
conda install -n mb19 ipykernel 
  
mkvirtualenv mb19

Use virtualenv as jupyter kernel
```
(fachkurs) python -m ipykernel install --user --name=mb19

```


## Convert material to PDF
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
jupyter nbconvert --to pdf 01_structural_models.ipynb
jupyter nbconvert --to pdf 02_ordinary_differential_equations.ipynb
jupyter nbconvert --to pdf 03_compartment_model.ipynb

jupyter nbconvert --to pdf 04_simple_absorption.ipynb
jupyter nbconvert --to pdf 05_multiple_dosing.ipynb
jupyter nbconvert --to pdf 06_metabolism.ipynb
jupyter nbconvert --to pdf 07_pharmacokinetic_parameters.ipynb
jupyter nbconvert --to pdf 08_variability.ipynb
jupyter nbconvert --to pdf 09_sbml.ipynb


