from threading import Thread
from time import sleep

def first_function():
    for i in range(5):
        print('first_function')
        sleep(1)

def second_function():
    for i in range(5):
        print('second_function')
        sleep(1)


t = Thread(target=first_function)
t.start()

t2 = Thread(target=second_function)
t2.start()
