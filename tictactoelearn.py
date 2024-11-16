board={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
player='X'
computer='O'
def print_board(board):
    print(board['1']+' |'+board['2']+' |'+board['3'])
    print('--|--|--')
    print(board['4']+' |'+board['5']+' |'+board['6'])
    print('--|--|--')
    print(board['7']+' |'+board['8']+' |'+board['9'])
def is_win(board,mark):
    win_combination=[['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
    for combo in win_combination:
        if (board[combo[0]]==board[combo[1]]==board[combo[2]]==mark):
            return True
    return False
def is_draw(board):
    for i in board.values():
            if i==' ':
                return False
    return True
def player_move():
    n=input("Enter a value betwee")
    board[n]=player
def minimax(board,is_maximising):
    if is_win(board,computer):
        return 1
    if is_win(board,player):
        return -1
    if is_draw(board):
        return 0
    
    if is_maximising:
        best_score=float('-inf')
        for key in board.keys():
            if board[key]==' ':
                board[key]=computer
                score=minimax(board,False)
                board[key]=' '
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=float('inf')
        for key in board.keys():
            if board[key]==' ':
                board[key]=player
                score=minimax(board,True)
                board[key]=' '
                best_score=min(best_score,score)
        return best_score
    

def computer_move():
    best_score=float('-inf')
    best_move=None
    for key in board.keys():
        if board[key]==' ':
            board[key]=computer
            score=minimax(board,False)
            board[key]=' '
            if score>best_score:
                best_score=score
                best_move=key
    if best_move is not None:
        board[best_move]=computer
def play_game():
    while True:
        print_board(board)
        player_move()
        if is_win(board,player):
            print("Player Won")
            return
        if is_draw(board):
            print("It is a Draw")
            return
        print_board
        computer_move()
        if is_win(board,computer):
            print("Computer Won")
            return
        
        if is_draw(board):
            print("It is a draw")
            return
        print_board(board)


play_game()

