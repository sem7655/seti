import time
import threading
def get_thread(thread_name):
    time.sleep (1)
    print (thread_name)
    threads = []
    for i in range (5):
        thread = threading.Thread (target=get_thread, args=(f"Thread {i + 1}",))
        threads.append (thread)
        thread.start ()
        for thread in threads:
            thread.join ()
