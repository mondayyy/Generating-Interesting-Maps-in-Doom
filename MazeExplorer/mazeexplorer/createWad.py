from omg import *
from maze import *
from wad import *
import numpy

# Global Variables
WALL = 1
EMPTY = 0

# print map 
def print_map(board):
	# Print the rows
	for r in board:
		#print(r)
		rowprint = ""
		for c in r:
			if c == WALL:
				rowprint = rowprint + "X"
			else:
				rowprint = rowprint + " "
		print(rowprint)


## TO DO
# create a list of wall points [DONE]
# set spawn point for agent
# set spawn point for keys
# create a wall that has direction only up or right [DONE]
# get these maps to show up in Eureka [IN PROGRESS]
##

# make sure to add floor/ceiling
def create_map():
	# create clear map 9x9
	base_map = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
		[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]]
    	
	print_map(base_map)

    
	# find appropriate wall points with direction (wall will be 2 spaces long)
	wall_points = [(1, 1), (3,4), (5,5), (7,7)]

	for point in wall_points:
		print(point)
		#print(base_map[point[0]][point[1]])
		base_map[point[0]][point[1]] = WALL
        
	# add a wall that goes up or right at these points
	prob = 0.5
	for point in wall_points:
		if random.random() < prob:
			# add wall that goes up
			print("Wall faces up")
			base_map[point[0]-1][point[1]] = WALL
		else:
			# add wall that goes right
			print("Wall faces right")
			base_map[point[0]][point[1]+1] = WALL

	print_map(base_map)
    
	# save map as a .txt file
	with open('testMap1.txt', 'w') as output_file:
		for row in base_map:
			rowprint = ""
			for c in row:
				if c == WALL:
					rowprint = rowprint + "X"
				else:
					rowprint = rowprint + " " 
			output_file.write(rowprint)
			output_file.write("\n")
	output_file.close()
	print(output_file, " is created!")
	return output_file

# main
maze_path = "tempfile"
maze_id = 3
# mazes = generate_mazes(maze_path, maze_id)

# create .txt representation of this
### TO DO
# change varables in .txt file to match naming scheme
###
testMap1 = create_map()

# create a .wad representation of testMap1 (.txt file)
outputs = os.path.join(maze_path, "outputs/")
generate_wads(maze_path, maze_path + ".wad", outputs + "maze.o")
