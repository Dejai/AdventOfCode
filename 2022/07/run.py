
import helper
from classes import Tree, Directory, File

'''
***************************************************************
    Input
***************************************************************
'''

exampleInput = helper.getFileContentAsList("./example.txt")
realInput = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions
***************************************************************
'''

# Get the directory name
def getDirectoryName(val):
    return val.replace("$ ","").replace("cd ","").replace("dir ","")

# Get the tree 
def getTree(inputList):
    tree = Tree()

    for line in inputList:

        if "$ ls" in line:
            continue
        
        dirName = getDirectoryName(line)

        if "cd /" in line:
            # print("Setting root")
            tree.setCurrentDirectory( Directory(dirName) )
            print(str(tree.currentDirectory))

        elif "cd " in line:
            if ".." in line:
                # print("Going back up one: ")
                tree.setCurrentDirectory( tree.currentDirectory.parentDirectory )
            else:
                # print("Going down to {0}".format(dirName))
                subDirectory = tree.currentDirectory.getDirectory(dirName)
                tree.setCurrentDirectory( subDirectory )

        elif "dir " in line:
            # print("Adding a contained directory: " + dirName)
            tree.currentDirectory.addDirectory(dirName, Directory(dirName, tree.currentDirectory))

        else:
            # print("Adding file {0} in directory = {1}".format(line, tree.currentDirectory))
            tree.currentDirectory.addFile( File(line) )

    return tree


'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
tree = getTree(inputList)
sizes = [ x[1] for x in tree.getDirectoriesBySize() if x[1] <= 100000]
a1 = sum(sizes)
helper.printAnswer(1,a1)


# Print answer for Part 2
totalSpace = 70000000
neededSpace = 30000000
usedSpace = tree.rootDirectory.getSize()
unusedSpace = totalSpace - usedSpace
threshold = neededSpace - unusedSpace
sizes = tree.getDirectoriesBySize()
candidates = [x[1] for x in sizes[1:] if x[1] >= threshold]
candidates.sort()
a2 = candidates[0]
helper.printAnswer(2, a2)