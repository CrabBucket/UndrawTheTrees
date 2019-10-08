nodes = []
class Node:
    
    def __init__(self, y, x, name):
        self.self = self
        self.y = y
        self.x = x
        self.children = []
        self.name = name
        nodes.append(self)

    def printchildren(self,child):
        print('(',end="")
        print(child.name,end="")
        for child in child.children:
            child.printchildren(child)
        print(')',end="")

inputCount = int(input())

def getTreeInput():
    currentInput = ""
    values = []
    while currentInput != "#":
        currentInput = input()
        values.append(currentInput)
    
    return values

# def getName(tree):
#     print(tree)
#     for x in range(0,len(tree),3):
#         b = tree[x].split(" ")
#         b = [x for x in b if x != ""]
#         print(b)


def getChildren(y,x,tree):
    start = 0
    end = 0
    children = []
    try:
        if tree[y+1][x] == "|":
            print('has children')
            
            offset = 0
            print('here')
            try:
                while (tree[y+2][x-offset] == "-"):
                    print('here')
                    start = x - offset
                    offset += 1
            except IndexError:
                start = 0
            
            offset = 0
            '''
            This is the broken area
            HERE IT IS THOMAS
            '''
            while (tree[y+2][x+offset] == "-" and x + offset < len(tree)):
                end = x + offset
                offset += 1
            for g in range(start,end+1):
                if tree[y+3][g] != " ":
                    print('got here')
                    children.append(Node(y+3,g,tree[y+3][g]))
            print("Start : %d, end : %d"%(start,end))
    except IndexError:
        3
    return children

for q in range(inputCount):
    tree = getTreeInput()
    for y in range(len(tree))[0::3]:
        # print(y)
        for x in range(len(tree[y])):
            if tree[y][x] != " ":
                node1 = Node(y,x,tree[y][x])
                # print('y : %d, x : %d'%(node1.y,node1.x))
                kids = getChildren(node1.y,node1.x,tree)
                for kid in kids:
                    # node1.children.append(kid)
                    print("KIDS NAME : ",kid.name)
