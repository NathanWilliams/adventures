
'''
Simple utilities
'''

#Text manipulation
def plural_str(seq):
    l = len(seq)
    if l > 1:
        return 's'
    return ''

def newline(count):
    return '\n'*count


#convenience functions
def door_count(doors):
    return len(doors)

def door_directions(doors):
    return doors.keys()

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

def number_name(num):
    if num is 0:
        return 'zero'
    if num is 1:
        return 'one'
    if num is 2:
        return 'two'
    if num is 3:
        return 'three'
    if num is 4:
        return 'four'


