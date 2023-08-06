# Litelab


<a href="https://github.com/1lint/litelab/blob/master/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-yellowgreen" /></a>

Litelab is a tool for running machine learning experiments from lightweight YAML files.

In ML experiments we often have to instantiate multiple layers of nested objects, leading to cumbersome instantiation logic and configuration file formats specific to each project's code. Through some simple recursion in [litelab/lite.py](https://github.com/1lint/litelab/blob/master/litelab/lite.py), Litelab simplifies and standardizes the instantiation process, enabling a lightweight configuration format that directly translates into the defined objects. 

Please see [tutorial.ipynb](https://github.com/1lint/litelab/blob/master/tutorial.ipynb) for an explanation and demonstration of `litelab`. 

## Quick Start

Clone repo and install requirements
```
git clone https://github.com/1lint/litelab
cd litelab
python -m pip install -r requirements.txt
```

As a basic example, run the Pytorch Lightning Basic GAN tutorial from https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/basic-gan.html
```
python lite.py configs/lab.yaml fit
```

As a more complete example, train a stable diffusion pipeline from Huggingface using 
```
python lite.py configs/stable_diffusion/train_unet.yaml fit
```
This will instantiate a stable diffusion pipeline from HuggingFace and train the UNet model using the logic defined in `train_sd/`. I also plan to add more examples/projects using litelab in my other repositories (coming soon!). 

To run lite.py in other directories, install the pip package. Then run configurations with the `lite` console script 
```
python -m pip install .
lite configs/lab.yaml fit
```

Syntax is 
```
lite {config_path} {object_method}
```
Where `config_path` is path to the yaml file to instantiate, and `object_method` is the name of the object method to invoke once the object is instantiated. 








