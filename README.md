# MicronsBinder
A collection of notebooks to provide examples of using data from [microns-explorer.org](https://microns-explorer.org).  The repository is designed to work with [mybinder.org](https://mybinder.org)


# Contents
### Phase 3 cubic mm Introductory Notebooks
In July 2021, we released the data from [Phase 3 of the project](https://) that includes functional and anatomical data from large scale EM reconstructions covering approximately a mm^3 .  We have created some [introductory notebooks](notebooks/mm3_intro) to help users begin to analyze the anatomical data. There is a companion set of repositories for how to access the functional data located here ()

* [CAVESetup](notebooks/mm3_intro/CAVEsetup.ipynb)
This notebook walks users through how to setup their environment to connect to the Connectome Annotation Versioning Engine services that are needed to access the data.  When using mybinder you will need to follow this notebook each time you launch the docker image.  When setting up your own machine it will only need to be followed once.  All other notebooks assume you have setup an account and credentials before continuing. 

* [SynapseAndAnnotationQuery](notebooks/mm3_intro/SynapseAndAnnotationQuery.ipynb)
This notebook shows how to query the inputs and outputs of a neuron, and then goes on to show you how to query any of the data annotation tables, including automated detection of where the neurons are, what neurons have been proofread, and so on. 

* [MeshAccess](notebooks/mm3_intro/MeshAccess.ipynb)
Demonstrates how to download meshes of neurons from the flat and dynamic segmentation using cloud-volume and MeshParty, explaining their differences.  Note the visualization components of this require 


### Phase 1 Introductory Notebooks
An earlier releases of the [Phase 1 data  from layer 2/3](https://microns-explorer.org/phase1) used alternative data formats, and so we have alternative notebooks for accessing this data. 

We've created some [introductory notebooks](notebooks/intro) to demonstrate some potential uses of the data. See:

* [MostSynapsesInAndOut](notebooks/intro/MostSynapsesInAndOut.ipynb)  
This notebook introduces you to reading synapses and the soma valence table.  It creates neuroglancer links that let you explore the inputs and outputs of individual neurons.
* [DashSynapseExplorer](notebooks/intro/DashSynapseExplorer.ipynb)  
This notebook shows you how to create dynamic scatterplots that recreate some of the results about layer 2/3 to layer 2/3 connections that were reported in Dorkenwald et al. 2019.
* [ImageAndSegmentationDownload](notebooks/ImageAndSegmentationDownload.ipynb)  
This notebook shows you how to create figures with overlaid EM and segmentation figures.

The introductory notebooks below are not intended to be run on mybinder for reasons specified below. To run them you should set up a local python environment (see [these instructions](#localenv)).

* [MeshExample](notebooks/intro/MeshExample.ipynb)
This demonstrates basic 3D visualization of meshes and skeletons using vtk, as well as calculating shortest paths along a mesh. This example uses more memory than allocated to most binder instances, and may be killed during processing while using those resources.
* [Render3DScaleBar](notebooks/intro/Render3DScaleBar.ipynb)
This demonstrates two techinques to create 3D scale bars on 3D visualization plots. It requires access to an X windows system to view these plots.

### Vignette manuscript analyses
These notebooks walk through some newer analyses studying the [Phase 1 data  from layer 2/3](https://microns-explorer.org/phase1).  

These include:
* [Motif analysis](notebooks/vignette_analysis/motifs) of a proofread synaptic connectivity graph between pyramidal cells.
* [Functional analysis](notebooks/vignette_analysis/function) of a subset of the same pyramidal cells based on two-photon calcium imaging. The analysis relates local connectivity to function.
* [Mitochondria analysis](notebooks/vignette_analysis/mitochondria) comparing mitochondria across neuronal compartments (axon, dendrite, soma), as well as a relation between mitochondrial density and synapse density.
* [Resource statistics](notebooks/vignette_analysis/resource_statistics) that summarize neurite branch length and the expected completeness of the dendritic arbors in the volume.

See each [directory](notebooks/vignette_analysis) and our [biorxiv manuscript](https://www.biorxiv.org/content/10.1101/2020.10.14.338681v3) for more details.


# <a name="localenv"></a> Local environment
### Python packages
A local environment for running the intermediate code generation scripts can be installed using the Anaconda environment installed within the binder and the `postBuild` script. We highly recommend using [mamba](https://mamba.readthedocs.io/en/latest/index.html) to at least resolve the initial set of dependencies.
```
conda install mamba -n base -c conda-forge
mamba env create -f environment.yml
conda activate micronsbinder
```
This installs the required python packages for running the contained code.

If you'd like to use these notebooks as part of your general jupyter environment. You'll likely need to install this environment into your ipython kernels.
```
conda activate micronsbinder
python -m ipykernel install --user --name=micronsbinder
```
You can then select this python environment when opening the relevant notebooks.

### Analysis data

If you'd like to download the data or jupyter plugins for a specific analysis, you can use the `Makefile` targets to download the data for a specific notebook directory. For example, the command for the [motif analysis](notebooks/vignette_analysis/motifs) is:
```bash
make vignette_analysis/motifs
```

You can also install all data using `make all` and remove all data using `make clean`. See the `Makefile` for more options.