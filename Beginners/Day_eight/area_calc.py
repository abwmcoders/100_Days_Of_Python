def paint_area_calc(height, width, cover):
    area_calc = round((height * width) / cover)
    print(f"THe total cans of paint needed is {area_calc}")

wall_h = int(input("Enter the height of the wall: "))
wall_w = int(input("Enter the width of the wall: "))
coverage = 5

paint_area_calc(height=wall_h, width=wall_w, cover=coverage)
