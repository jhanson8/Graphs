from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"




# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

visited = dict()
track_path = []
#reverse directions used to traverse backwards if needed
reverse = {'n': 's', 'e': 'w', 's': "n", "w": "e"}

# Add the first room to the visited dictionary and get its exits
visited[player.current_room.id] = player.current_room.get_exits()  # {0: [*list of possible exits/paths to take*]}
# print(visited, 'first room info and exits')

# Run the following code until we've hit all 500 rooms
while len(visited) < len(room_graph):
    # If the current room has not been visited
    if player.current_room.id not in visited:
        # Get the exits for the room we're in and store them in our dictionary with the current room's id
        visited[player.current_room.id] = player.current_room.get_exits()
        # access the direction just visited and assign to recent_move
        recent_move = track_path[-1]
        # Remove that direction from the list of possible direction to go for the current room since we've already been there
        visited[player.current_room.id].remove(recent_move)
    # If there are no directions left to go for the current room...
    if len(visited[player.current_room.id]) == 0:
        # Step backwards until we find a path we haven't traversed yet
        recent_move = track_path[-1]
        # As we check we need to remove paths we've already taken
        track_path.pop()
        # Append previous paths to traversal_path
        traversal_path.append(recent_move)
        # Move player as we step backwards
        player.travel(recent_move)
    else:
        # We know that the current room has been visited
        # Get the next path to traverse in the current room
        next_travel = visited[player.current_room.id][-1]
        # Remove 
        visited[player.current_room.id].pop() 
        # Move player
        player.travel(next_travel) 
        # Track our steps as we work in reverse to get to a room we haven't visited
        track_path.append(reverse[next_travel])
        # As we traverse, add to traversal path 
        traversal_path.append(next_travel)



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
