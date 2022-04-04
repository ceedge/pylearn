'''
Created on Apr 3, 2022

@author: Joker
'''
board=[" " for i in range(9)]

print(board)
def print_board():
    row1="|{}|{}|{}|".format(board[0], board[1],board[2])
    row2="|{}|{}|{}|".format(board[3], board[4],board[5])
    row3="|{}|{}|{}|".format(board[6], board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def player_move(ic):
    if ic == "x":
        num=1
    if ic == "o":
        num=2
    print("Your turn player {}".format(ic))
    choice=int(input("Enter your move (1-9):").strip())
    if board[choice-1]==' ':
        board[choice-1]=ic
        
    else:
        print()
        print("that space is taken")
        return player_move(ic)

def is_victory(ic):
    if (board[0]==ic and board[1]==ic and board[2]==ic)or\
       (board[3]==ic and board[4]==ic and board[5]==ic)or\
       (board[6]==ic and board[7]==ic and board[8]==ic)or\
       (board[0]==ic and board[3]==ic and board[6]==ic)or\
       (board[1]==ic and board[4]==ic and board[7]==ic)or\
       (board[2]==ic and board[5]==ic and board[8]==ic)or\
       (board[0]==ic and board[4]==ic and board[8]==ic)or\
       (board[2]==ic and board[4]==ic and board[6]==ic):
        return True
    else:
        return False
        
def is_draw():
    if " " not in board:
        return True
    else:
        return False
        
while True:
    print_board()
    player_move("x")
    print_board()
    if is_victory("x"):
        print("x wins")
        break
    elif is_draw():
        print(" it is a draw")
        break
    player_move("o")
    if is_victory("o"):
        print_board()
        print("o wins")
        break
    
   


    
        