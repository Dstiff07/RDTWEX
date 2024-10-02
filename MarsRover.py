while True:
    
    print("Welcome to Mars Rover.  Here you can enter L to turn the rover Left, R to turn it right, and M to move the rover forwards in the direction it is facing.")
    xmax = input("Please enter the maximum coordinate for the X axis: ")
    ymax = input("Please enter the maximum coordinate for the y axis: ")
    
    x = int(input("Please enter the starting X coordinate for the rover: "))
    y = int(input("Please enter the starting Y coordinate for the rover: "))
    heading = input("Please enter the starting direction for the rover: ")
    if heading == "North" or heading == "north":
            direction = 1
    elif heading == "East" or heading == "east":
            direction = 2
    elif heading == "South" or heading == "south":
            direction = 3
    elif heading == "West" or heading == "west":
            direction = 4
    sequence = input("Please enter your directions, with no spaces.  Please add an X at the end to show the end of your sequence. > ")
    for letter in sequence:
        if letter == "R":
                direction = direction + 1
                if direction == 5:
                        direction = 1
        elif letter == "L":
                direction = direction - 1
                if direction == 0:
                        direction = 4
        elif letter == "M":
                if direction == 1:
                        if y == ymax:
                                print("Movement could not be carried out: exceeding area")
                        else:
                            y = y + 1
                elif direction == 2:
                        if x == xmax:
                                print("Movement could not be carried out: exceeding area")
                        else:
                            x = x + 1
                elif direction == 3:
                        if y == 0:
                            print("Movement could not be carried out: exceeding area")
                        else:
                            y = y - 1
                elif direction == 4:
                        if y == 0:
                            print("Movement could not be carried out: exceeding area")
                        else:
                            x = x - 1
        elif letter == "X":
                break
        if direction == 1:
                heading = "North"
        elif direction == 2:
                heading = "East"
        elif direction == 3:
                heading = "South"
        elif direction == 4:
                heading = "West"
        
    print("Your first mars rover ended up in grid square ", x, ",", y, "facing ", heading)
    repeat = input ("Would you like to try again? Y/N: ")
    if repeat == "Y" or repeat == "y":
            continue
    else:
            break