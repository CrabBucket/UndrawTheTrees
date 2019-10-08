class Node:
    def __init__(self, position, name, children=[]):
        self.self = self
        self.position = position
        self.children = children
        self.name = name

inputCount = int(input())
for x in range(inputCount):
    currentInput = ""
    values = []
    while currentInput != "#":
        currentInput = input()
        values.append(currentInput)
    
    print(values)