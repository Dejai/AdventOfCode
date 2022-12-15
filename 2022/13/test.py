x1 = [[[]]]
x2 = [[]]
y = [1,[2,[3,[4,[5,6,7]]]],8,9]
z = [[[[8,6],[8,9,0],1,[]],8,[6,4,4],10,6],[[3,[]],8],[[10],[7,0]],[10,6,5,[[5],[4,6,10,4,0],8,3],[[4],[4,2],[7,3,2,1],3,[4,6,6]]],[[[8,6,9]],1,[9,10,[8,3,7,8]],10]]
z2 = "868901-1,86441063-1,810701065546104083442732134668691910837810"


def getValues(inputList, level=1):

    if len(inputList) == 1:
        # If first element is a list & it is empty: return multiple -1 
        if "list" in str(type(inputList[0])) and len(inputList[0]) == 0:
            return "-1," * level

    if len(inputList) == 0:
        return "-1,"

    # Get list of values
    values = ""

    for item in inputList:
        if "int" in str(type(item)):
            # print("Single Value = " + str(item))
            values += str(item)+","
        elif "list" in str(type(item)):
            # print("List Value = " + str(item))
            values += getValues(item, level+1)

    return values
    

# print(getValues(y))
print(getValues(x1))
print(getValues(x2))
print(getValues(z))
test = [ int(x) for x in getValues(z).split(",") if x != ""]
print(test)
print(z2)