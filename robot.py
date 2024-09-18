# Robot navigation in a 5x4 grid

class Robot:
    def __init__(self, x=0, y=0, direction='S'):
        self.x = x  # row
        self.y = y  # column
        self.direction = direction
        self.grid = (5, 4)  # Grid size is 5 rows and 4 columns

    def move(self):
        if self.direction == 'N':
            if self.x > 0:
                self.x -= 1
        elif self.direction == 'S':
            if self.x < self.grid[0] - 1:
                self.x += 1
        elif self.direction == 'E':
            if self.y < self.grid[1] - 1:
                self.y += 1
        elif self.direction == 'W':
            if self.y > 0:
                self.y -= 1

    def change_direction(self, new_direction):
        if self.direction != new_direction:
            self.direction = new_direction

    def execute_commands(self, commands):
        for command in commands:
            if command in ['N', 'S', 'E', 'W']:
                self.change_direction(command)
            elif command == 'M':
                self.move()
        
        return (self.x, self.y, self.direction)

# Reading input command from the user
if __name__ == "__main__":
    # Initial position of the robot is (0,0,S)
    robot = Robot(0, 0, 'S')
    
    # Take input command
    command = input("Enter the command for the robot: ")
    
    # Execute the command and get the final position of the robot
    final_position = robot.execute_commands(command)
    
    # Output the final position of the robot
    print("Robot Location:", final_position)
