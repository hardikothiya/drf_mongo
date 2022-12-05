import threading
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done Sleeping')


t1 = threading.Thread(target=do_something, args=[2])
t2 = threading.Thread(target=do_something, args=[3])
t1.start()
t2.start()
t1.join()
t2.join()
finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
