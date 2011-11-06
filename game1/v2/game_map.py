
from objects import Door, Room
roomHeap = {}

def make_world():
    global roomHeap
    
    frontDoor = {'south' : Door('Front Yard', 'Lounge Room')}
    roomHeap['Front Yard'] = Room('Front Yard', 'Green grass and a garden gnome', frontDoor)
    
    lrDoors = {'north' : Door('Lounge Room', 'Front Yard'), 'south' : Door('Lounge Room', 'Hall')}
    roomHeap['Lounge Room'] = Room('Lounge Room', 'Small lounge and a big tv', lrDoors)

    hlDoors = {'north' : Door('Hall', 'Lounge Room'), 'south' : Door('Hall', 'Kitchen'), 'west' : Door('Hall', 'Backyard')}
    roomHeap['Hall'] = Room('Hall', 'A hallway connection the rooms of the house', hlDoors)

    ktDoors = {'north' : Door('Kitchen', 'Hall')}
    roomHeap['Kitchen'] = Room('Kitchen', 'A small kitchen', ktDoors)

    byRooms = {'east' : Door('Backyard', 'Hall')}
    roomHeap['Backyard'] = Room('Backyard', 'A small backyard', byRooms)


def get_room(name):
    return roomHeap[name]

def current_room(player):
    return get_room(player.room)


