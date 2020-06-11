def win_check(board,mark):
    
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
                
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True

    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
                                    

def whochoose():
    import random
    a=random.randint(0,10)
    if a%2==0:
        return player_1
    else:
        return player_2

def display(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def choosemarker(a):
    if a==player_1:
        marker=""
        while not (marker=="X" or marker=="O"):
            print(a)
            print("Will Choose First:")
            marker=input("MARKER:").upper()
            
        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")
    elif a==player_2:
        marker=""
        while not (marker=="X" or marker=="O"):
            print(a)
            print("Will Choose First:")
            marker=input("MARKER:").upper()
        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")
def place_marker(board, marker, position):
    board[position] = marker        

def space_check(board, position):
    
    if board[position] == "R":
        return True        

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
        


if __name__ == "__main__":
    import sys
    print("Welcome to Tic Tac Toe")
    player_1=input("Player 1:")
    player_2=input("Player 2:")
    a=whochoose()
    if a==player_1:
        player_1_marker,player_2_marker=choosemarker(a)
    else:
        player_2_marker,player_1_marker=choosemarker(a)
    
    print(player_1+","+player_1_marker)
    print(player_2+","+player_2_marker)
    sample_board=["R","R","R","R","R","R","R","R","R","R"]
    display(sample_board)

    if a==player_1:
        print(a+","+"Enter Position:")
        position=int(input())
        if space_check(sample_board, position):
            place_marker(sample_board, player_1_marker, position)
            display(sample_board)
            if win_check(sample_board,player_1_marker)==True:
                print(player_1+","+"Won")
                sys.exit()
                
                

        for i in range(1,10):
            print(player_2+","+"Enter Position:")
            position=int(input())
            if space_check(sample_board, position):
                place_marker(sample_board, player_2_marker, position)
                display(sample_board)
                if win_check(sample_board,player_2_marker)==True:
                    print(player_2+","+"Won")
                    sys.exit()
                    

            print(player_1+","+"Enter Position:")
            position=int(input())
            if space_check(sample_board, position):
                place_marker(sample_board, player_1_marker, position)
                display(sample_board)
                if win_check(sample_board,player_1_marker)==True:
                    print(player_1+","+"Won")
                    sys.exit()
                    

    elif a==player_2:
        print(a+","+"Enter Position:")
        position=int(input())
        if space_check(sample_board, position):
            place_marker(sample_board, player_2_marker, position)
            display(sample_board)
            if win_check(sample_board,player_2_marker)==True:
                print(player_2+","+"Won")
                sys.exit()
                
            


        for i in range(1,10):
            print(player_1+","+"Enter Position:")
            position=int(input())
            if space_check(sample_board, position):
                place_marker(sample_board, player_1_marker, position)
                display(sample_board)
                if win_check(sample_board,player_1_marker)==True:
                    print(player_1+","+"Won")
                    sys.exit()
                    

            print(player_2+","+"Enter Position:")
            position=int(input())
            if space_check(sample_board, position):
                place_marker(sample_board, player_2_marker, position)
                display(sample_board)
                if win_check(sample_board,player_2_marker)==True:
                    print(player_2+","+"Won")
                    sys.exit()
                    






    
        





    

    
