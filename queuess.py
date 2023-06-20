queue=[]

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print("Initial queue is \n",queue)

print("\n")
print("Element is dequeued from list")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("final queue",queue)