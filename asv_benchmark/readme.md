# ASV-project

Assuming you have Python and pip installed, and qcodes cloned with qcodes environment.

In Bash:
1) Activate qcodes environment.
2) Enter qcodes folder (not qcodes/qcodes).
3) Type ```pip install asv``` - installing asv.
4) Type ```asv quickstart``` - now you'll have all the needed files and folders.
5) Open configuration file ```asv.conf.json```.
6) Paste the code of the configuration file from here, in the new configuration file you just created.
7) Type ```asv run``` and then ```asv machine``` - Now you've runed it all successfully for the first time. 

*You find a full basic project, with graphs, and all that asv have to offer under Basic_example.md folder, which you can follow.

Additional usefull information for every step:

* About installation - Airspeed velocity is a standard Python package, and the latest version may be installed with pip install asv. The project uses setuptools, and can also be installed by cloning the repository and using: python setup.py install. For more information: https://asv.readthedocs.io/en/latest/installing.html

* Airspeed Velocity manages building and Python virtualenvs by itself, unless told otherwise.

* Adding benchmarks - go to benchmarks folder, add python file which name starts with benchmark.

* You must import the module timeit into your benchmark file.

* Creating classes and functions - Each class and function have to have a particular name, depending on its perposes. If you fx start the functions name with time, then it will be a time benchmarking. asv understands how to handle the prefix in either CamelCase or lowercase with underscores (fx def time_measure and def TimeMeasure). See more in the following link: https://asv.readthedocs.io/en/latest/writing_benchmarks.html#benchmark-types

* The default timeout for each function is 60s, which can be sometimes problematic. In order to change it, you'll need to write in the class but not in a function; timeout = x, where x is a float variale, and is in seconds, i.e. timeout = 72.33 means that you've changed the timeout to be 72.33 seconds.

* Precis measurements - for the most accurate measurements, try to put as much as possible in the setup and teardown functions, and less in the functions you want to benchmark.You'll find a complete explanation for every type of function in here: https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

* Importing modules - as in every Python file.

* Usefull options for ```asv run``` - add ```--show-stderr``` to see the results (if a function have outputs) and full explanation of errors/possible errors. Another option is adding ```--python=python``` if you don't want the program to reinstall everything every time you run it, so you won't need to wait to long. See more here: https://asv.readthedocs.io/en/latest/writing_benchmarks.html#running-benchmarks-during-development

* About graph - After commiting your python files, type: ```asv run``` then: ```asv publish``` And in order to see the graph, type: ```asv preview```, and then paste the http you get. Sometimes problems with ```asv publish``` might accure. In this case you should check the hash of the commit in the error. If the hash isn't amoung those you get in the command ```git log```, but is in the results -> DESKTOP-53K0ASV file, then delete it from results -> DESKTOP-53K0ASV, and you are good to go. If there's problems with ```asv preview``` then you'll probably have to change the port. Do that by typing ```asv preview --port 8081```, which will change the port to port number 8081, instead of the default, which is normally 8080.

If you have any problem not explained here, please message me on: adir7saly@gmail.com , or see if you can find an answer here (if not, create a new issue): https://github.com/airspeed-velocity/asv/issues

Files in this project:
1. Basic_example.md - example to follow for everything about using Airspeed Velocity (except for electronic devices).
2. experimental.py and benchmarks1.
3. benchmark_el.py - using asv on electronic devices (the example here is on KEYSIGHT34465A).
4. benchmark.py.
5. General explanation (not just for QCoDes) - https://github.com/Adir7SK/ASV-project
6. Program creater - https://github.com/airspeed-velocity/asv
