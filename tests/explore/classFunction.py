import threading
import time

def func_thread(j):
    for i in range(100):
        print(f"Thread {j} - iter: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=func_thread, args=(1, ))
thread2 = threading.Thread(target=func_thread, args=(2, ))

thread1.start()
thread2.start()