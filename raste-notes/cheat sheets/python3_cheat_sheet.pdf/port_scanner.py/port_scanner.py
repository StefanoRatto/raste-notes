import socket

import threading
from queue import Queue

target = "192.168.254.49"
queue = Queue()
open_ports = []

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

#print(port_scan(443))

# for port in range(1, 1024):
#     result = port_scan(port)
#    
#     if result:
#         print("Port " + format(port) + " is OPEN")
#     #else:
#     #    print("Port " + format(port) + " is CLOSED")

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port " + format(port) + " is OPEN")
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: " + format(open_ports))






