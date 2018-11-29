if __name__ == '__main__':
    import sys
    print('Python version info:\n%s\n' % (sys.version,))
    import time
    import threading

    start_time = time.time()

    def trace_dispatch(frame, event, arg):
        if frame.f_code.co_filename.endswith('mod2.py'):
            print('will sleep inside trace_dispatch on thread %s %.2fs' % (threading.current_thread(), time.time() - start_time))
            time.sleep(10)  # Sleep inside of trace_dispatch actually prevents any import from working in any thread.
            print('end sleep inside trace_dispatch thread %s %.2fs' % (threading.current_thread(), time.time() - start_time))

    sys.settrace(trace_dispatch)

    class MyThread(threading.Thread):

        def run(self):
            for i in range(3):
                time.sleep(.2)
                print('will import sys on thread %s %.2fs' % (threading.current_thread(), time.time() - start_time))
                import sys  # Will actually halt until the sleep on the trace_dispatch resumes in the main thread!
                print('finished importing sys on thread %s %.2fs' % (threading.current_thread(), time.time() - start_time))

    t = MyThread()
    t.daemon = True
    t.start()
    import mod2
    time.sleep(3)  # Show that the sys import executes