
# Overview

Installation notes for the ScyPy stack.  Refer to my [SciPyStackNotes](https://github.com/GitLeeRepo/PythonNotes/blob/master/SciPyStackNotes.md#overview) for the majority of non-install notes and references.

# References

## My Other Notes

* [SciPyStackNotes](https://github.com/GitLeeRepo/PythonNotes/blob/master/SciPyStackNotes.md#overview)

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

## Issue installing sympy and pandas


Note these python packages are installed in:

```
/usr/local/lib/python2.7
/usr/local/lib/python3.5
```
for python3:

```
/usr/local/lib/python3.5/dist-packages
```

which contains

```
isympy.py  
mpmath  
mpmath-1.0.0.dist-info  
numpy  
numpy-1.15.0.dist-info  
pandas
pandas-0.23.4.dist-info
__pycache__  
sympy  
sympy-1.2.dist-info
```

Note that when using **sudo** with pip or pip3 installs you need to **include the -H flag**, **sudo -h pip install**, or else you get the following warning/error (think just a warning since some installs with this were successful):

```
The directory '/home/tracy/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/tracy/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
```

The sudo -H will use the invoking user's permissions

ran

```bash
$pip3 install pandas
```
Note this was without sudo or sudo -H and it worked (but sympy didn't and needed sudo -H).  Later (see below) discovered that even though this worked and **import pandas** worked, pandas didn't appear in the **/usr/local/lib/python3.5/dist-packages directory**, but it did appear in the **python2.7** directory

I reran with **sudo -H** and it now shows up there

When installing **pandas** It gives info message about upgrading pip:

```bash
You are using pip version 8.1.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
### Issue started here

```bash
$pip3 install --upgrade pip
```

This worked but **broke my pip3** (online posts said it breaks the system installed pip)

**Evidence it broke** was when:
Running sympy install

```bash
$pip3 install sympy
#and
$sudo -H pip3 install sympy
```

failed with:

```bash
Traceback (most recent call last):
  File "/usr/bin/pip3", line 9, in <module>
    from pip import main
ImportError: cannot import name 'main'
```

I tried a suggested fix of uninstalling and reinstalling pip/pip3 with:

```bash
$sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
```

This ran successfully but didn't fix the issue.  But after the fix that did work, by starting a **new shell**, when I exited back I was able to later run the install **$sudo -H pip3 install pandas**, so **maybe it eventually got sorted out and did work**.

### Fix starts here

Another suggestion, which **did work**, was to start a new bash shell, which won't be affected by the broken pip3

```bash
$bash
```

tried installing sympy first without sudo, got most of the way through, but failed trying to copy to \usr\lib directory

```bash
$sudo -H pip3 install sympy
```

Finally **this worked** and the **import sympy also worked**

I then noticed **pandas** wasn't in the **/usr/local/lib/python3.5/dist-packages** directory.  So I reinstalled with **sudo -H**

```bash
$sudo -H pip3 install pandas
```

When I ran this I had exited back to the **original shell** and now the **pip3 install** worked.  Not sure if it will was just in this case or whether it will now work correctly in all other cases.

It continued to work (not sure how it worked before, it was in the **python2.7** directory, but more likely it was in my local environment)


# Uppdating Packages using Anaconda

Use the **conda update command** instead of **conda install**, for example:

```
conda update jupyter
conda update ipython
```
