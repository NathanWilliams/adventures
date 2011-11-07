#!/usr/bin/python

import curses

def main(screen):
    screen.border(0)
    screen.addstr('Main screen')
    maxy, maxx = screen.getmaxyx()
    cmd_win = screen.derwin(maxy-10,0)
    cmd_win.border(0)
    cmd_win.addstr('Command Window')
    screen.refresh()
    curses.echo()
    cmd_win.addstr(1,1, '>> ')
    txt = cmd_win.getstr(1,4)

    
    #screen.getch()
    curses.endwin()

if __name__=='__main__':
    curses.wrapper(main)

