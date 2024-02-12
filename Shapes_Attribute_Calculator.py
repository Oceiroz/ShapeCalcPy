import math

def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("Input is invalid")
    return user_input

shape_list = ["1.circle", "2.square", "3.rectangle", "4.equilateral triangle", "5.cube", "6.cuboid", "7.sphere", "8.cylinder"]

while(True):
    choice = get_input(f"what shape are you looking to calculate: {shape_list}", int)
    f = open("geometry.txt", "w")
    
    if choice == 1 or choice == 7 or choice == 8:
        radius = get_input("please input the radius", float)
    if choice == 2 or choice == 3 or choice == 4 or choice == 6:
        width = get_input("please input the width", float)
    if choice == 3 or choice == 4 or choice == 6:
        height = get_input("please input the height", float)
    if choice == 5 or choice == 6 or choice == 8:
        depth = get_input("please input the depth", float)
    
    if choice == 1:
        #circle
        shape_a = math.pi * radius ** 2
        shape_p = math.pi * 2 * radius       
    elif choice == 2:
        #square
        shape_a = width ** 2
        shape_p = width * 4
    elif choice == 3:
        #rectangle
        shape_a = (width * height)
        shape_p = (width * 2) + (height * 2)
    elif choice == 4:
        #triangle
        shape_a = (width * height) / 2
        shape_p = width * 3
    elif choice == 5:
        #cube
        shape_a = depth ** 3
        shape_p = (depth * 4) * 6
    elif choice == 6:
        #cuboid
        shape_a = width * depth * height
        shape_p = ((width * depth) + (width * height) + (depth * height)) * 2
    elif choice == 7:
        #sphere
        shape_a = (4/3) * math.pi * radius ** 3
        shape_p = 4 * math.pi * radius ** 2
    elif choice == 8:
        #cylinder
        shape_a = (math.pi * radius ** 2) * depth
        shape_p = ((math.pi * radius ** 2) + (math.pi * radius ** 2 * depth)) * 2
        
    if choice > 4:
        f.write("volume is: " + str(round(shape_a, 2)) + " surface area is: " + str(round(shape_p, 2)))
    elif choice == 1:
        f.write("area is: " + str(round(shape_a, 2)) + " circumference is: " + str(round(shape_p, 2)))
    elif choice < 4 and choice != 1:
        f.write("area is: " + str(round(shape_a, 2)) + " perimeter is: " + str(round(shape_p, 2)))     
    
    f.close()