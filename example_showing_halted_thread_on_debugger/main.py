import threading
import time
import sys
import traceback
import os

_current_frames = sys._current_frames
def dump_threads_on_timeout():
    print('start sleep')
    time.sleep(3)
    print('end sleep')
    with open(os.path.join(os.path.dirname(__file__), 'threads.log'), 'w') as stream:
        thread_id_to_name = {}
        try:
            for t in threading.enumerate():
                thread_id_to_name[t.ident] = '%s  (daemon: %s, pydevd thread: %s)' % (
                    t.name, t.daemon, getattr(t, 'is_pydev_daemon_thread', False))
        except:
            pass

        stream.write('===============================================================================\n')
        stream.write('Threads running\n')
        stream.write('================================= Thread Dump =================================\n')
        stream.flush()

        for thread_id, stack in _current_frames().items():
            stream.write('\n-------------------------------------------------------------------------------\n')
            stream.write(" Thread %s" % thread_id_to_name.get(thread_id, thread_id))
            stream.write('\n\n')

            for i, (filename, lineno, name, line) in enumerate(traceback.extract_stack(stack)):

                stream.write(' File "%s", line %d, in %s\n' % (filename, lineno, name))
                if line:
                    stream.write("   %s\n" % (line.strip()))

                if i == 0 and 'self' in stack.f_locals:
                    stream.write('   self: ')
                    try:
                        stream.write(str(stack.f_locals['self']))
                    except:
                        stream.write('Unable to get str of: %s' % (type(stack.f_locals['self']),))
                    stream.write('\n')
            stream.flush()

        stream.write('\n=============================== END Thread Dump ===============================')
        stream.flush()

t = threading.Thread(target=dump_threads_on_timeout)
t.pydev_do_not_trace = True
t.is_pydev_daemon_thread = True
t.start()
import mod2  # Add breakpoint here, do a step in and wait for the thread dump in threads.log (right next to this file).