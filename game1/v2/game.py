#!/usr/bin/python

from objects import Player
from game_map import make_world, get_room, current_room
from utils import dir_opts, check_valid_move, get_door

GAME_NAME   = "Walking the halls"
GOAL        = "The goal is simple, walk the halls and visit every room"

def stars(count):
    return "*"*count


def main():
    print GAME_NAME
    print stars(len(GAME_NAME))
    print GOAL

    make_world()
    player = Player('Front Yard')
    
    print 'Your only commands are directions'
    print 's or south, n or north and so on'
    
    while 1:
        room = current_room(player)
        print
        print room.look()
        cmd = raw_input('Direction ' + dir_opts(room) + ' > ')
        valid = check_valid_move(room, cmd) 
        if not valid:
            print 'That is an invalid direction'
            continue

        d = get_door(room, cmd)
        d.enter(player)

    
if __name__ == '__main__':
    main()
