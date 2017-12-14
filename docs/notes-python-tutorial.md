### Reading "The Python Tutorial"

* The Python Tutorial: <https://docs.python.org/3/tutorial/index.html>

(1.) Whetting Your Appetite: <https://docs.python.org/3/tutorial/appetite.html>

(2.) Using the Python Interpreter: <https://docs.python.org/3/tutorial/interpreter.html>
    - Invoking the Interpreter

-------------
On itm-gpaolo-w10, Python 3.6.1.1150.0 (32-bit) was installed under `C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32`.

Shortcuts are available under `C:\Users\gmcario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.6`:
- IDLE (Python 3.6 32-bit)
- Python 3.6 (32-bit)
- Python 3.6 Module Docs (32-bit)

**NOTE**: IDLE = Python's **I** ntegrated **D** eve **L** opment **E** nvironment

Under Cygwin @itm-gpaolo-w10 we also have Python 2.7.12 installed under `/usr/bin/python`

```
gmacario@ITM-GPAOLO-W10:~ $ which python
/usr/bin/python
gmacario@ITM-GPAOLO-W10:~ $ python --version
Python 2.7.12
gmacario@ITM-GPAOLO-W10:~ $
```

-------------

Invoking

* `python3.6`
* `python -c command [arg] ...`
* `python -m module [arg] ...`

    - The Interpreter and Its Environment

(3.) An Informal Introduction to Python: <https://docs.python.org/3/tutorial/introduction.html>

(4.) More Control Flow Tools: <https://docs.python.org/3/tutorial/controlflow.html>

PEP = Python Enhancement Proposal - see <https://www.python.org/dev/peps/>

(5.) Data Structures: <https://docs.python.org/3/tutorial/datastructures.html>

(6.) Modules: <https://docs.python.org/3/tutorial/modules.html>

```
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\gmacario\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> for k in range(len(sys.path)):
	print(k, sys.path[k])


0
1 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32\Lib\idlelib
2 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32\python36.zip
3 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32\DLLs
4 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32\lib
5 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32
6 C:\Users\gmacario\AppData\Local\Programs\Python\Python36-32\lib\site-packages
>>>
```

(7.) Input and Output: <https://docs.python.org/3/tutorial/inputoutput.html>

(8.) Errors and Exceptions: <https://docs.python.org/3/tutorial/errors.html>

(9.) Classes: <https://docs.python.org/3/tutorial/classes.html>

(10.) Brief Tour of the Standard Library: <https://docs.python.org/3/tutorial/stdlib.html>

(11.) Brief Tour of the Standard Library - Part II: <https://docs.python.org/3/tutorial/stdlib2.html>

(12.) Virtual Environments and Packages: <https://docs.python.org/3/tutorial/venv.html>

(13.) What Now?: <https://docs.python.org/3/tutorial/whatnow.html>

<!-- EOF -->
