import os
import sys

args = sys.argv
dir = args[1] if len(args) > 1 else ""

if dir != "":

    # The new directory
    dirPath = format("./%s" % dir)
    dirExists = os.path.isdir(dirPath)


    print(dirExists)

    if(not dirExists):
        print("Creaing new directory = %s" % dirPath)
        os.mkdir(dirPath )    
    else:
        print("Folder already exists.")



    # Copy template
    scriptPath = format("%s/script.py" % (dirPath))
    scriptExists = os.path.isfile(scriptPath)

    if(not scriptExists):
        print("Copying template file")

        templateFile = open("./common/template.py", "r+") # open file
        templateContent = templateFile.read() # read full content
        templateFile.close()

        newFile = open(scriptPath, "w+")
        newFile.write(templateContent)
        newFile.close()


        print("Adding empty example and input files")
         # Write empty example and input files
        exampleTxt = format("%s/example.txt" % dirPath)
        inputTxt = format("%s/input.txt" % dirPath)

        open(exampleTxt, "w")
        open(inputTxt, "w")

    else:
        print("Script file exists")

    
else:
    print("No day specified")

