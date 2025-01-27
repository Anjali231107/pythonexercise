# import threading
# import time

# def print_numbers():
#     for i in range(i):
#         print(f"thread 1 : {1}")
#         time.sleep(1)

# def print_letters():
#     for letter in ["a","b","c"]:
#         print(f"thread 2: {letter}")
#         time.sleep(1)

#         thread1 = threading.Thread(target=print_numbers)
#         thread2 = threading.Thread(target=print_letters)

#         thread1.start()
#         thread2.start()

#         thread1.join()
#         thread2.join()

#         print("both threads have finished execution.")

import threading
import time

# Define a function for the thread
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2: {letter}")
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")
