# Notes reading book "PacktPub - Learning Python" by Fabrizio Romano (December 2015)

<!-- 2017-10-06 17:00 CEST -->

* Book Homepage: <https://www.packtpub.com/application-development/learning-python>
* Read book online at Mapt: <https://www.packtpub.com/mapt/book/application_development/9781783551712>
* Code files available at <https://www.packtpub.com/lcode_download/22033>
* PDF: `My_E-Books\PacktPub-Learning_Python_(2015-12)\w_pac45.pdf` (PDF, 443 pages)

### Install Python on itm-gpaolo-w10

Tested on IDLE running on itm-gpaolo-w10

```
>>> import sys
>>> print(sys.version)
3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)]
>>>
```

<!-- 2017-10-20 14:45 CEST -->

Update Python installation to latest release for Windows x86-64 available at <https://www.python.org/downloads/windows/>

```
>>> import sys
>>> print(sys.version)
3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]
>>> import os
>>> print(os.getcwd())
C:\Users\gmacario\AppData\Local\Programs\Python\Python36
>>>
```

### Running virtualenv on itm-gpaolo-w10

Use command `py -m venv <DIRECTORY>` - example

```
D:
cd \data\github\gmacario\learning-python
py -m venv .lpenv
.lpenv\Scripts\activate.bat
```

Result:

```
C:\Users\gmacario>D:

D:\>cd \data\github\gmacario\learning-python

D:\data\github\gmacario\learning-python>py -m venv .lpenv

D:\data\github\gmacario\learning-python>.lpenv\Scripts\activate.bat
(.lpenv) D:\data\github\gmacario\learning-python>
```

**NOTE**: You should add file `.gitignore` to avoid checking in the files created by virtualenv

Within the `(.lpenv)` prompt you may now directly invoke `python`, `pip`, etc.

```
pip list
pip install virtualenv
python lpbook/ch1/bike.py
```

To terminate the virtualenv type the following command

```
deactivate.bat
```

### Launching IDLE inside a virtualenv

This is useful if you want to install additional libraries (using pip as described above)

```
(.lpenv) D:\data\github\gmacario\learning-python>python -m idlelib
```

Example

```
pip install requests
python -m idlelib
```

Then open `findpeople/medium_find.py` and run it

### Running the Python debugger

Inside a properly created virtualenv

```
python -m pdb findpeople/finder.py
```

Result

```
(.lpenv) D:\data\github\gmacario\learning-python>python -m pdb findpeople/finder.py
> d:\data\github\gmacario\learning-python\findpeople\finder.py(5)<module>()
-> import click
(Pdb) c
Hello, world!
DEBUG: get_interesting_users: username=gmacario
Looking for interesting users for gmacario...
Retrieving user ID...
DEBUG: get_user_id: url=https://medium.com/@gmacario?format=json
DEBUG: get_interesting_users: user_id=e43f1f66533d
Retrieving users from Followings...
DEBUG: get_interesting_users: usernames=['voltera', 'gdgtorino', 'TrackR', 'codeschool', 'googleyasheck', 'benjaminhardy', 'echoconnectkeys', 'docker', 'Indiegogo', 'ContinoHQ', 'rogermud', 'gitlab', 'lewisshepherd', 'Samaritan_o', 'Nextclouders', 'benjaminjfoley', 'CNET', 'porteneuve', 'timoreilly', 'be.betr.codr', 'resin_io', 'fulcorno', 'MediumStaff', 'alexsimo', 'neskov7', 'Cars_Joel', 'UDOO_Board', 'producthunt', 'webagnus', 'Backfeed_cc', 'badelfceo', 'AndroidDev', 'alekshnayder', 'z80mikael', 'OpenBadges', 'marcocamisanicalzolari']
Retrieving the latest posts...
...
```

### Run a Python script from the Python shell

As an alternative to `python findpeople/finder.py`, type the following commands inside a Python shell:

```
import findpeople.finder
findpeople.finder.main()
```

Result:

```
(.lpenv) D:\data\github\gmacario\learning-python>python
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import findpeople.finder
Hello, world!
>>> findpeople.finder.main()
DEBUG: get_interesting_users: username=gmacario
Looking for interesting users for gmacario...
Retrieving user ID...
DEBUG: get_user_id: url=https://medium.com/@gmacario?format=json
DEBUG: get_interesting_users: user_id=e43f1f66533d
Retrieving users from Followings...
DEBUG: get_interesting_users: usernames=['voltera', 'gdgtorino', 'TrackR', 'codeschool', 'googleyasheck', 'benjaminhardy', 'echoconnectkeys', 'docker', 'Indiegogo', 'ContinoHQ', 'rogermud', 'gitlab', 'lewisshepherd', 'Samaritan_o', 'Nextclouders', 'benjaminjfoley', 'CNET', 'porteneuve', 'timoreilly', 'be.betr.codr', 'resin_io', 'fulcorno', 'MediumStaff', 'alexsimo', 'neskov7', 'Cars_Joel', 'UDOO_Board', 'producthunt', 'webagnus', 'Backfeed_cc', 'badelfceo', 'AndroidDev', 'alekshnayder', 'z80mikael', 'OpenBadges', 'marcocamisanicalzolari']
Retrieving the latest posts...
...
```

**TODO**: Understand how to pass command line parameters

---------------------

### Print global namespace (with keys in ascending order)

```
>>> for d in sorted(globals()): print(d, "==>", globals().get(d))
...
__annotations__ ==> {}
__builtins__ ==> <module 'builtins' (built-in)>
__doc__ ==> None
__loader__ ==> <class '_frozen_importlib.BuiltinImporter'>
__name__ ==> __main__
__package__ ==> None
__spec__ ==> None
a ==> 1000000
b ==> 1000000
c ==> {'A': 1, 'Z': -1}
csv ==> <module 'csv' from 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36\\lib\\csv.py'>
d ==> d
e ==> {'Z': -1, 'A': 1}
get_squares ==> <function get_squares at 0x0000020673A5A510>
get_squares_gen ==> <function get_squares_gen at 0x0000020673A5A620>
number ==> 9
os ==> <module 'os' from 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36\\lib\\os.py'>
s ==> <generator object get_squares_gen at 0x0000020673A58830>
square ==> <function square at 0x00000206739D4E18>
this ==> <module 'this' from 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36\\lib\\this.py'>
>>>
```

### Notes on Chapter 5 (Data Science)

<!-- 2017-10-31 18:03 CEST -->

* Page 282: Python Package `fake-factory` has been replaced with `Faker` (TBV) - Adjust the command at line 280 accordingly
* Page 282: Remember that Panda stands for Python Data Analysis Library - See TODO:URL

TODO: Add commands to create the virtualenv able to run jupyter

To launch Jupyter on itm-gmacario-w10, open a Wndows Command Shell (Start > cmd) then type the following commands

```
d:
cd \data\github\gmacario\learning-python\.venv
Scripts\activate.bat
cd \data\github
jupyter notebook
```

<!-- TODO -->

<!-- EOF -->
