#!/usr/bin/python

_short_cmds = { 'l':'look', 'g':'get','d':'drop', 'i':'inventory',
                'q':'quit'}

'''
I like the idea of calling the functions by name,
but it doesn't allow me to be specific with the params I give each function

Currently I need to either have everything as a global, or pass an "environment" data structure

I could list the params in the name/func dicttionary I guess
At what point is it better to provide a dispatch function instead?

what would it look like....
cmds={'get':(get, 'player', 'room')}

That doesn't look too bad.
I would probably still have to pass such values in the form of a dictionary though.

How about changes to state?
If I pass in an object, I can modifiy it I guess.
What about errors and other simple return values?

I could define a standard that all functions return.
Something like:
(Success, message)

More thought needed

'''

def look(param_str):
    print 'look!'

def get(param_str):
    print 'get: '+param_str

def drop(param_str):
    print 'drop: '+param_str

def inventory(param_str):
    print 'inventory!'

#being an inventory system, we don't check if rooms are linked
def goto(param_str):
    print 'goto!'

def quit(param_str):
    print 'quit!'

_cmd_funcs = {  'look'      : (look,'room'),
                'get'       : (get,'room','player'),
                'drop'      : (drop,'room','player'),
                'inventory' : (inventory,'player'),
                'goto'      : (goto,)
                'quit'      : (quit,)}


class inventory:
    SUCCESS     = 0
    NO_OBJECT   = 1
    NOT_ENOUGH  = 2
    def __init__(self):
        self.objects = {}

    def add(self, obj, count=1):
        if obj not in self.objects:
            self.objects[obj]=0
        self.objects[obj] += count

    def remove(self, obj, count=1):
        if obj not in self.objects:
            return (False, inventory.NO_OBJECT)
        if count > self.objects[obj]:
            return (False, inventory.NOT_ENOUGH)

        self.objects[obj] -= count
        if self.objects[obj] <= 0:
            del self.objects[obj]

        return (True, inventory.SUCCESS)

def run_cmd(cmd, full_cmd):
    params = ''
    pos = full_cmd.find(' ')
    if pos >= 0:
        params = full_cmd[pos+1:]

    _cmd_funcs[cmd](params)


def expand_cmd(cmd):
    #Expand short commands to their full version
    cmd = cmd.lower()
    if cmd not in _short_cmds:
        return cmd
    return _short_cmds[cmd]

def main():
    print 'Inventory!'
    print 
    
    room = {}
    player = {}


    while 1:
        cmd_line = raw_input('>> ')
        cmd = cmd_line.split(' ')[0]
        cmd = expand_cmd(cmd)
        run_cmd(cmd, cmd_line, env)


if __name__=='__main__':
    main()
