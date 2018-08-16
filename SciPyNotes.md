# Overview

Notes on the SciPy Stack and its associated packages

# References

## Anaconda and SciPy Stack

* [Anaconda](https://www.anaconda.com/)
* [NumPy](http://www.numpy.org/)
* [ScyPy](https://www.scipy.org/)
* [SymPy](https://www.sympy.org/en/index.html)
* [Matplotib](https://matplotlib.org/)
* [Pandas](https://pandas.pydata.org/)
* [IPython](https://ipython.org/)
* [Jupyter](https://jupyter.org/)
* [Pyzo](http://www.pyzo.org/)

## Jupyter References

* [Jupyter Gallery](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#introductory-tutorials)
* [Jupyter Notebbok Viewer](https://nbviewer.jupyter.org/)

## YouTube Videos

* [SciPy Overview](https://www.youtube.com/watch?v=MtdLd2lrvag)
* [Jupyter Notebook Tutorial](https://www.youtube.com/watch?v=HW29067qVWk)

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

## Anaconda Install

I initially installed [Pyzo](http://www.pyzo.org/), and per its recommendation I installed **Anaconda** (**Miniconda for Windows (64-bit)**, because it makes it easier to install scientific packages.  After doing so I now have two Python interpreters on my Windows 10 system, neither of which is on the environment path.  With **Anaconda** this wasn't to much of an issue since it has its own **Andaconda Prompt** utility that runs Python without being on the path.  But **VSCode** could not find it so I ended up adding it to the path anyway.

Anaconda's Getting Started document shows it also installed with the Anaconda Navigator, which I did not have.  I found this could be installed from within the **Anaconda Prompt** as follows:

```
conda install anaconda-navigator
````
## Numpy Install using Anaconda

```
conda install numpy
```

**import** in Python using the standard shortcut namespace:

```python
import numpy as np
```

## SciPy Install using Anaconda

```
conda install scipy
```

With **SciPy" you import the individual module(s) needed:

```python
from scipy import linalg
from scipy import integrate
```

## SymPy Install using Anaconda

```
conda install sympy
```

**import** in Python:

```python
import sympy
```

## MatPlotLib Install using Anaconda

```
conda install matplotlib
```

**import** in Python using the standard shortcut namespace for pyplot:

```python
import matplotlib.pyplot as plt
```

## Jupyter Install using Anaconda

```
conda install jupyter
```

To run a **Jupyter notebook** from within **Anaconda Prompt**

```python
jupyter notebook
```

## IPython Install using Anaconda

Note: I'm pretty sure this was installed by the **Jupyter install**, if not then by Anaconda's own install itself.  I ran the following command which showed it was installed

```
conda update ipython
```

To run the **IPython shell** from within **Anaconda Prompt**

```
ipython
```

To include an **IPython** package:

```python
from IPython.display import HTML
```

## Numpy Install using Anaconda

```
conda install numpy
```
**import** in Python using the standard shortcut namespace:

```python
import numpy as np
```

## Pandas Install using Anaconda

```
conda install pandas
```

**import** in Python using the standard shortcut namespace:

```python
import pandas as pd
```


# Install Linux

## Numpy Install

Installed on Ubuntu running in **Linux Subsystem for Windows**.  I initially installed it using the **sudo apt-get install python-numpy** command.  It appeared to install correctly, but it wasn't recognized by the Python **import** command, either as numpy or python-numpy.  After researching I first installed via **pip (Python Package Index)** utility, which I had to install first with **sudo apt-get install python-pip python3-pip** command, it then recommend I upgrade using **sudo pip install --upgrade pip**.  Finally I installed **NumPy** (after first removing my prior install) using the following command:

```bash
sudo pip3 install -U numpy
```

This time Python successfully recognize **NumPy** with the following **import** command:

```python
sudo pip3 install -U numpy
```

# Uppdating Packages using Anaconda

Use the **conda update command** instead of **conda install**, for example:

```
conda update jupyter
conda update ipython
```

# Anaconda

## Refer to

* [Anaconda](https://www.anaconda.com/)


# SciPy

## Refer to

* [ScyPy](https://www.scipy.org/)

# NumPy

## Refer to

* [NumPy](http://www.numpy.org/)

# SymPy

## Refer to

* [SymPy](https://www.sympy.org/en/index.html)

# Mathplotlib

## Refer to

* [Matplotib](https://matplotlib.org/)
* [pyplot_tutorial](https://matplotlib.org/users/pyplot_tutorial.html)

## Colors and Specifiers

The plot colors are based on **MatLab format strings** and are specified in the plot parameters as strings.  For example,
**plt.plot(xpoints, ypoints, 'b-',xpoints, ypoints, 'ro')**, where 'b-' specifies a blue line and 'ro' specifies a red point.


### MatLab Colors
Long Name | Short Name | RGB Triplet |
----------|------------|-------------|
blue      | b          | [0,0,1]     |
black     | k          | [0,0,0]     |
red       |r           | [1,0,0]     |
green     |g           | [0,1,0]     |
yellow    | y          | [1,1,0]     |
cyan      | c          | [0,1,1]     |
magenta   | m          | [1,0,1]     |
white     | w          | [1,1,1]     |

# Pandas

Python Data Analysis Library

## Refer to

* [Pandas](https://pandas.pydata.org/)

# IPython

## Refer to

* [IPython](https://ipython.org/)

# Jupyter

## Refer to

* [Jupyter](https://jupyter.org/)
* [Jupyter Gallery](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#introductory-tutorials)

## Displaying Notebooks on GitHub

The **Jupyter notebooks** are in a **JSON** format and can be displayed directly on **GitHub**.  It does a fairly good job of displaying it as markdown, which this format supports.  It does have some issues with **embedded html**, such as **iframes** and header **styles**.  A better display option which will display the notebook without these issues is to open the **GitHub repository notebook** using **nbviewer**.  The downside is that it will only display **public** repo notebooks.  Here is an example of **nbviewer** using my first notepook:

![FirstNotebook](http://nbviewer.jupyter.org/github/GitLeeRepo/JupyterNotebooksPub/blob/master/FirstNotebook.ipynb)
![FirstNotebook](http://nbviewer.jupyter.org/github/GitLeeRepo/JupyterNotebooksPub/blob/master/FirstNotebook.ipynb)

## HTML/PDF/Markdown Versions of Jupyter Notebooks

### Markdown

A **Jupyter notebook** can be saved as an **markdown** file.  For example in in my **SciPy repository**:

This is not really necessary for **GitHub** since it will already disply a **Jupyter notebook** since it is **JSON** wiith markdown in it.  It has the same issues mentions here.  The better option as mentioned above is to display it by adding it to **nbviewer** link as shown above, although it has to be a **public** repository.

![FirstNotebook](https://github.com/GitLeeRepo/SciPy/blob/master/Notebooks/Export/Markdown/FirstNotebook/FirstNotebook.md)

For the most part everything displays fine.  It does use some embedded html for some things, which works in some cases (tables work form example), and in others such as iframes and header styles it doesn't render, but displays the hmtml instead.
