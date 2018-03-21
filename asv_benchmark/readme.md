# ASV-project

Benchmark suite intended to run with Airspeed-velocity:
http://asv.readthedocs.io/en/latest/
To run the benchmark, type:
asv run
in the command prompt.

About benchmarking:

Each class and function have to have a particular name, depending on its perposes.
If you fx start the benchmarks name with time, then the benchmark will measure the time. 
asv understands how to handle the prefix in either CamelCase or lowercase with underscores.
See more in the following link, under "Benchmark types": https://asv.readthedocs.io/en/latest/writing_benchmarks.html#writing-benchmarks

The default timeout for each function is 60s, which can be sometimes problematic.
In order to change it, you'll need to write in the class but not in a function; timeout = x, where x is a float variale, and is in seconds, i.e. timeout = 72.33 means that you've changed the timeout to be 72.33 seconds.

Creating a new class, with an existing class name in the following brackets, means that the new class will inherit all the functions from the class in the brackets. It's also possible to add other functions. Short example:

```
class TimeSuit():
    def time_range(self):
        code...
    def time_upper(self):
        code...
class TimeNew(TimeSuit):
    def time_upper(self):
        code...
    def time_other(self):
        code...
```        
        
The result will be that it runs the function time_range twice normally (once through TimeSuit and once through TimeNew). The function time_upper will run ones with the code in TimeSuite class, and ones with the code in TimeNew. The function time_other will run just ones.


In each benchmark you can measure a function from another place, by importing as in every python file.
The configuration file (asv.conf.json) should only have this code:
```
{
  "version": 1,
  "project": "project",
  "project_url": "https://github.com/Whichever_url",
  "repo": ".",
  "show_commit_url": "https://github.com/Same_url/commit/",
  "branches": ["master"], 
  "environment_type": "conda"
}
```
*Note that there have to be a setup file in the url.

After commiting your python files, write in the Bash: ```asv run``` then: ```asv publish```
And in order to see the graph, type: ```asv preview```, and then paste the http you get.
Sometimes problems with ```asv publish``` might accure. In this case you should check the hash of the commit in the error. If the hash isn't amoung those you get in the command ```git log```, but is in the results -> DESKTOP-53K0ASV file, then delete it from results -> DESKTOP-53K0ASV, and you are good to go.

In order to remove some commits from the graph before its running (asv run) and drawing, enter the file where you saved the benchmark project (but not the file named benchmarks) -> results -> DESKTOP-53K0ASV  then delete whichever commit you want (each commit will be assigned with its first 8 letters).

Files in this project:
1. Dummy_benchmarking.py
