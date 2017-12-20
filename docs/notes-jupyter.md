# Running Jupyter on itm-gpaolo-w10

Open a Windows shell (NOT a Cygwin shell) and type the following commands

```
C:
cd \Users\gmacario\Dropbox\github\gmacario\learning-python
py -m venv .lpenv
.lpenv\Scripts\activate.bat

pip install jupyter
pip install Faker numpy pandas delorean matplotlib
pip install openpyxl
pip freeze >requirements.txt

jupyter notebook
```

Your browser should open URL <http://localhost:8888/tree>

To run against the already created venv

```
C:
cd \Users\gmacario\Dropbox\github\gmacario\learning-python
.lpenv\Scripts\activate.bat

jupyter notebook
```
