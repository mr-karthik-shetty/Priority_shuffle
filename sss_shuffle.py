
# importing "collections" for deque operations
import collections
import math
import random
# initializing deque used to store incomplete nodes for level order creation
de = collections.deque()

class Node:
    #creation of node
    def __init__(self, data,height,visited):
        self.left = None
        self.right = None
        self.data = data
        self.height=height
        self.visited=False

#level order tree traversal
def printLevel(root,tree_height):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        prob=tree_height*(2**(queue[0].height-1))
        prob=1/prob
        print (queue[0].data,queue[0].height,prob)
        node = queue.pop(0)

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.data),

        # now recur on right child
        printInorder(root.right)

#level order tree creation
def insert(data,root,count):
    count+=1
    height=math.ceil(math.log2(count+1))
    node=Node(data,height,False)
    if root==None:
        root=node
    elif (de[0].left==None):
        de[0].left=node
    else:
        de[0].right=node
        height+=1
        de.popleft()
    de.append(node)
    return root,count

def shuffle(root,tree_height):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)
    thresh=random.random()
    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        prob=tree_height*(2**(queue[0].height-1))
        prob=1/prob
        print(thresh,prob)
        if(thresh<prob and queue[0].visited==False):
            print (queue[0].data,prob)
            return
        else:
            thresh-=prob
        node = queue.pop(0)

        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

root=None
#stores number of nodes
count=0
for i in range(1,8):
    root,count=insert(i,root,count)

tree_height=math.ceil(math.log2(count+1))
leaves=int((count+1)/2)

#print("Level order traversal")
#printLevel(root,tree_height)
#print("-----")
#printInorder(root)
#print("-----")
#print("Queue contents(Incomplete nodes)")
#for i in de:
#    print(i.data)
#print("Height of tree-",tree_height)
#print("Leaves-",leaves)
shuffle(root,tree_height)
