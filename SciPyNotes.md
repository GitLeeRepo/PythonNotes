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

## Books

* [PythonDataScienceHandbook Online version](https://jakevdp.github.io/PythonDataScienceHandbook/)
* [Notebooks for PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook)
* [Notebooks for Python for Data Analysis](https://github.com/wesm/pydata-book)

## YouTube Videos

* [SciPy Overview](https://www.youtube.com/watch?v=MtdLd2lrvag)
* [Jupyter Notebook Tutorial](https://www.youtube.com/watch?v=HW29067qVWk)
* [Anaconda Tutorial](https://www.youtube.com/watch?v=YJC6ldI3hWk)

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

## References

* [Anaconda](https://www.anaconda.com/)
* [Anaconda Tutorial](https://www.youtube.com/watch?v=YJC6ldI3hWk) YouTube video

Refer to the section **Anaconda vs PIP** in the **PIP Package Manager** section on differences between **pip** and **conda**  

## Conda Commands

* Conda help
* Conda install /<package\> - if you ever have issues with conda (I never have) you can use **pip install** as an alternative.
* Conda update /<package\>
* Conda list - list installed packages.  Note those that begin with **py** in the **Build Column** are also listed by **pip list**
* conda create --name my_app /<list of packages for the environment\>  --> create a new **environment**
* activate my_app - activate the named environment you previously created
* deactivate my_app - deactivate the current environment
* conda env list - list the environments that have been created
* conda info --envs -  info on enviroments that have been created

## Virtual Environments

You can create **virtual enironments** in **Anaconda** so that you can have different environments for different versions of Python and the various packages.  You create an new environment by entering:

```bash
conda create --name my_app /<list of packages for the environment\>
```

To **activate** the environment:

```bash
activate my_app
# note that on Mac or Linux it is "source activate my_app*
```

The name of your current environment displays above your **prompt**.  The default environment is **base**.

To **deactivate** the environment:

```bash
deactivate my_app
# note that on Mac or Linux it is "source deactivate my_app*
```

To list the environments available:

```bash
conda env list
# or for info
conda info --envs
```

To install a Python 2.7 Enviroment

```bash
conda create --name my_py27 python=2.7 /<list of packages for the environment\>
```

To remove an environtment:

```bash
conda remove --name my_app --all
# will remove all packages and the environment
# or
conda remove --name my_app /<list of packages in the environment\>
# to remove specific packages
```

# SciPy

## References

* [ScyPy](https://www.scipy.org/)

# NumPy

## References

* [NumPy](http://www.numpy.org/)

# SymPy

## References

* [SymPy](https://www.sympy.org/en/index.html)

# Mathplotlib

## References

* [Matplotib](https://matplotlib.org/)
* [pyplot_tutorial](https://matplotlib.org/users/pyplot_tutorial.html)
* [Matplotlib GitHub](https://github.com/matplotlib/matplotlib)

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

## References

* [Pandas](https://pandas.pydata.org/)

**Python Data Analysis Library**.  **Pandas** main focus is on **dataframes**.  

**Dataframes** are very much like **spreadsheets**.  Pandas and dataframes have the advantage over spreadsheets in that they **scale up** much better, whereas an **Excel spreadsheet** can really start to bog down if it gets too big.

**Pandas** like **SciPy** and **NumPi** is written in the **C programming language**

## Installations/Updates

2018-08-16 - installed pandas-datareader (pandas itself was previously installed)

## Issues

Received an error when trying to import **pandas_datareader.data** with the **is_list_like** object, a Google seach found the **pd.core.common.is_list_like = pd.api.types.is_list_like** fix for this by placing it before the **import**.

```python
import pandas as pd
import datetime
# the following is needed to prevent import pandas_datareader.data as web from throwing an error
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
```
# IPython

## References

* [IPython](https://ipython.org/)

## Keyboard Shortcuts

* **Ctl-D** - Exit IPython

## Magic Commands

Refer to the **Jupyter** section.

## Tips

* **mutliline input** - use **%cpaste** magic. This is intended for pasting code, but has the side effect of enabling multiline input.
* **copy multiline code to clipboard** - by using the **history \<index\>** (where index is the number in the input brackets) you will display the text without the leading dashes, which can then be highlighted and pasted.

# Jupyter

## References

* [Jupyter](https://jupyter.org/)
* [Jupyter Gallery](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#introductory-tutorials)

## Keyboard Shortcuts

* **Shift-Tab** - display the signature of the function or object under the cursor

## Magic Commands

* **%cpaste** - more useful for **IPython** by using it to allow **multiline** input.  Its intention was to allow you to paste code into **IPython**, but you really don't need this to do that, just paste it.
* **history \<index\>** -  displays the entry from a prior **input cell** by referring to its **index** number in its brackets

## Displaying Notebooks on GitHub

The **Jupyter notebooks** are in a **JSON** format and can be displayed directly on **GitHub**.  It does a fairly good job of displaying it as markdown, which this format supports.  It does have some issues with **embedded html**, such as **iframes** and header **styles**.  A better display option which will display the notebook without these issues is to open the **GitHub repository notebook** using **nbviewer**.  The downside is that it will only display **public** repo notebooks.  Here is an example of **nbviewer** using my first notepook:

[FirstNotebook](http://nbviewer.jupyter.org/github/GitLeeRepo/JupyterNotebooksPub/blob/master/FirstNotebook.ipynb)

## HTML/PDF/Markdown Versions of Jupyter Notebooks

### Markdown

A **Jupyter notebook** can be saved as an **markdown** file.  For example in in my **SciPy repository**:

This is not really necessary for **GitHub** since it will already disply a **Jupyter notebook** since it is **JSON** wiith markdown in it.  It has the same issues mentions here.  The better option as mentioned above is to display it by adding it to **nbviewer** link as shown above, although it has to be a **public** repository.

[FirstNotebook](https://github.com/GitLeeRepo/SciPy/blob/master/Notebooks/Export/Markdown/FirstNotebook/FirstNotebook.md)

For the most part everything displays fine.  It does use some embedded html for some things, which works in some cases (tables work form example), and in others such as iframes and header styles it doesn't render, but displays the hmtml instead.

# PIP Package Utility

## References

tbd

## Installation

Installed on 2018-08-16 from the **Anaconda prompt**:

```
python -m pip install --upgrade pip
```

It could have also been installed with

```
conda install pip
```

## PIP Commands

* pip help
* pip list
* pip install
* pip show - show information on packages

## Blog Post on PIP vs Conda

Having been involved in the python world for so long, we are all aware of pip, easy_install, and virtualenv, but these tools did not meet all of our specific requirements. The main problem is that they are focused around Python, neglecting non-Python library dependencies, such as HDF5, MKL, LLVM, etc., which do not have a setup.py in their source code and also do not install files into Python’s site-packages directory.

So Conda is a packaging tool and installer that aims to do more than what pip does; handle library dependencies outside of the Python packages as well as the Python packages themselves. Conda also creates a virtual environment, like virtualenv does.

As such, Conda should be compared to Buildout perhaps, another tool that lets you handle both Python and non-Python installation tasks.

Because Conda introduces a new packaging format, you cannot use pip and Conda interchangeably;  pip cannot install the Conda package format. You can use the two tools side by side (by installing pip with conda install pip) but they do not interoperate either.
