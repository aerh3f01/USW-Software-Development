class Car:
    RIGHT = 1
    LEFT = -1
    FORWARD = 1
    REVERSE = 0

    def __init__(self):
        self._speed = 0
        self._gear = 1
        self._direction = 0  # front of car
        self._broken = False  # indicates whether car is broken
        self._simulation = []
        self._simulation_loaded = False

    def accelerate(self):
        if self._broken:
            return
        print("Accelerating...")
        increment = 5 if self._gear != 0 else -5
        self._speed += increment
        if self._speed > 80: self._speed = 80
        if self._speed < -10: self._speed = -10
        self._change_gear()
        self.display_stats()

    def brake(self):
        if self._broken:
            return
        print("Braking...")
        decrement = -5 if self._gear != 0 else 5
        self._speed += decrement
        if self._speed > 80: self._speed = 80
        if self._speed < -10: self._speed = -10
        self._change_gear()
        self.display_stats()

    def turn_steering_wheel(self, direction_change):
        if self._broken or direction_change not in [self.RIGHT, self.LEFT, 0]:
            return
        if self._gear == 0:  # In reverse
            direction_change = -direction_change
        self._direction += direction_change
        if self._direction > 11:
            self._direction -= 12
        elif self._direction < 0:
            self._direction += 12
        self.display_stats()

    def select_forward_or_reverse(self, selected_direction):
        if self._speed != 0:
            self._broken = True
            print("Car broke due to direction change while moving!")
            return
        self._gear = 0 if selected_direction == self.REVERSE else 1
        self.display_stats()

    def _change_gear(self):
        previous_gear = self._gear
        if self._broken:
            return
        # Automatic gear change logic
        gear_speed_ranges = [(-10, 0), (0, 10), (10, 20), (20, 30), (30, 45), (45, 80)]
        for i, (min_speed, max_speed) in enumerate(gear_speed_ranges):
            if min_speed < self._speed <= max_speed:
                self._gear = i
                if previous_gear != self._gear:
                    print(f"Changing up...\nCurrent gear = {self._gear}")
                break

    def display_stats(self):
        print(f"Speed = {self._speed}, Gear = {self._gear}, Direction = {self._direction}")

    def load_simulation(self, filename):
        try:
            with open(filename, 'r') as file:
                self._simulation = file.read().splitlines()
                self._simulation_loaded = True
        except FileNotFoundError:
            print("Simulation file not found.")
            self._simulation_loaded = False

    def run_simulation(self):
            if not self._simulation_loaded:
                print("Simulation not loaded.")
                return
            print("Loading simulation...")
            
            # Execute the command actions based on the simulation commands
            for command in self._simulation:
                # Execute the command action based on the command
                if command == "FORWARD":
                    self.select_forward_or_reverse(self.FORWARD)
                elif command == "REVERSE":
                    self.select_forward_or_reverse(self.REVERSE)
                elif command == "ACCELERATE":
                    self.accelerate()
                elif command == "BRAKE":
                    self.brake()
                elif command == "LEFT":
                    self.turn_steering_wheel(self.LEFT)
                elif command == "RIGHT":
                    self.turn_steering_wheel(self.RIGHT)
                else:
                    print(f"Invalid command: {command}")
                    break


if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
