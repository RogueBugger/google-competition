import threading
from queue import Queue
import time




print_lock = threading.Lock()

def threadTest():
    # when this exits, the print_lock is released
    with print_lock:
        print(worker)

def threader():
  while True:
    # get the job from the front of the queue
    threadTest(q.get())
    q.task_done()

q = Queue()
for x in range(5):
    thread = threading.Thread(target = threader)
    # this ensures the thread will die when the main thread dies
    # can set t.daemon to False if you want it to keep running
    t.daemon = True
    t.start()

for job in range(10):
    q.put(job)
#print_lock = threading.Lock()
#   

'''
t1 = threading.Thread(target = multi)
t2 = threading.Thread(target = multi)
t1.start()
t2.start()
t1.join()
t2.join()
'''