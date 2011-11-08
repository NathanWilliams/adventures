#!/usr/bin/python

import curses

'''
How I want a room to be drawn:

#####D####D
#.........#
#.........#
D.........#
#.........#
#.........#
#####D#####
With doors to the north, north east, west and south 

'''

'''
doors
    n
    ne
    e
    se
    s
    sw
    w
    nw

'''

def door_wall(d):
    if d:
        return 'D'
    return '#'

def horz_wall(w, d1, d2, d3):
    rtn=''
    rtn += door_wall(d1)
    mid_point = w/2 #allow truncation
    rtn += '#'*(mid_point-1)
    rtn += door_wall(d2)
    rtn += '#'*(mid_point-1)
    rtn += door_wall(d3)
    return rtn

def draw_room(screen, x,y, doors):
    #doors can be at all points of the compass
    #including ne, sw etc
    #doors should be drawn at the mid point of a wall, or the corner of the walls
    
    w = 10
    h = 10
    
    room = []
    room.append(horz_wall(w, 'nw' in doors, 'n' in doors, 'ne' in doors))
    mid_height = h/2
    for i in range(0,mid_height-2):
        room.append('#' + '.'*(w-1) + '#')

    #mid way down
    room.append(door_wall('w' in doors) + '.'*(w-1) + door_wall('e' in doors))

    for i in range(0,mid_height-2):
        room.append('#' + '.'*(w-1) + '#')
    
    room.append(horz_wall(w, 'sw' in doors, 's' in doors, 'se' in doors))
    for i,txt in enumerate(room):
        screen.addstr(y+i,x,txt)


def main(screen):
    doors = {'n':1,'e':1, 'w':1, 'sw':1}
    draw_room(screen, 5,10, doors)
    screen.refresh()
    screen.getch()
    curses.endwin()

if __name__=='__main__':
    curses.wrapper(main)
