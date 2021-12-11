#input = open("./example.txt", "r+")
input = open("./input.txt", "r+")

positions = {
    "horizontal": 0,
    "depth" : 0,
    "aim": 0
}


for line in input:
    splits = line.split(" ")
    dir = splits[0]
    val = int(splits[1])

    if(dir == "forward"):
        positions["horizontal"] += val
        positions["depth"] += ( positions["aim"] * val )
    elif(dir == "down"):
        #positions["depth"] += val
        positions["aim"] += val
    elif(dir == "up"):
        #positions["depth"] -= val
        positions["aim"] -= val


print(positions)
print(positions["horizontal"] * positions["depth"])