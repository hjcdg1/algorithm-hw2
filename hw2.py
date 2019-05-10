# Definitions of Node
class Node :
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = None
        self.size = 1

# Definitions of Tree
class Tree :
    RED = 1
    BLACK = 0
    nil = Node(None)
    nil.color = BLACK
    nil.size = 0

    def __init__(self, root):
        self.root = root

    def print_inorder(self, x):
        if (x == self.nil) :
            return
        self.print_inorder(x.left)
        print(x.key, ("RED" if x.color == Tree.RED else "BLACK"), x.size, "child", x.left.key, x.right.key)
        self.print_inorder(x.right)

# Function for left rotation
def left_rotate(x):
    y = x.right
    y.size = x.size
    x.right = y.left
    if (y.left != T.nil) :
        y.left.p = x
    y.p = x.p
    if (x.p == T.nil) :
        T.root = y
    else :
        if (x == x.p.left) :
            x.p.left = y
        else :
            x.p.right = y
    y.left = x
    x.p = y
    x.size = x.left.size + x.right.size + 1

# Function for right rotation
def right_rotate(y):
    x = y.left
    x.size = y.size
    y.left = x.right
    if (x.right != T.nil) :
        x.right.p = y
    x.p = y.p
    if (y.p == T.nil) :
        T.root = x
    else :
        if (y == y.p.left) :
            y.p.left = x
        else :
            y.p.right = x
    x.right = y
    y.p = x
    y.size = y.left.size + y.right.size + 1

# Function for searching
def os_search(key):
    x = T.root
    while (x != T.nil):
        if (key < x.key):
            x = x.left
        elif (key > x.key):
            x = x.right
        else:
            return x
    return None

# Function for updating size information
def update_size(x):
    if (x == T.nil) :
        return
    x.size = x.left.size + x.right.size + 1
    update_size(x.p)

# Function for initializing RB tree
def init():
    global T
    global cnt
    T = Tree(Tree.nil)

# Function for insertion
def os_insert(key):
    z = Node(key)
    y = T.nil
    x = T.root
    while (x != T.nil) :
        y = x
        if (z.key < x.key) :
            x = x.left
        elif (z.key > x.key) :
            x = x.right
        else :
            return 0
    z.p = y
    if (y == T.nil) :
        T.root = z
    else :
        if (z.key < y.key) :
            y.left = z
        else :
            y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = T.RED
    update_size(z.p)
    os_insert_fixup(z)
    return key

# Function for insertion fixup
def os_insert_fixup(z):
    while (z.p.color == T.RED) :
        if (z.p == z.p.p.left) :
            y = z.p.p.right
            if (y.color == T.RED) :
                z.p.color = T.BLACK
                y.color = T.BLACK
                z.p.p.color = T.RED
                z = z.p.p
            else :
                if (z == z.p.right) :
                    z = z.p
                    left_rotate(z)
                z.p.color = T.BLACK
                z.p.p.color = T.RED
                right_rotate(z.p.p)
        else :
            y = z.p.p.left
            if (y.color == T.RED) :
                z.p.color = T.BLACK
                y.color = T.BLACK
                z.p.p.color = T.RED
                z = z.p.p
            else :
                if (z == z.p.left) :
                    z = z.p
                    right_rotate(z)
                z.p.color = T.BLACK
                z.p.p.color = T.RED
                left_rotate(z.p.p)
    T.root.color = T.BLACK

# Function for transplanting one node to other node
def transplant(u, v):
    if (u.p == T.nil) :
        T.root = v
    else :
        if (u == u.p.left) :
            u.p.left = v
        else :
            u.p.right = v
    v.p = u.p

# Function for finding a node with minimum value
def minimum(x):
    if (x.left != T.nil) :
        return minimum(x.left)
    else :
        return x

# Function for deletion
def os_delete(key):
    z = os_search(key)
    if (z == None) :
        return 0
    y = z
    y_original_color = y.color
    if (z.left == T.nil) :
        x = z.right
        transplant(z, z.right)
    elif (z.right == T.nil) :
        x = z.left
        transplant(z, z.left)
    else :
        y = minimum(z.right)
        y_original_color = y.color
        x = y.right
        if (y.p == z) :
            x.p = y # Why necessary?
        else :
            transplant(y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    update_size(x.p)
    if (y_original_color == T.BLACK) :
        os_delete_fixup(x)
    return key

# Function for deletion fixup
def os_delete_fixup(x):
    while (x != T.root and x.color == T.BLACK) :
        if (x == x.p.left) :
            w = x.p.right
            if (w.color == T.RED) :
                w.color = T.BLACK
                x.p.color = T.RED
                left_rotate(x.p)
                w = x.p.right
            if (w.left.color == T.BLACK and w.right.color == T.BLACK) :
                w.color = T.RED
                x = x.p
            else :
                if (w.right.color == T.BLACK) :
                    w.left.color = T.BLACK
                    w.color = T.RED
                    right_rotate(w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = T.BLACK
                w.right.color = T.BLACK
                left_rotate(x.p)
                x = T.root
        else :
            w = x.p.left
            if (w.color == T.RED) :
                w.color = T.BLACK
                x.p.color = T.RED
                right_rotate(x.p)
                w = x.p.left
            if (w.right.color == T.BLACK and w.left.color == T.BLACK) :
                w.color = T.RED
                x = x.p
            else :
                if (w.left.color == T.BLACK) :
                    w.right.color = T.BLACK
                    w.color = T.RED
                    left_rotate(w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = T.BLACK
                w.left.color = T.BLACK
                right_rotate(x.p)
                x = T.root
    x.color = T.BLACK

# Function for selection
def os_select(i):
    if (T.root.size < i) :
        return 0
    else :
        return os_select_helper(T.root, i)

# Helper function for selection
def os_select_helper(x, i):
    r = x.left.size + 1
    if (i == r) :
        return x.key
    elif (i < r) :
        return os_select_helper(x.left, i)
    else :
        return os_select_helper(x.right, i-r)

# Function for finding rank
def os_rank(key):
    x = os_search(key)
    if (x == None) :
        return 0
    else :
        return os_rank_helper(x)

# Helper function for finding rank
def os_rank_helper(x):
    r = x.left.size + 1
    y = x
    while (y != T.root) :
        if (y == y.p.right) :
            r = y.p.left.size + 1 + r
        y = y.p
    return r

# Checker program
def check(opt_seq, val_seq, out_seq):
    ans_seq = []
    check_val = 0
    for opt, val, out in zip(opt_seq, val_seq, out_seq):
        if opt == 0:
            if val in ans_seq:
                check_val = 0
            else:
                ans_seq.append(val)
                check_val = val
        elif opt == 1:
            if val in ans_seq:
                ans_seq.remove(val)
                check_val = val
            else:
                check_val = 0
        elif opt == 2:
            ans_seq.sort()
            if (val <= len(ans_seq)):
                check_val = ans_seq[val-1]
            else:
                check_val = 0
        else:
            ans_seq.sort()
            if val in ans_seq:
                for v, i in zip(ans_seq, range(len(ans_seq))):
                    if v == val:
                        check_val = i + 1
            else:
                check_val = 0
        if (check_val != out):
            return False
    return True
