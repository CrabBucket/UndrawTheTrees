class Node:
    def printchildren(node):
        print('(')
        print(node.name)
        for child in node.children:
            printchildren(child)
        print(')')
    def __init__(self, position, name, children=[],start,end):
        self.self = self
        self.position = position
        self.children = children
        self.name = name
        self.startpos = start
        self.end = end

inputCount = int(input())
for x in range(inputCount):
    currentInput = ""
    values = []
    while currentInput != "#":
        currentInput = input()
        values.append(currentInput)
    
    print(values)