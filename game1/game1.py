#!/usr/bin/python

'''
Map layout is small and simple, but testing all different door combinations and directions.

'''
def plural_str(seq):
    l = len(seq)
    if l > 1:
        return 's'
    return ''

def newline(count):
    return '\n'*count

def door_count(doors):
    return len(doors)

def door_directions(doors):
    return doors.keys()

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


def make_player():
    player = Player('Front Yard') 
    return player

def get_room(name):
    return roomHeap[name]

def current_room(player):
    return get_room(player.room)

def room_look(room):
    rtn_str  = room.describeRoom() + newline(1)
    rtn_str += room.describeDoors()
    
    return rtn_str

def get_doors(room):
    return room.doors

def dir_opts(room):
    rtn_str = '('
    for d in door_directions(get_doors(room)):
        rtn_str += d[0] + ','
    rtn_str = rtn_str[:-1] + ')'
    return rtn_str

def expand_dir(cmd):
    if cmd == 'n':
        cmd = 'north'
    if cmd == 'e':
        cmd = 'east'
    if cmd == 's':
        cmd = 'south'
    if cmd == 'w':
        cmd = 'west'
    return cmd
    
def check_valid_move(room, cmd):
    return expand_dir(cmd) in door_directions(get_doors(room))

def get_door(room, direction):
    return room.doors[expand_dir(direction)]


class Door:
    def __init__(self, roomFrom, roomTo):
        self.roomAttached = roomFrom
        self.destination = roomTo
    
    def enter(self, player):
        fromRoom = player.room
        assert fromRoom == self.roomAttached, 'Entering a door not in this room! Coming from room %s but door is attached to %s' % (fromRoom, self.roomAttached)

        player.change_rooms(self.destination)
        

class Room:
    def __init__(self, roomName, roomDescription, doorDict):
        self.name = roomName
        self.description = roomDescription
        self.doors = doorDict

    def describeRoom(self):
        rtn_str  = 'You are in the '+self.name + newline(1)
        rtn_str += self.description + newline(2)
        rtn_str += 'You see %d door' % door_count(self.doors)
        rtn_str += plural_str(self.doors) + newline(1)
        return rtn_str
    
    def describeDoors(self):
        rtn_str = ''
        if door_count(self.doors) is 1:
            rtn_str = 'You see one door to the ' + door_directions(self.doors)[0]
        else:
            rtn_str  = 'There are %d doors in this room' % door_count(self.doors)
            for d in door_directions(self.doors):
                rtn_str += ', ' + d

        return rtn_str

class Player:
    def __init__(self, startRoom):
        self.room = startRoom
    
    def change_rooms(self, room):
        self.room = room

def main():
    game_name = "Walking the halls"
    print game_name
    print "*"*len(game_name)
    print "The goal is simple, walk the halls and visit every room"

    make_world()
    player = make_player()
    
    print 'Your only commands are directions'
    print 's or south, n or north and so on'
    print
    print
    
    while 1:
        room = current_room(player)
        print room_look(room)
        cmd = raw_input('Direction ' + dir_opts(room) + ' > ')
        valid = check_valid_move(room, cmd) 
        if not valid:
            print 'That is an invalid direction'
            continue

        d = get_door(room, cmd)
        d.enter(player)

    
if __name__ == '__main__':
    main()
