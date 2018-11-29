Example showing issue with debugger. Open `main.py`, add breakpoint in the `import mod2` statement, launch
the file in the debugger then do a step in and wait for the threads.log to be generated to see the running
threads.

It's possible to see that pydevd.Writer is locked in in an import in the stack and it'll be there forever because the user thread is suspended
inside of the `import mod2` call.

 File "/home/fabioz/.vscode/extensions/ms-python.python-2018.10.1/pythonFiles/experimental/ptvsd/ptvsd/wrapper.py", line 2479, in on_pydevd_thread_suspend
   xml = self.parse_xml_response(args)
 File "/home/fabioz/.vscode/extensions/ms-python.python-2018.10.1/pythonFiles/experimental/ptvsd/ptvsd/wrapper.py", line 1405, in parse_xml_response
   return untangle.parse(io.BytesIO(args.encode('utf8'))).xml
 File "/home/fabioz/.vscode/extensions/ms-python.python-2018.10.1/pythonFiles/experimental/ptvsd/ptvsd/untangle.py", line 183, in parse
   parser = make_parser()
 File "/home/fabioz/miniconda3/envs/py27/lib/python2.7/xml/sax/__init__.py", line 81, in make_parser
   return _create_parser(parser_name)
 File "/home/fabioz/miniconda3/envs/py27/lib/python2.7/xml/sax/__init__.py", line 105, in _create_parser
   drv_module = __import__(parser_name,{},{},['create_parser'])