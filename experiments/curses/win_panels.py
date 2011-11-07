#!/usr/bin/python

import curses
import curses.panel

def main(screen):
    curses.start_color()
    screen.border(0)
    screen.addstr(0,0, 'Hello world')

    sub_win = curses.newwin(10, 20, 30, 20)
    sub_win.border(0)
    sub_win.addstr(3,4, 'blah')
    screen_panel = curses.panel.new_panel(screen)
    sw_panel = curses.panel.new_panel(sub_win)
    sw_panel.top()
    curses.panel.update_panels()
    curses.doupdate()
    sub_win.getch()
    sw_panel.hide()
    screen.getch()
    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(main)
