from utils import plural_str, newline, door_count, door_directions, number_name

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

    def describe_room(self):
        rtn_str  = 'You are in the '+self.name + newline(1)
        rtn_str += self.description + newline(2)
        rtn_str += 'You see %s door' % number_name(door_count(self.doors))
        rtn_str += plural_str(self.doors) + newline(1)
        return rtn_str
    
    def describe_doors(self):
        rtn_str = ''
        if door_count(self.doors) is 1:
            rtn_str = 'You see one door to the ' + door_directions(self.doors)[0]
        else:
            rtn_str  = 'There are %s doors in this room: ' % number_name(door_count(self.doors))
            for d in door_directions(self.doors):
                rtn_str += ', ' + d

        return rtn_str
    
    def look(self):
        rtn_str  = self.describe_room() + newline(1)
        rtn_str += self.describe_doors()
        return rtn_str


class Player:
    def __init__(self, startRoom):
        self.room = startRoom
    
    def change_rooms(self, room):
        self.room = room

