height = input("Enter the height of the wall: ")
width = input("Enter the width of the wall: ")
cover_can = 5

def areaCalc(wall_height,wall_width):
    result = (wall_height * wall_width) / cover_can
    print(f"You will need {round(result)} can of paints")
areaCalc(wall_height= int(height), wall_width= int(width))   