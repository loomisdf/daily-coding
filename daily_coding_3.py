# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into 
# a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(rootNode):
    str = rootNode.val
    prevNode = node.left
    while prevNode != None:
        str = prevNode.val + " " + str
        prevNode = prevNode.left

    nextNode = rootNode.right
    while nextNode != None:
        str = str + " " + nextNode.val
        nextNode = nextNode.right

    return str

def deserialize(str):
    strList = str.split()
    currentNode = Node(strList.pop(0))
    rootNode = Node('root')

    # Deserialize up to the root
    while True:
        val = strList.pop(0)
        if val == "root":
            rootNode.left = currentNode
            currentNode = rootNode
            break
        else:
            newNode = Node(val, left=currentNode)
            currentNode = newNode

    # Deserialize from the root to the end
    while len(strList) != 0:
        val = strList.pop(0)
        newNode = Node(val)
        currentNode.right = newNode
        currentNode = newNode

    return rootNode
    
node = Node('root', Node('left', Node('left.left')), Node('right'))

# print(deserialize(serialize(node)).left.left.val == "left.left")
node = deserialize("butts salad pineapple root potatoes cauliflower")
print(serialize(node))