def f1(x,y):
    z = x*y #the area is base*height
    print("The area is " + str(z))

# Refactor with good style

def rectangule_area(base,height):
    area =  base * height
    print("The area is " + str(area))

rectangule_area(8,8)
