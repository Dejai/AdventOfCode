import shared

'''
***************************************************************
    Input and Global variable
***************************************************************
'''

inputList = shared.getFileContentAsList("./input.txt")
DEBUG = False


'''
***************************************************************
    Functions
***************************************************************
'''
# Printing messages conditionally
def debug(msg):
    if DEBUG:
        print(msg)


# Get integer value of binary
def binToInteger(binaryString):
    return int(binaryString, 2)

# Convert given hex char to binary
def hexToBinary(inputValue):
    hexMap = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    binaryString = ""
    for char in inputValue:
        bin = hexMap[char] if char in hexMap else "UNKNOWN-" + char
        binaryString += bin
    return binaryString


# Parse the input to generate a set of operations
# Includes pertinent details about type, bits, and LTID (if applicable)
def parseInput(hexadecimal):
    binary = hexToBinary(hexadecimal)

    # Values to be returned
    operations = []
    versionSum = 0

    # Get all operations until none left to process
    while True:

        bitsProcessed = 0
        
        # If trailing 0s - we can end
        if "1" not in binary:
            break   

        # Get version and type
        version = binToInteger( binary[:3] )
        type = binToInteger( binary[3:6] )
        
        versionSum += version

        # Shift input & count bits processed
        binary = binary[6:]
        bitsProcessed += 6
        
        # Default values for operation
        value = None
        ltid = None
        ltidValue = None

        # Process a literal
        if type == 4:
            literalBin = ""
            while True:
                segment = binary[:5]  # get 5 bits (preceded by 1 or 0)
            
                literalBin += segment[1:] # don't include the prefix
                
                # Shift and update bits processed
                binary = binary[5:]
                bitsProcessed += 5
                # Stop if found last segment
                if(segment[0] == "0"):
                    value = binToInteger(literalBin)  # Set the value for this operation
                    break
        else:

            # Get the length type ID (ltid)
            ltid = binary[0]

            # Shift and update bits processed
            binary = binary[1:]
            bitsProcessed += 1


            if (ltid == "0"):
                totalLength = binToInteger ( binary[:15] )
                ltidValue = totalLength

                # Shift and updated bits processed
                binary = binary[15:]
                bitsProcessed += 15

            elif (ltid == "1"):
                totalSubpackets = binToInteger( binary[:11] )
                ltidValue = totalSubpackets

                # Shift and updated bits processed
                binary = binary[11:]
                bitsProcessed += 11

        # Add the operation to the set of operations
        operation = (type,value,bitsProcessed, ltid,ltidValue)
        operations.append(operation)

    return operations, versionSum


# Process the operations
def processOperations(operations):

    storage = []

    # Keep processing until answer found
    while True:

        if len(operations) == 0:
            break

        # Get the pieces of info from the operations
        type,val,bits,ltid,ltidval = operations.pop()

        if type == 4:
            storage.insert(0, (val,bits))

        else:

            # Get the set of values to be processed by this operator
            pairs = []
            count = 0
            while count < ltidval:
                v,b = storage.pop(0)
                count += b if ltid == "0" else 1  # Updating count: if bit length, add the bits; Otherwise, just add 1 (for packet count)
                pairs.append( (v,b) )

            #print(pairs)

            # Get the values and their bit counts separately.
            values = [ v for v,b in pairs]

            # Set the default answer to be added next
            ans = -1
            newBits = bits
            newBits += sum( [ b for v,b in pairs ] )  # Get the total bits for the values to be procesed

            if type == 0:  # addition
                debug(format("Adding = %s" % str(values)))
                ans = sum(values)
                
            elif type == 1:  # multiplication
                debug(format("Multiplying = %s" % str(values)))
                product = 1
                for x in values:
                    product *= x
                ans = product

            elif type == 2:  # minimum
                debug(format("Minimum of = %s" % str(values)))
                ans= min(values)

            elif type == 3:  # maximum
                debug(format("Maximum of = %s" % str(values)))
                ans= max(values)

            elif type == 5:  # Greater than?
                debug(format("Compare(>) = %s" % str(values)))
                ans = 1 if values[0] > values[1] else 0

            elif type == 6:  # Less than
                debug(format("Compare(<) = %s" % str(values)))
                ans = 1 if values[0] < values[1] else 0

            elif type == 7:  # Equals
                debug(format("Compare(=) = %s" % str(values)))
                ans = 1 if values[0] == values[1] else 0

            
            # Add answer back to storage
            if(ans == -1):
                print("ERROR!")
                print(storage)
                break
            storage.insert(0, (ans,newBits))

    # Return final answer
    return storage


'''
***************************************************************
    Run
***************************************************************
'''

# Part 1
hexValue = inputList[0]
operations, versionSum = parseInput(hexValue)
shared.printAnswer(versionSum)

# Part 2
answer = processOperations(operations)
shared.printAnswer(answer, 2)