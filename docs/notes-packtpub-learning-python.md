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
py -m venv lpenv
lpenv\Scripts\activate.bat
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


<!-- TODO -->

<!-- EOF -->
