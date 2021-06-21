
#TIC-TAC-TOE

import sys
import random as rnd

def board(lst):
    for i in range(3):
        print((' | ').join(str(j) for j in lst[i]))
        if i < 2:
            print('---------')
    print('              ')

def inp(lst):
    k = -1
    print('enter your prefered index: ')
    try:
        m,n = map(int, input().split())
        k = 0
    except:
        print('enter "1 1" to select 1st row 1st place\nenter "1 2" to select 1st row 2nd place\nenter "1 3" to select 1st row 3rd place\nenter "2 1" to select 2nd row 1st place and so on\n"0 0" to exit the game')
        inp(lst)
    if k == 0:
        if lst[m-1][n-1] == ' ' and m != 0 and n != 0:
            lst[m-1][n-1] = 'X'
            return lst
        elif m == 0 or n == 0:
            sys.exit('you quit the game')
        else:
            print('this index has been filled, choose another')
            return inp(lst)

def compch(lst,zz):
    for i in range(3):
        if lst[i] == [zz,' ',zz]:
            lst[i][1] = 'O'
            return lst
        elif lst[i] == [zz,zz,' ']:
            lst[i][2] = 'O'
            return lst
        elif lst[i] == [' ',zz,zz]:
            lst[i][0] = 'O'
            return lst

    for i in range(3):
        if lst[0][i] == ' ' and lst[1][i] == zz and lst[2][i] == zz:
            lst[0][i] = 'O'
            return lst
        elif lst[0][i] == zz and lst[1][i] == ' ' and lst[2][i] == zz:
            lst[1][i] = 'O'
            return lst
        elif lst[0][i] == zz and lst[1][i] == zz and lst[2][i] == ' ':
            lst[2][i] = 'O'
            return lst

    if lst[0][0] == ' ' and lst[1][1] == zz and lst[2][2] == zz:
        lst[0][0] = 'O'
        return lst
    elif lst[0][0] == zz and lst[1][1] == ' ' and lst[2][2] == zz:
        lst[1][1] = 'O'
        return lst            
    elif lst[0][0] == zz and lst[1][1] == zz and lst[2][2] == ' ':
        lst[2][2] = 'O'
        return lst

    if lst[0][2] == ' ' and lst[1][1] == zz and lst[2][0] == zz:
        lst[0][2] = 'O'
        return lst
    if lst[0][2] == zz and lst[1][1] == ' ' and lst[2][0] == zz:
        lst[1][1] = 'O'
        return lst
    if lst[0][2] == zz and lst[1][1] == zz and lst[2][0] == ' ':
        lst[2][0] = 'O'
        return lst
    return -1

def comp(lst):
    z = compch(lst,'O')
    if z != -1:
        return z
    z = compch(lst,'X')
    if z != -1:
        return z
    
    
    k = rnd.randint(0,2)
    k2 = rnd.randint(0,2)
    if lst[k][k2] == ' ':
        lst[k][k2] = 'O'
        return lst
    else:
        return comp(lst)

def chc(lst):
    for i in range(3):
        if lst[i] == ['X','X','X']:
            return 1
        elif lst[i] == ['O','O','O']:
            return -1
        if lst[0][i] == 'X' and lst[1][i] == 'X' and lst[2][i] == 'X':
            return 1
        elif lst[0][i] == 'O' and lst[1][i] == 'O' and lst[2][i] == 'O':
            return -1
    if lst[0][0] == 'X' and lst[1][1] == 'X' and lst[2][2] == 'X':
        return 1
    elif lst[0][2] == 'X' and lst[1][1] == 'X' and lst[2][0] == 'X':
        return 1
    elif lst[0][0] == 'O' and lst[1][1] == 'O' and lst[2][2] == 'O':
        return -1
    elif lst[0][2] == 'O' and lst[1][1] == 'O' and lst[2][0] == 'O':
        return -1

def log(lst):
    for i in range(9):
        if i%2 == 0:
            lst = inp(lst)
        else:
            lst = comp(lst)
        z = chc(lst)
        board(lst)
        if z == -1:
            print("\nYou're not just a CLOWN, You're the entire CIRCUS\n")
            return 0
        elif z == 1:
            print('\nEnjoy this rare Victory!\n')
            return 0
    print('\nI tip my hat to you, one legend to another!\n')


def start():
    data = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    print('your turn\npress "0 0" to exit')
    log(data)

    ans = input('\ncan you defeat me this time?(y/n)\n')
    if ans == 'y':
        start()


ans = input('\ncan you defeat me this time?(y/n)\n')
if ans == 'y':
    start()



