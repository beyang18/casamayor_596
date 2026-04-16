#Kent Gabriel Ongga - CCS 1301 SC: 526
print("--- STACK ---")

class stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


s = stack()
s.push(10)
s.push(20)
s.push(30)

print("Pushing:", s.items)
print("Stack:", s.items)
print("Popped element:", s.pop())
print("Top element:", s.peek())
print("Stack after pop:", s.display())