# Overview

Notes on the SciPy Stack and its associated packages

# References

* [NumPy](http://www.numpy.org/)
* [ScyPy](https://www.scipy.org/)
* [SymPy](https://www.sympy.org/en/index.html)
* [Anaconda](https://www.anaconda.com/)
* [Pyzo](http://www.pyzo.org/)

# SciPi Stack

**NumPy** is part of the **SciPy Stack** which includes:

* Python (2.x >= 2.6 or 3.x >= 3.2)
* NumPy (>= 1.6)
* SciPy library (>= 0.10)
* Matplotlib (>= 1.1)
* dateutil
* pytz

With support for at least one backend:

* IPython (>= 0.13)
* pyzmq
* tornado
* pandas (>= 0.8)
* Sympy (>= 0.7)
* nose (>= 1.1)

Other software commonly used:

* Anaconda
* Pyzo
* jupyter notebook
* jupyter lab
* Spyder
* VSCode

# Install Windows (including Anaconda install info)

I initially installed [Pyzo](http://www.pyzo.org/), and per its recommendation I installed **Anaconda** (**Miniconda for Windows (64-bit)**, because it makes it easier to install scientific packages.  After doing so I now have two Python interpreters on my Windows 10 system, neither of which is on the environment path.  With **Anaconda** this wasn't to much of an issue since it has its own **Andaconda Prompt** utility that runs Python without being on the path.  But **VSCode** could not find it so I ended up adding it to the path anyway.

Anaconda's Getting Started document shows it also installed with the Anaconda Navigator, which I did not have.  I found this could be installed from within the **Anaconda Prompt** as follows:

```
conda install anaconda-navigator
````

To get **numpy** installed I ran the following from the **Pyzo shell**:

```
install numpy
```

This uses the Anaconda installer, so you might as well do it directly in the **Anaconda Prompt** with:

```
conda install numpy
```

I then tested it in a Python script with the following **import command**:

```python
import numpy as np
```

# Install Linux

Installed on Ubuntu running in **Linux Subsystem for Windows**.  I initially installed it using the **sudo apt-get install python-numpy** command.  It appeared to install correctly, but it wasn't recognized by the Python **import** command, either as numpy or python-numpy.  After researching I first installed via **pip (Python Package Index)** utility, which I had to install first with **sudo apt-get install python-pip python3-pip** command, it then recommend I upgrade using **sudo pip install --upgrade pip**.  Finally I installed **NumPy** (after first removing my prior install) using the following command:

```bash
sudo pip3 install -U numpy
```

This time Python successfully recognize **NumPy** with the following **import** command:

```python
sudo pip3 install -U numpy
```

# Mathplotlib

## Colors and Specifiers

The plot colors are based on **MatLab format strings** and are specified in the plot parameters as strings.  For example,
**plt.plot(xpoints, ypoints, 'b-',xpoints, ypoints, 'ro')**, where 'b-' specifies a blue line and 'ro' specifies a red point.


### MatLab Colors
Long Name | Short Name | RGB Triplet |
----------|------------|-------------|
blue | b | [0,0,1] |
black | k [0,0,0] |
red |r | [1,0,0] |
green |g | [0,1,0] |
yellow| y | [1,1,0] |
cyan | c | [0,1,1] |
magenta | m [1,0,1] |
white	w	[1,1,1]
