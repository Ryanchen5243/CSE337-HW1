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
    indentLevel = 0
    def __init__(self,name,items):
        super().__init__(name)
        self.items = items
    def add_item(self,item):
        self.items.append(item)
    def __str__(self):
        res = f"Folder: {self.name}\n"
        Folder.indentLevel += 1
        for i in self.items:
            if type(i) == Folder:
                res += str("---" * Folder.indentLevel) + " " + i.__str__() + "\n"
            else:
                res += str("---" * Folder.indentLevel) + " " + str(i) + "\n"
        Folder.indentLevel -= 1
        return res

class File(FS_Item):
    def __init__(self,name,size):
        super().__init__(name)
        self.size = size
    def __str__(self):
        return f"{self.name} {self.size} bytes"

def load_fs(ls_output):
    topLevelFolder = None
    # tree structure
    with open(ls_output,"r") as inFile:
        all_lines = inFile.readlines()
        # parse top level folder
        topLevelFolder = Folder(".",[])
        currFolder = topLevelFolder

        for line in all_lines:
            line = line.split()
            # folder start
            if len(line) == 1 and line[0][0] == ".":
                path = line[0].split("/")
                # remove the colon from last
                path[-1] = path[-1][0:len(path[-1])-1]
                # print("The path is -------->",path)
                # update currFolder to process subsequent
                # files/folders in else clause
                if len(topLevelFolder.items) == 0:
                    # top level case
                    pass
                else:
                    # find current folder using path
                    # print("the path is ")
                    # print(path)
                    # reset pointer
                    currFolder = topLevelFolder

                    path_ind = 1 # iterate through path
                    while path_ind < len(path):
                        # print(path_ind)
                        # update currFolder at current level
                        for item in currFolder.items:
                            # print("detecting ",item)
                            if type(item) == Folder:
                                if item.name == str(path[path_ind]):
                                    # print("found folder",item.name)
                                    currFolder = item
                                    break
                        path_ind += 1
                    # print("assigned current folder to ",currFolder.name)
            elif len(line) == 0 or len(line) == 2 and line[0] == "total":
                continue
            else:
                if line[0][0] == "d": # folder detected
                    currFolder.add_item(Folder(str(line[-1]),[]))
                elif line[0][0] == "-": # file detected
                    currFolder.add_item(File(str(line[-1]),int(line[4])))

    return topLevelFolder

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
    pass



if __name__ == "__main__":
    main()
