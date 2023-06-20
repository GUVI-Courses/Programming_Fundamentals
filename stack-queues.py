# using collections stack
'''
from collections import deque

stack=deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print(stack)

print("pop from stack")

print(stack.pop())
print(stack.pop())
print(stack.pop())

'''
'''
from queue import LifoQueue

stack=LifoQueue(maxsize=5)

print(stack.qsize())

# pushing
print("inserting items into the stacks")
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
# stack.put(6)

print(stack)
print(stack.full())
print(stack.qsize())
print()
print(stack.get())
print(stack.get())


print()
print(stack.full())
print(stack.qsize())

print()
print(stack.get())
print(stack.get())
print(stack.get())

print()
print(stack.full())
print(stack.qsize())
print(stack.empty())

'''

# queues
'''
from collections import deque

queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

print("deque")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

'''



from queue import Queue
queue=Queue(maxsize=5)
print("insert the elements in queues\n")
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
print(queue)
print(queue.qsize())
print(queue.full())

print("removing items in queues")
print(queue.get())
print(queue.get())
print(queue.get())