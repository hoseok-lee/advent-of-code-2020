import numpy as np



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("directions.txt", "r")
directions = [
    [x[0], int(x[1:])]
        
    for x in list(f.read().split("\n"))
]



'''
    PART 1: PROCESS DIRECTIONS

    Complexity: O(n)

    This algorithm is very straightforward. It keeps track of the current 
    direction that it is facing, and calculates its current horizontal and
    vertical location accordingly. It accounts for different directions by
    shifting the NSEW directions.
'''
'''
# Current direction
# current_direction[0] is the direction the boat is currently facing
# If the boat is turned left or right, it will shift all elements to the left
# or right accordingly
current_direction = np.array(["E", "S", "W", "N"])

# Cardinal directions
# Denotes the travel vector of each cardinal direction
cardinal_directions = {
    "E": np.array([1, 0]), 
    "S": np.array([0, -1]), 
    "W": np.array([-1, 0]), 
    "N": np.array([0, 1])
}

# Current ship position
# E/W and then N/S
current_position = np.array([0, 0])

# Iterate through the directions
for dir_type, dir_value in directions:
    # Travel forward
    if dir_type == "F":
        current_position = np.add(current_position,
            cardinal_directions[current_direction[0]] * dir_value)

    # Turn left or right
    elif dir_type in "LR":
        roll_direction = int(dir_value / 90) * (-1 if dir_type == "R" else 1)
        current_direction = np.roll(current_direction, roll_direction)
            
    # Translation in cardinal direction
    else:
        current_position = np.add(current_position,
            cardinal_directions[dir_type] * dir_value)

print(np.sum(np.abs(current_position)))
'''


'''
    PART 2: PROCESS WAYPOINT

    Complexity: O(n)

    This algorithm operates on a very similar fashion. The only difference is
    the only operation that effect the ship's movement is F, and the rest will
    effect the waypoint's position/direction.

    The waypoint's direction can be calculated by using a rotational matrix, 
    and considering the waypoint's position coordinates as vectors.
'''

# Generate rotational matrix based on its angle and direction
def rotational_matrix (angle):
    return np.array([
        [int(np.cos(angle)), -int(np.sin(angle))],
        [int(np.sin(angle)), int(np.cos(angle))]
    ])



# Cardinal directions
# Denotes the travel vector of each cardinal direction
cardinal_directions = {
    "E": np.array([1, 0]), 
    "S": np.array([0, -1]), 
    "W": np.array([-1, 0]), 
    "N": np.array([0, 1])
}

# Current waypoint position
# E/W and then N/S
waypoint = np.array([10, 1])

# Current ship position
# E/W and then N/S
current_position = np.array([0, 0])

# Iterate through the directions
for (dir_type, dir_value) in directions:
    # Travel forward
    if dir_type == "F":
        current_position = np.add(current_position, waypoint * dir_value)

    # Turn left or right
    elif dir_type in "LR":
        rotation_angle = np.radians(dir_value) * (-1 if dir_type == "L" else 1)
        rotation = rotational_matrix(rotation_angle)
        waypoint = np.matmul(waypoint.transpose(), rotation)

    # Translation in cardinal direction
    else:
        waypoint = np.add(waypoint, cardinal_directions[dir_type] * dir_value)

print(np.sum(np.abs(current_position)))