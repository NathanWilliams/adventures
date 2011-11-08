#!/usr/bin/python


def nl(count):
    return '\n'*count

def add_to_inventory(inv, item, count=1):
    if item not in inv:
        inv[item] = 0
    inv[item] += count
    return inv

def remove_from_inventory(inv, item, count=1):
    if item not in inv:
        raise Exception('This needs to be better')
    inv[item] -= count #there needs to be checking here too
    if inv[item] <= 0:
        del inv[item]
    return inv

def move_object(name, from_inv, to_inv):
    
    if name not in from_inv:
        msg = 'There is no '+name #this needs a way to say "in this room" or "in your pocket"
    else:
        msg = name+' transferred' #again, this needs a way to customise this
        to_inv = add_to_inventory(to_inv, name)
        from_inv = remove_from_inventory(from_inv, name)
    return msg, from_inv, to_inv

def make_player_inventory():
    return {'Apple':1,
            'Piece of Eight':2}

def list_inventory(inv):
    rtn = ''
    for k in inv:
        rtn += str(inv[k]) + ' x '+k + nl(1)
    return rtn

def fill_rooms():
    rtn = []
    tmp = {}
    tmp = add_to_inventory(tmp, 'Rock')
    tmp = add_to_inventory(tmp, 'Apple')
    rtn.append(tmp)

    tmp = {}
    tmp = add_to_inventory(tmp, 'Piece of Eight', 10)
    rtn.append(tmp)

    return rtn

def get_input():
    return raw_input('>> ').strip()

def eval_cmd(cmd):
    '''The main loop was getting messy'''
    if cmd == 'quit' or cmd == 'q':
        return ('quit',None)
    if cmd == 'look':
        return ('look',None)
    if cmd == 'inventory' or cmd == 'i':
        return ('inventory', None)
    cs = cmd.split(' ')
    if cs[0] == 'room' and len(cs) == 2:
        try:
            num = int(cs[1])
        except ValueError:
            return (False, '"'+cs[1]+'" is not a valid room number')
        return ('room',num)
    elif cs[0] == 'get':
        return ('get', cs[1])
    elif cs[0] == 'drop':
        return ('drop',cs[1])
    else:
        return (False, 'Unknown command: '+cmd)
    return (False, 'How did I get here?')



def main():
    print 'An inventory system'
    
    player_inventory = make_player_inventory()
    room_inventories = fill_rooms()
    room = 0

    while 1:
        cmd = get_input()
        cmd, val = eval_cmd(cmd)
        if cmd == 'quit':
            print 'Bye!'
            return
        elif cmd == 'inventory':
            print list_inventory(player_inventory)
        elif cmd == 'room':
            if val >= len(room_inventories):
                print 'There is no room '+str(val)
            else:
                room = val
                print 'Changed to room '+str(val)
                print 'It contains: '
                print list_inventory(room_inventories[room])
        elif cmd == 'look':
            print 'You are in room '+str(room)
            print 'It contains: '
            print list_inventory(room_inventories[room])
        elif cmd == 'get':
            msg, ri, pi = move_object(val, room_inventories[room], player_inventory)
            room_inventories[room] = ri
            player_inventory = pi
            print msg
        elif cmd == 'drop':
            msg, pi, ri = move_object(val, player_inventory, room_inventories[room])
            room_inventories[room] = ri
            player_inventory = pi
            print msg

        elif cmd is False:
            print val #val is the error message

if __name__=='__main__':
    main()
