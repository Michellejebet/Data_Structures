class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

    def peek(self):
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()


a = input("Enter your word: ")
s = Stack()
for i in a:
    s.push(i)

new_word = ""
while not s.isEmpty():
    new_word += s.pop()

if a == new_word:
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")
