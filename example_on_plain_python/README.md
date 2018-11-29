Example showing CPython 2.7 halting all imports in any thread when tracing is paused during import.

It goes something like:

python2.7 main.py

Will set a sys.settrace() method which will do a sleep inside the import statement for `mod2.py`,
then, it'll start a thread which will simply do an import and that thread will be halted until
the tracing resumes.

The output which is expected on Pyhon 2.7 with this program is below (note how 10 seconds are
elapsed before the secondary thread resumes executing because the main thread is inside an import
which is halted in the trace function).

```
Python version info:
2.7.15 |Anaconda, Inc.| (default, May  1 2018, 23:32:55) 
[GCC 7.2.0]

will sleep inside trace_dispatch on thread <_MainThread(MainThread, started 140046171518336)> 0.00s
will import sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 0.20s
end sleep inside trace_dispatch thread <_MainThread(MainThread, started 140046171518336)> 10.00s
Actually finished importing mod2.py
finished importing sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 10.00s
will import sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 10.20s
finished importing sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 10.20s
will import sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 10.40s
finished importing sys on thread <MyThread(Thread-1, started daemon 140046127834880)> 10.40s
```