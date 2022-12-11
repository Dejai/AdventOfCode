from collections import deque
import sys

class Monkey:

    def __init__(self, monkeyDetails):


        self.Name = None
        self.Items = deque()
        self.NumItemsInspected = 0

        # Attributes for operation
        self.Operation = ""

        # Attributes for Testing an item
        self.Divisible = 0
        self.isTrue = None
        self.isFalse = None

        # Setup the monkey details
        self.setupMonkey(monkeyDetails)

    def __repr__(self):
        return self.Name

    # Process the lines & setup this monkey
    def setupMonkey(self, details):
        lines = details.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("Monkey "):
                self.Name = line.replace(":","").split(" ")[1]
            elif line.startswith("Starting items: "):
                itemLine = line.split(":")[1].strip()
                items = [ int(x) for x in itemLine.split(", ")]
                self.Items = deque(items)
            elif line.startswith("Operation: "):
                self.Operation = line.split(" = ")[1]
            elif line.startswith("Test: "):
                self.Divisible = int(line.split(" by ")[1])
            elif line.startswith("If true: "):
                self.isTrue = line.split(" monkey ")[1]
            elif line.startswith("If false: "):
                self.isFalse = line.split(" monkey ")[1]

    # Add an item to the monkey's 
    def addItem(self, item):
        self.Items.append(item)

    # Run operation to multiply the worry
    def runWorryOperation(self, value):
        equation = self.Operation.replace("old", str(value))
        return eval(equation)

    # Determine which monkey is next
    def TestWorry(self,value):
        if value % self.Divisible == 0:
            return self.isTrue
        else:
            return self.isFalse

    # Inspect an item
    def inspectItem(self, divideFactor=None):
        
        if len(self.Items) == 0:
            return None,None
        
        item = self.Items.popleft()
        worryVal = self.runWorryOperation(item)
        reliefVal = worryVal % divideFactor if divideFactor is not None else worryVal // 3
        nextMonkey = self.TestWorry(reliefVal)

        self.NumItemsInspected += 1

        return nextMonkey,reliefVal