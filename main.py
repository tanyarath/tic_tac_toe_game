def tic_tac_toe_game():
    num = 9
    lisst = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    board = [' ' for _ in range(9)]

    def display_board():
        print(f'''
         | {board[0]} | {board[1]} | {board[2]} |
        --------------
         | {board[3]} | {board[4]} | {board[5]} |
        --------------
         | {board[6]} | {board[7]} | {board[8]} |
        ''')

    while num > 0:
        # PLAYER 1
        try:
          choice1 = int(input("PLAYER 1 :: Enter the move you want to play (1-9): "))
          while 'I'f'{choice1}' not in lisst:
            if choice1 < 1 or choice1 > 9:
                print("Invalid choice! Try again.")
                choice1 = int(input("PLAYER 1 :: Enter the move you want to play (1-9): "))
                
            if board[choice1 - 1] != ' ':
                print("Cell already occupied! Try again.")
                choice1 = int(input("PLAYER 1 :: Enter the move you want to play (1-9): "))
                
          board[choice1 - 1] = 'X'
          lisst.remove(f'I{choice1}')
          display_board()
          if (board[0] =='X' and board[1] =='X' and board[2]=='X') or(board[3]=='X' and board[4] =='X' and board[5] =='X')or(board[6]=='X' and board[7]=='X' and board[8]=='X')or(board[0]=='X' and board[3]=='X' and board[6]=='X')or (board[1]=='X' and board[4]=='X' and board[7]=='X')or(board[2]=='X' and board[5]=='X' and board[8]=='X')or(board[0]=='X' and board[4]=='X' and board[8]=='X') or (board[2]=='X' and board[4]=='X' and board[6]=='X'):
              print("\n")
              print("\n")
              print("***************************")
              print("\n")
              print("\n")
              print("WOOH ! PLAYER1 WON THE GAME")
              print("\n")
              print("\n")
              print("***************************")
              print("\n")
              print("\n")
              return
          num -= 1
        except ValueError:
            print("Enter a valid number!")
            continue

        if num == 0:
            break

        # PLAYER 2
        try:
          
          choice2 = int(input("PLAYER 2 :: Enter the move you want to play (1-9): "))
          while 'I'f'{choice2}' not in lisst:  
            if choice2 < 1 or choice2 > 9:
                print("Invalid choice! Try again.")
                choice2 = int(input("PLAYER 2 :: Enter the move you want to play (1-9): "))
            if board[choice2 - 1] != ' ':
                print("Cell already occupied! Try again.")
                choice2 = int(input("PLAYER 2 :: Enter the move you want to play (1-9): "))
          board[choice2 - 1] = 'O'
          lisst.remove(f'I{choice2}')
          display_board()
          if (board[0] =='O' and board[1] =='O' and board[2]=='O') or(board[3]=='O' and board[4] =='O' and board[5] =='O')or(board[6]=='O' and board[7]=='O' and board[8]=='O')or(board[0]=='O' and board[3]=='O' and board[6]=='O')or (board[1]=='O' and board[4]=='O' and board[7]=='O')or(board[2]=='O' and board[5]=='O' and board[8]=='O')or(board[0]=='O' and board[4]=='O' and board[8]=='O') or (board[2]=='O' and board[4]=='O' and board[6]=='O'):
              print("\n")
              print("\n")
              print("***************************")
              print("\n")
              print("\n")
              print("WOOH ! PLAYER2 WON THE GAME")
              print("\n")
              print("\n")
              print("***************************")
              print("\n")
              print("\n")
              return
          num -= 1
        except ValueError:
            print("Enter a valid number!")
            continue
    print("OOPS ! GAME IS DRAW ")        

tic_tac_toe_game()
