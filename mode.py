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
def whochoose1():
    import random
    a=random.randint(0,10)
    if a%2==0:
        return player
    else:
        return robot

def display(board):
    print("                                                 ")
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
def choosemarker1(a):
    if a==player:
        marker=""
        while not (marker=="X" or marker=="O"):
            print(a)
            print("Will Choose First:")
            marker=input("MARKER:").upper()
            
        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")
    elif a==robot:
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
    
    if board[position] == " ":
        return True        

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
class Rob():
    def __init__(self):
        pass

    def robot(self,br):
        ar=[]
        for i in range(0,9):
            if i not in br:
                ar.append(i) 
        return ar[1]        

    
        

if __name__ == "__main__":
    import sys
    
    print("Welcome to Tic Tac Toe")
    
    print("Choose the Gaming Mode:")
    print("1.Multiplayer")
    print("2.Vs Computer")
    ch=int(input("->"))

    if ch==1:
        player_1=input("Player 1:")
        player_2=input("Player 2:")
        a=whochoose()
        if a==player_1:
            player_1_marker,player_2_marker=choosemarker(a)
        else:
            player_2_marker,player_1_marker=choosemarker(a)
    
        print(player_1+","+player_1_marker)
        print(player_2+","+player_2_marker)
        sample_board=[" "," "," "," "," "," "," "," "," "," "]
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

    elif ch==2:
        print("Select the Difficulty level")
        print("1.Easy")
        print("2.Medium")
        print("3.Hard")
        ch=int(input("->"))
        if ch==1:
            robot="Raghav"
        elif ch==2:
            robot="Tony Stark"
        else:
            robot="Nick Furry"
        print("                               ________________________")
        print("                              /                        \ ") 
        print("_____________________________/        Hey there!        \_____________________________")
        print("                             \      I'm "+robot+"       /")
        print("                              \________________________/ ")

        player=input("Homie name:")
        a=whochoose1()
        if a==player:
            player_marker,robot_marker=choosemarker1(a)
        else:
            player_marker,robot_marker=choosemarker1(a)
        
        print(player+","+player_marker)
        print(robot+","+robot_marker)
        sample_board=[" "," "," "," "," "," "," "," "," "," "]
        display(sample_board)
        
        br=[]
        if a==player:
            print(a+","+"Enter Position:")
            
            position=int(input())
            br.append(position)

            if space_check(sample_board, position):
                place_marker(sample_board, player_marker, position)
                display(sample_board)
                if win_check(sample_board,player_marker)==True:
                    print(player+","+"Won")
                    sys.exit()
            
            for i in range(1,10):
                my_move=Rob()
                num=my_move.robot(br)
                br.append(num)
                if space_check(sample_board, num):
                    place_marker(sample_board, robot_marker, num)
                    display(sample_board)
                    if win_check(sample_board,robot_marker)==True:
                        print(robot+","+"Won")
                        sys.exit()
                
                print(a+","+"Enter Position:")
            
                position=int(input())
                br.append(position)

                if space_check(sample_board, position):
                    place_marker(sample_board, player_marker, position)
                    display(sample_board)
                    if win_check(sample_board,player_marker)==True:
                        print(player+","+"Won")
                        sys.exit()
        elif a==robot:
            my_move=Rob()
            num=my_move.robot(br)
            br.append(num)
            if space_check(sample_board, num):
                place_marker(sample_board, robot_marker, num)
                display(sample_board)
                if win_check(sample_board,robot_marker)==True:
                    print(robot+","+"Won")
                    sys.exit()
                
            for i in range(1,10):
                print(a+","+"Enter Position:")
            
                position=int(input())
                br.append(position)

                if space_check(sample_board, position):
                    place_marker(sample_board, player_marker, position)
                    display(sample_board)
                    if win_check(sample_board,player_marker)==True:
                        print(player+","+"Won")
                        sys.exit()
                
                my_move=Rob()
                num=my_move.robot(br)
                br.append(num)
                if space_check(sample_board, num):
                    place_marker(sample_board, robot_marker, num)
                    display(sample_board)
                    if win_check(sample_board,robot_marker)==True:
                        print(robot+","+"Won")
                        sys.exit()


                
                

                



                

        
