# OSIRISPY

`osirispy` is a python package for reading simulation
output for the particle-in-cell code OSIRIS. It utilizes the numpy interface to provide
a simple way to readsimulation output.

## Installing osirispy

`osirispy` is available on PyPI. You can install it by running the following
command inside your terminal

```shell
pip install osirispy

pip3 install osirispy
```


## Using osirispy

import the package in python 

```python3
import osirispy as ospy
```

You can use the function `ospy.read()` to read osiris files. It will give a different output based on the type of file that is being opened.

### grid files

Grid files are the output of vdf objects and can have between 1 and 3 dimensions. They can represent charge density, current, E.M. fields, phasespaces, etc... 

`ospy.read("/path/to/grid.h5")` will output a `grid` object when reading a grid-type file.
The data is a numpy array accessible at `grid.data`
The object also contains a list of axis containing the physical dimentions of the grid file at `grid.axis`.


### particle (aka RAW) files

Particle files contain the  output of the RAW diagnostic for a given species at a given time-step. 
RAW files contain information on the quantities `x1`,`x2`,`x3`,`p1`,`p2`,`p3`,`ene`.
`ospy.read(filepath,req_quantitites)` will output a `raw` object with the required quantities specified with a list of strings on the `req_quantities` parameter.

The data is a python dictionary of numpy arrays accessible at grid data. An example is given below:

```python3
# read raw data
rawdata=ospy.read("/path/to/raw.h5",("x1","x2"))
#access x1 array
x1=rawdata.data["x1"]
```

The object also contains a dictionary with the label of each quantity accessible at `raw.label`.


### track  files

Track files contain the output of the tracks diagnostic for a given species . 
Track files contain information on the quantities `t`,`x1`,`x2`,`x3`,`p1`,`p2`,`p3`,`ene`.
`ospy.read(filepath,req_quantitites)` will output a `tracks` object 

The data is a python dictionary of a list of numpy arrays accessible at grid data. An example is given below:

```python3
# read tracks data
trackdata=ospy.read("/path/to/track.h5",("x1","x2"))
#access x1 array of particle i
x1=trackdata.data["x1"][i]
```

The object also contains a dictionary with the label of each quantity accessible at `raw.label`.

