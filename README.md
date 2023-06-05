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
pip install numpy scipy matplotlib pandas
```
