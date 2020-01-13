# HDF5 Examples

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/European-XFEL-examples/hdf5-examples/master)

Repository containins notebooks going through some introductory
h5py examples, with a focus on photon and neutron data analysis.


## Cloud

### Running on Binder

Nothing special is done during the install or start phases, only
standard binder files are used. Go to the link in the binder badge
above to start the examples.


## Local

### Singularity

Image coming soon, check [panosc-trieste-demo](https://github.com/European-XFEL-examples/panosc-trieste-demo/blob/master/README.md)
to see what the functionality will be like.

## Running Locally

To set up and run this locally, first install conda and activate it, then:

```
git clone https://github.com/European-XFEL-examples/hdf5-examples
cd hdf5-examples
pip install -r requirements.txt
sh ./binder/postBuild
```

Now either install and run jupyter from inside the conda environment,
or alternatively install a kernel by running `ipykernel install --user --name=hdf5-examples`,
then start up Jupyter as you normally would and select this kernel
for the notebooks.
