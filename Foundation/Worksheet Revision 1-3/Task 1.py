# Write a car simulation program for Mercadies Ltd. 
# Input the cars gears, speed and outputs messages based on conditions.

def car_simulator():
    
    messages = ["You are going too fast!", "Boom!!! You went too fast and your car blew up!", "Boom!!! You went too fast for the gear you are in and the car blew up!", "Splutter, splutter!!! You were going too slow for the gear you were in and your car stalled!"]

    gear = int(input("Please enter the gear you are in (forward only)"))
    speed = int(input("Please enter the car's speed (mph)"))

    if speed > (gear * 20):
        print(messages[2])
    elif speed < (gear * 8):
        print(messages[3])
    elif speed > 100:
        print(messages[1])
    elif speed > 80:
        print(messages[0])
    else:
        print("Good driving!")

   



if __name__ == '__main__':
    car_simulator()