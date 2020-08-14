from room import Room
from player import Player
from world import World

# imported Queue Class
from util import Queue
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

####################################

# class Room
    # print_room_description(self, player)
    # get_exits(self)
    # get_exits_string(self)
    # connect_rooms(self, direction, connecting_room)
    # get_room_in_direction(self, direction)
    # get_coords(self)
    
# class Player
    # travel(self, direction, show_rooms = False)
    
##################################

visited = {}
reverse_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}
reverse = []
rooms_to_visit = []
        
# loop while room_graph is larger than visited
while len(room_graph) > len(visited):
    # gets current room
    current = player.current_room.id
    # gets all the exits of current_room
    exits = player.current_room.get_exits()
    # puts current into rooms_to_visit array
    rooms_to_visit.append(current)
    # gets current's exits
    if current not in visited:
        visited[current] = exits
    # checks length
    if len(visited[current]) > 0:
        # pop current in visited
        v = visited[current].pop()
        # appends to traversal_path array
        traversal_path.append(v)
        # appends to reverse array reverse direction
        reverse.append(reverse_direction[v])
        # player goes to v
        player.travel(v)
        
    else:
        # reverse direction
        r = reverse.pop()
        traversal_path.append(r)
        player.travel(r)    
    



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######


# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
