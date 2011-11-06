#!/usr/bin/python

import curses


def main(screen):
    curses.start_color()
    screen.border(0)
    screen.addstr(0,0, 'Hello world')
    


if __name__ == '__main__':
    curses.wrapper(main)
