"""
Given a padlock with the numbers from 1 to 9 knowing that the lock combination
it is a sequence of numbers of n length. The first digit D of the combination is known. 
The next digit is calculated by making a movement in L similar to that of the Knight
in Chess.
"""
next_move = {1: [6,8], 
             2: [7,9], 
             3: [8,4], 
             4: [3,9], 
             6: [1,7], 
             7: [2,6], 
             8: [3,1], 
             9: [4,2] 
            }

"""
Given a current digit, return the possible next moves (in chess night L movement, from the 
next_move table above.
"""
def fnext(d):
    return(next_move[d])

"""
This class defines the Node object and its methods.  Each node corresponds to a digit in the 
possible lock combinations
"""

class newNode(): 

    def __init__(self, data): 
	    self.key = data 
	    self.left = None
	    self.right = None

    """
    This method walks the binary tree and returns an order list, by level, left-right of the 
    digits found for the initial parameters given (starting number, lock_combination length)
    """
    def levelOrderWalk(self, tnode):
        if tnode is None:
            return[]

        # start at the root of the tree
        qnodes = [tnode]
        qptr = 0
        while (tnode.left or tnode.right):
            qnodes.extend([qnodes[qptr].left, qnodes[qptr].right])
            qptr += 1
            tnode = qnodes[qptr]

        return [node.key for node in qnodes]

    """
    This method walks each branch of the tree, from tree root to leaf, and returns all the possible
    lock combinations.  For example:  ['2->7->2', '2->7->6', '2->9->4', '2->9->2']
                                2
                               / \ 
                              7   9
                             / \ / \
                            2  6 4  2
    """
    def getLockCombinations(self, troot):
        if troot is None: 
            return []
        if (troot.left == None and troot.right == None):
            return [str(troot.key)]
        
        # if left/right is None we will get an empty list anyway. 
        # Use list comprehensions and recursion. 
        return [str(troot.key) + '->'+ l for l in 
                self.getLockCombinations(troot.left) + self.getLockCombinations(troot.right)]


""" 
This function inserts a new node into a binary tree, in level-order traversal, left-right.
It walks the tree for a new digit and inserts where it finds an empty space, in that order.
"""
def insertNode(tnode, key):

    # start at the root of the tree
    q = [] 
    q.append(tnode)

    # Do level order node traversal until we find an empty space (L or R)
    while (len(q)): 
        tnode = q.pop(0)
        if (not tnode.left): 
            tnode.left = newNode(key)
            break
        else: 
            q.append(tnode.left) 

        if (not tnode.right): 
            tnode.right = newNode(key)
            break
        else: 
            q.append(tnode.right) 

"""
This function builds the digit sequence (not including the first one) to be inserted into a binary
tree.  The sequence corresponds to level-order, lef-right.  For example, for first_digit = 2
and key_length = 3 the sequence returned is [7, 9, 2, 6, 4, 2].  We don't include the first digit,
which is 2 (the root of the tree). 
"""
def buildDigitSequence(root, klength):
    dlist = [root]
    nparents = 2**(klength-1)
    for x in range(1, nparents):   
        dlist.extend(fnext(dlist[x-1]))
    return dlist[1:]

"""
Main program.  Ask the user for first digit and length of the lock combination. 
"""

if __name__ == '__main__':

    first_dig = int(input("Ingrese el primer digito: "))
    comb_length  = int(input("Ingrese longitud de la combinacion: "))

    comb_vals = buildDigitSequence(first_dig, comb_length) 

    troot = newNode(first_dig)

    for key in comb_vals:
        insertNode(troot, key)

    print("\nLevel-Order Digits (root->left->right): {}".format(troot.levelOrderWalk(troot)))
    lock_combinations = troot.getLockCombinations(troot)
    print("\nKeyLock Possible Combinations: {}\n {}\n".format(
        len(lock_combinations), lock_combinations)
        )


