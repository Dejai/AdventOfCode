from collections import deque

class Tree:
    def __init__(self):
        self.currentLevel = 0
        self.rootDirectory = None
        self.currentDirectory = None
    
    def setCurrentDirectory(self, directory):
        self.currentDirectory = directory

        if(self.rootDirectory is None):
            self.rootDirectory = directory

    def getDirectoriesBySize(self):
        matchingDirs = []

        directorySizePair = []

        dirsToCheck = deque()
        dirsToCheck.append(self.rootDirectory)

        while len(dirsToCheck) > 0:
            directory = dirsToCheck.pop()
            size = directory.getSize()

            directorySizePair.append( (directory, size) )
            
            for subdir in directory.directories.values():
                dirsToCheck.append(subdir)

        return directorySizePair

class Directory:
    def __init__(self, name, parentDirectory=None):
        self.name = name
        self.files = []
        self.parentDirectory = parentDirectory
        self.directories = {}

    def __repr__(self):
        return "Directory: " + str(self.name)

    def addFile(self, file):
        self.files.append(file)

    def addDirectory(self, name, directory):
        self.directories[name] = directory

    def getDirectory(self, name):
        directory = self
        if name in self.directories:
            directory = self.directories[name]
        return directory

    def changeDirectory(self, name):
        newDirectory = None
        if name in self.directories:
            newDirectory = self.directories[name]
        return newDirectory

    def getSize(self):
        fileSizes = sum([file.size for file in self.files])
        dirSizes = sum([x.getSize() for x in self.directories.values()])
        return fileSizes + dirSizes

class File:
    def __init__(self, fileDetails):
        details = fileDetails.split(" ")
        self.size = int(details[0])
        self.name = details[1]

    def __repr__(self):
        return "File: " + str(self.name)