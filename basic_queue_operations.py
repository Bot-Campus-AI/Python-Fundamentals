# Creating a queue
queue = []

# Enqueue operation
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueue operations:", queue)

# Dequeue operation
queue.pop(0)
print("Queue after dequeue operation:", queue)

# Peek operation
first_element = queue[0]
print("First element after dequeue operation:", first_element)

# IsEmpty operation
is_empty = len(queue) == 0
print("Is the queue empty?", is_empty)

# Size operation
queue_size = len(queue)
print("Current queue size:", queue_size)
