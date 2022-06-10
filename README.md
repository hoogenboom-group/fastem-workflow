# FAST-EM workflow
Post-processing software for FAST-EM data. Performs importing, montaging, alignment and export to CATMAID of FAST-EM data sets. Based on the iCAT-workflow by Ryan Lane.

### Requirements
- Linux server with [conda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) and [git]() configured.
- User permissions

(Optional) Fetch and install `miniconda`
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

(Optional) Install `git` and clone repository
```
apt-get install git
```

### Installation
1. Create new `conda` environment called `fastem`: 
```
conda env create --file=environment.yml
conda activate fastem
```

2. Install `Jupyter lab` extensions
```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyter-matplotlib
jupyter nbextension enable --py widgetsnbextension
```

3. Clone GitHub repo
```
git clone https://github.com/hoogenboom-group/iCAT-workflow
```

4. Install FAST-EM workflow from github repo
```
pip install git+https://github.com/hoogenboom-group/FAST-EM_workflow.git
```

### Getting started

1. Connect to remote server with port forwarding e.g.
```
ssh -L 8888:localhost:8888 {user}@{server}
```

2. Go to `FAST-EM_workflow` directory and start `jupyter lab` session
```
cd ./FAST-EM_workflow/
jupyter lab --no-browser --port 8888
```

3. Open a browser and navigate to http://localhost:8888/lab to run jupyter lab session

