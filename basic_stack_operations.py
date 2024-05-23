# Creating a stack
stack = []

# Push operation
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after push operations:", stack)

# Pop operation
stack.pop()
print("Stack after pop operation:", stack)

# Peek operation
top_element = stack[-1]
print("Top element after pop operation:", top_element)

# IsEmpty operation
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)

# Size operation
stack_size = len(stack)
print("Current stack size:", stack_size)
