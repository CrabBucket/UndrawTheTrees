nodes = []
class Node:

    def __init__(self, y, x, name,hasParent):
        self.self = self
        self.y = y
        self.start = -1
        self.end = -1
        self.hasParent = hasParent
        self.x = x
        self.children = []
        self.shouldOpen = True
        self.name = name
        nodes.append(self)
    def setRange(self,start,end):
        self.start = start
        self.end = end
    def printchildren(self,child):
        if(self.shouldOpen):
            print('(',end='')
        print(child.name,end="")
        count = 0;
        testbool = False
        for child in child.children:
            testbool = True
            if(count == 0):
                child.shouldOpen=True;
            else:
                child.shouldOpen=False;
            count = count + 1
            child.printchildren(child)
        if not testbool:
            print('(',end='')

        print(')',end='')

shoulOpen=True
inputCount = int(input())
def getStart(string,index):
    #print("stuck")
    while (string[index] == '-'):
        index -= 1
        if (index == -1):
            index += 1
            break
    return index
def getEnd(string,start):
    index = start
    #print("stuck")
    while(string[index]=='-'):
        index+=1
        if(index==len(string)):
            index-=1
            break
    return index
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


def getChildren(node,tree):
    start = 0
    end = 0
    y = node.y
    x = node.x
    children = []
    try:
        if tree[y+1][x] == "|":
            #print('has children')
            node.start = getStart(tree[y+2],x)
            offset = 0
            #print('here')
            # try:
            #     # while (tree[y+2][x-offset] == "-"):
            #     #     print('here')
            #     #     start = x - offset
            #     #     offset += 1
            # except IndexError:
            #     start = 0

            offset = 0
            '''
            This is the broken area
            HERE IT IS THOMAS
            '''
            node.end = getEnd(tree[y+2],x)
            # while (tree[y+2][x+offset] == "-" and x + offset < len(tree)):
            #     end = x + offset
            #     offset += 1
            for g in range(node.start,node.end+1):
                if tree[y+3][g] != " " and tree[y+3][g] != "#" and tree[y+3][g] != "-" and tree[y+3][g] != "|":
                    #print('got here')

                    child = Node(y + 3, g, tree[y + 3][g],True)
                    getChildren(child,tree)
                    node.children.append(child)
            #print("Start : %d, end : %d"%(start,end))
    except IndexError:
        3




for q in range(inputCount):
    tree = getTreeInput()

    nodes = []
    y = 0
    for x in range(len(tree[y])):
        if tree[y][x] != " " and tree[y][x] != '#' and tree[y][x]!='|' and tree[y][x]!='-':
            node1 = Node(y,x,tree[y][x],False)
            # print('y : %d, x : %d'%(node1.y,node1.x))
            getChildren(node1,tree)
    try:
        nodes[0].printchildren(nodes[0])
        print(')')
    except IndexError:
        print('()')




# for q in range(inputCount):
#     tree = getTreeInput()
#     nodes = []
#     for y in range(len(tree))[0::3]:
#         # print(y)
#         for x in range(len(tree[y])):
#             if tree[y][x] != " ":
#                 node1 = Node(y,x,tree[y][x])
#                 # print('y : %d, x : %d'%(node1.y,node1.x))
#                 kids = getChildren(node1.y,node1.x,tree)
#                 node1.children = kids
#                 nodes.append(node1)

