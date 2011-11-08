#!/usr/bin/python

'''
A from scratch reimplementation of the room system.
'''

directions = [ 'n','ne','e','se','s','sw','w','nw',
                'north', 'north east', 'east', 'south east', 'south', 'south west', 'west', 'north west']

dir_names = {   'n' : 'North',
                'e' : 'East',
                's' : 'South',
                'w' : 'West'}

def dir_name(d):
    if len(d) is 1:
        return dir_names[d]
    if len(d) is 2:
        return dir_names[d[0]] + ' ' + dir_names[d[1]]
    return d.title() #you have to love python!

def cmd_to_dir(cmd):
    s = cmd.strip().split(' ')
    if len(s) is 1:
        if len(cmd.strip()) is 2:
            return cmd.lower()
        return cmd[0].lower()
    return s[0][0].lower() +s[1][0].lower()


def nl(count):
    return '\n'*count

def get_input():
    return raw_input('>> ').lower()

def move_to(cmd, current_room, rooms):
    r = rooms[current_room]
    d = r['doors']
    direction = cmd_to_dir(cmd)
    valid = direction in valid_doors(d)
    new_room = None
    if valid:
        new_room = d[direction]
    return valid, new_room

def make_room(name, desc, doors):
    return {'name' : name,
            'desc' : desc,
            'doors' : doors}

def make_doors(n=None,ne=None,e=None,se=None,s=None,sw=None,w=None,nw=None):
    return {'n':n,
            'ne':ne,
            'e':e,
            'se':se,
            's':s,
            'sw':sw,
            'w':w,
            'nw':nw}

def add_room(room_map, room):
    room_map[room['name']] = room
    return room_map

def make_map():
    rooms = {}
    rooms = add_room(rooms, make_room('Prison Cell', 'Dark and damp', make_doors(s='Corridor')))
    rooms = add_room(rooms, make_room('Corridor', 'A long narrow passage', make_doors(n='Prison Cell', e='Guard station')))
    rooms = add_room(rooms, make_room('Guard station', 'A deserted guard station', make_doors(w='Corridor', se='Exit')))
    rooms = add_room(rooms, make_room('Exit', "I'm too lazy to make more rooms!", make_doors(nw='Guard station')))
    return rooms

def look_room(rooms, current_room):
    r = rooms[current_room]
    rtn = 'You are in a ' + r['name'] +nl(1)
    rtn += 'It is '+ r['desc'] +nl(1)
    rtn += desc_doors(r) +nl(2)
    return rtn

def valid_doors(doors):
    r = []
    for d in doors:
        if doors[d] is None:
            continue
        r.append(d)
    return r

def desc_doors(room):
    #It has doors to the
    #north, south and south east
    #or:
    #It has a door to the north
    rtn = ''
    doors = valid_doors(room['doors'])
    if len(doors) is 1:
        rtn = 'There is a door to the ' + dir_name(doors[0])
    else:
        rtn = 'There are doors to the '
        for d in doors[:-2]:
            rtn += dir_name(d) +','
        rtn += dir_name(doors[-2]) + ' and ' + dir_name(doors[-1])

    return rtn

def main():
    print 'Stay a while, stay forever!'
    print
    rooms = make_map()
    current_room = 'Prison Cell'
    print look_room(rooms, current_room)
    while 1:
        cmd = get_input()
        if cmd == 'quit' or cmd == 'q':
            print 'Bye!'
            break
        elif cmd in directions:
            valid, room = move_to(cmd, current_room, rooms)
            if valid:
                current_room = room
                print look_room(rooms, current_room)
            else:
                print 'There is no door to the '+dir_name(cmd) 
        elif cmd == 'look':
            print look_room(rooms, current_room)
        else:
            print 'What do you mean by "'+cmd+'"?'



if __name__=='__main__':
    main()

