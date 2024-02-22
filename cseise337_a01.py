"""
Ryan Chen
ryachen
113200236
"""

# Problem 1 – Chaotic Strings
def is_chaotic(s):
    hmap = {} # char -> count
    for c in s:
        if c in hmap:
            hmap[c] += 1
        else:
            hmap[c] = 1
    counts = set()
    for v in hmap.values():
        if v in counts: # not chaotic
            return 'ELMA'
        counts.add(v)
    # chaotic
    return 'TOHRU'

# Problem 2 – Balanced Brackets
def is_balanced(s):
    left = {'(','{','['}
    right = {')','}',']'}
    r_to_l = {')':'(','}':'{',']':'['}
    stack = []

    for c in s:
        if c in left:
            stack.append(c)
        else: # right bracket
            if len(stack) == 0:
                return False # too many right
            top = stack.pop()
            if top != r_to_l[c]:
                return False
    return len(stack) == 0 # too many left

# Problem 3 – Functional Programming
def winning_function(l, f1, f2):
    if sum(list(map(f1,l))) > sum(list(map(f2,l))):
        return f1.__name__
    elif sum(list(map(f1,l))) < sum(list(map(f2,l))):
        return f2.__name__
    else:
        return 'TIE'

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

# Problem 4 – Representing Filesystems
class FS_Item:
    def __init__(self,name):
        self.name = name
class Folder(FS_Item):
    def __init__(self,name,items):
        super().__init__(name)
        self.items = items
    def add_item(self,item):
        self.items.append(item)
    def __str__(self):
        res = "Folder: "
        for i in self.items:
            res += str(i)
        res += "\n"
        return res

class File(FS_Item):
    def __init__(self,name,size):
        super().__init__(name)
        self.size = size
    def __str__(self):
        return self.name

def load_fs(ls_output):
    topLevelFolder = None
    hmap = {} # folder path -> files

    # tree structure
    with open(ls_output,"r") as inFile:
        all_lines = inFile.readlines()
        # parse top level folder
        topLevelFolder = Folder(".",[])

        for line in all_lines:
            print(line)
    # procedure BFS(root):
    # create an empty queue
    # enqueue root into the queue
    #
    # while the queue is not empty:
    #     current_node = dequeue from the queue
    #     process current_node's data
    #
    #     for each child in current_node's children:
    #         enqueue child into the queue

    return topLevelFolder

# The argument passed to ls_output is the name of a file which contains
# the output of the system command ls -lR.
#
# The function should read this file and use it to construct an internal representation of the part of
# the file system recorded in the file named by ls_output. For each directory, create a Folder
# object with the same name. Add each directory and document contained in that directory as a
# Folder or File element of its items list. For each File element make sure to set its name
# and filesize when adding it to the items list of the Folder that contains it.
# When done the function should return a reference to the top-level Folder item (the one
# corresponding to the top-level directory in ls_output.


# Problem 5 – Decoding
def decode(ct):
    letter_to_lex_pos = {
    'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,
    'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,
    'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,
    'v': 21,'w': 22,'x': 23,'y': 24,'z': 25
    }
    res = ""
    i = 0
    lower_letter_ascii_range = range(ord('a'),ord('z')+1)
    for c in ct:
        if c == " ":
            res += c
        elif i == 0:
            lex_pos = letter_to_lex_pos[c]
            ordVal = (lex_pos - 59) % 26
            while ordVal not in lower_letter_ascii_range:
                ordVal += 26
            res += chr(ordVal)
        else:
            nminusonesumord = 0
            for c_1 in res:
                if c_1 == " ":
                    continue
                nminusonesumord += ord(c_1)
            lex_pos = letter_to_lex_pos[c]
            ordVal = (lex_pos - nminusonesumord) % 26
            while ordVal not in lower_letter_ascii_range:
                ordVal += 26
            res += chr(ordVal)
        i+= 1
    return res

def main():
    print(decode("sidnkw"))
    print(decode("i uz zwgd jqf"))
    print(decode("tmny zk d pmxj"))




if __name__ == "__main__":
    main()
