import sys

dic = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split(":")
        dic[line[0]] = line[1].strip(" \n").split(",")

for name in sys.argv[2].split(","):
    try:
        print(f"{name} : {dic[name][0]},{dic[name][1]} ")
    except IndexError:
        print("There is no college and\or department!!")
    except KeyError:
        print(f"No name found {name} !!")