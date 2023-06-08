import threading
import time

mutex = threading.Lock()

def get_thread(thread_name):
    time.sleep(1)
    with mutex:
        print(thread_name)

threads = []
for i in range(5):
    thread = threading.Thread(target=get_thread, args=(f"{i + 1}",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("потоки выполнены.")
