import os
import sys

# Create (or get?) directory
def getDirectory(day):
    
    dirPath = "./{0}".format(day)
    isNew = True
    
    dirExists = os.path.isdir(dirPath)
    if(not dirExists):
        print("Creaing new directory = %s" % dirPath)
        os.mkdir(dirPath )    
    else:
        print("Folder already exists.")
        isNew = False

    return dirPath,isNew

# Copy a template file to destination path.
def copyTemplateFile(fileName, destPath):

    templatefilePath = "./template/{0}".format(fileName)
    destFilepath = "{0}/{1}".format(destPath,fileName)

    print("Copying {0} to {1}".format(templatefilePath, destFilepath))

    templateFile = open(templatefilePath, "r+") # open file
    templateContent = templateFile.read() # read full content
    templateFile.close()

    newFile = open(destFilepath, "w+")
    newFile.write(templateContent)
    newFile.close()



#########################################################################################
# MAIN
#########################################################################################

args = sys.argv
day = args[1] if len(args) > 1 else ""

# If no day provided, end script
if day == "":
    print("No day specified")
    exit

# If day provided, then copy all template files
if day != "":

    # The new directory
   dirPath,isNew = getDirectory(day)
   if isNew:
    copyTemplateFile("run.py",dirPath)
    copyTemplateFile("helper.py", dirPath)
    copyTemplateFile("example.txt", dirPath)
    copyTemplateFile("input.txt", dirPath)