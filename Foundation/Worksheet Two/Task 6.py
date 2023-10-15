# Task 6
''' using mathmatical equasions to work out the physics equasions'''
print("\nTask 6 \n")

def velocity():
    u = 0
    a = int(input("Please enter the acceleration in metre per second\n")) 
    t = int(input("Please enter the time in seconds\n"))
    v = u + (a*t)
    print(f"Assuming the car started from rest, the final velocity in {t} seconds would be {v}m/s/s")
    
if __name__ == '__main__':
    velocity()

def distance1():
    v = int(input("\nPlease enter the final velocity of the car\n"))
    u = 0
    t = int(input("Please enter the time of travel\n"))
    
    s = 0.5 * (v+u) * t
    print(f"Distance 1 is {s}")
    
if __name__ == '__main__':
    distance1()
    
def distance2():
    u = int(input("\nPlease enter the initial velocity of the car\n"))
    a = int(input("Please enter the acceleration of the car\n"))
    t = int(input("Please enter the time of travel\n"))
    
    s = (u*t) + (0.5 * (a * (t*t)))
    print(f"Distance 2 is {s}")
    
if __name__ == '__main__':
    distance2()
    
def v_squared():
    u = int(input("\nPlease input the initial velocity of the car\n"))
    a = int(input("Please enter the acceleration of the car\n"))
    s = int(input("Please enter the distance of travel\n"))

    u_squared = u * u
    v_squared = u_squared + 2 * (a * s)

    print(f"The final velocity squared is {v_squared}")

if __name__ == '__main__':
    v_squared()
