
import helper

'''
***************************************************************
    Input
***************************************************************
'''

exampleInput = helper.getFileContentAsList("./example.txt")
realInput = helper.getFileContentAsList("./input.txt")

'''
***************************************************************
    Functions & Class
***************************************************************
'''
class Register:

    def __init__(self):
        self.X = 1
        self.Cycle = 0

        # Checking for signal strengths
        self.signalStrengthCheck = 20
        self.signalStrengths = []

        # 3 pixel position of the sprite
        self.spritePosition = [0,1,2] 

        # The CRT for the screen
        self.CRT = ["." for idex in range(0,240) ]

    def runInstruction(self, instruction):

        if "noop" in instruction:
            self.Cycle += 1
            self.setCRTPixel()
            self.setSignalStrength()

        if "addx" in instruction:
            for idx in range(0,2):
                self.Cycle += 1
                self.setCRTPixel()
                self.setSignalStrength()

            number = int(instruction.split(" ")[1])
            self.X += number
            # Increase sprite position
            self.setSpritePosition(number)

    # Set the signal strength
    def setSignalStrength(self):

        if self.Cycle == self.signalStrengthCheck:
            strength = self.Cycle * self.X
            self.signalStrengths.append(strength)
            self.signalStrengthCheck += 40

    # Set the relative sprite position
    def setSpritePosition(self, number):
        self.spritePosition[0] += number
        self.spritePosition[1] += number
        self.spritePosition[2] += number
    
    # Set the CRT Pixel "#";
    def setCRTPixel(self):

        cycleIndex = (self.Cycle-1)
        crtIndex = (self.Cycle-1) % 40
        index = self.Cycle-1
        if(cycleIndex in self.spritePosition or crtIndex in self.spritePosition):
            self.CRT[cycleIndex] = "#"

    # Print the CR
    def printCRT(self):
        output = ""
        count = 0
        for idx in range(0,240):
            pixel = self.CRT[idx]
            output += pixel
            count += 1
            if count == 40:
                count = 0
                output += "\n"
        print(output)  

'''
***************************************************************
    Run
***************************************************************
'''
# What are we working with; Change this variable to use the real input when ready
inputList = realInput
# print(inputList)

# Print answer for Part 1
register = Register()
for inst in inputList:
    register.runInstruction(inst)
a1 = sum(register.signalStrengths)
helper.printAnswer(1,a1)

# Print answer for Part 2
helper.printAnswer(2, "Part 2 Image")
register.printCRT()