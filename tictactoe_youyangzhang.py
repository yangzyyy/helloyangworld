#Tic Tac Toe Game by Youyang Zhang 2018.7.12 Hangzhou 


from IPython.display import clear_output
clear_output()
print('Welcome to the Tic Tac Toe Game by Youyang Zhang \n')

################functions##############################################################################################
def choose_xo():
    ply1 = input('Player1 please choose your symbol X or O: ')
    return ply1

def check_valid(inf,seq,rd):
    while inf[seq[rd]][2][-1] in inf[seq[rd]][2][0:-1] or inf[seq[rd]][2][-1] in inf[seq[rd + 1]][2]:
        inf[seq[rd]][2].pop()
        inf[seq[rd]][2].append(int(input(f'LOCATION OCCUPIED. {inf[seq[rd]][0]} please enter another number between 1 and 9 to locate your {inf[seq[rd]][1]}: ')))

def display_board(inf,board):
    for m1 in inf['ply1'][2]:
        if m1 in [1,2,3]:
            new = list(board[2])
            new[4 + 8 * (m1 - 1)] = inf['ply1'][1]
            board[2] = ''.join(new)
        elif m1 in [4,5,6]:
            new = list(board[6])
            new[4 + 8 * (m1 - 4)] = inf['ply1'][1]
            board[6] = ''.join(new)
        else:
            new = list(board[10])
            new[4 + 8 * (m1 - 7)] = inf['ply1'][1]
            board[10] = ''.join(new)
    for m2 in inf['ply2'][2]:
        if m2 in [1,2,3]:
            new = list(board[2])
            new[4 + 8 * (m2 - 1)] = inf['ply2'][1]
            board[2] = ''.join(new)
        elif m2 in [4,5,6]:
            new = list(board[6])
            new[4 + 8 * (m2 - 4)] = inf['ply2'][1]
            board[6] = ''.join(new)
        else:
            new = list(board[10])
            new[4 + 8 * (m2 - 7)] = inf['ply2'][1]
            board[10] = ''.join(new)
    for i in board:
        print(i)

    return(board)

def check_winner(inf,board,rd):
    if board[2][4] == board[2][12] == board[2][20] == inf['ply1'][1] or board[6][4] == board[6][12] == board[6][20] == inf['ply1'][1] or board[10][4] == board[10][12] == board[10][20] == inf['ply1'][1] or board[2][4] == board[6][4] == board[10][4] == inf['ply1'][1] or board[2][12] == board[6][12] == board[10][12] == inf['ply1'][1] or board[2][20] == board[6][20] == board[10][20] == inf['ply1'][1] or board[2][4] == board[6][12] == board[10][20] == inf['ply1'][1] or board[2][20] == board[6][12] == board[10][4] == inf['ply1'][1]:
        print('Player1 is the winner!')
        rd = 10
    elif board[2][4] == board[2][12] == board[2][20] == inf['ply2'][1] or board[6][4] == board[6][12] == board[6][20] == inf['ply2'][1] or board[10][4] == board[10][12] == board[10][20] == inf['ply2'][1] or board[2][4] == board[6][4] == board[10][4] == inf['ply2'][1] or board[2][12] == board[6][12] == board[10][12] == inf['ply2'][1] or board[2][20] == board[6][20] == board[10][20] == inf['ply2'][1] or board[2][4] == board[6][12] == board[10][20] == inf['ply2'][1] or board[2][20] == board[6][12] == board[10][4] == inf['ply2'][1]:
        print('Player2 is the winner!')
        rd = 10
    elif rd == 9:
        print('EVEN!')
    return(rd)

def game(ply1):
    board = ['-------------------------','|       |       |       |','|       |       |       |','|       |       |       |','-------------------------','|       |       |       |','|       |       |       |','|       |       |       |','-------------------------','|       |       |       |','|       |       |       |','|       |       |       |','-------------------------']
    ply1moves = []
    ply2moves = []
    rd = 0
    if ply1 == 'X':
            inf = {'ply1': ['Player1','X',ply1moves],'ply2': ['Player2','O',ply2moves]}
            seq = ['ply1','ply2','ply1','ply2','ply1','ply2','ply1','ply2','ply1','ply2']
    else:
        inf = {'ply1': ['Player1','O',ply1moves],'ply2': ['Player2','X',ply2moves]}
        seq = ['ply2','ply1','ply2','ply1','ply2','ply1','ply2','ply1','ply2','ply1']
    while rd < 9:
        inf[seq[rd]][2].append(int(input(f'{inf[seq[rd]][0]} please enter a number between 1 and 9 to locate your {inf[seq[rd]][1]}: ')))
        check_valid(inf,seq,rd)
        display_board(inf,board)
        rd += 1
        rd = check_winner(inf,board,rd)
    replay()
    

def replay():
    r = input('Do you want to replay Yes or No: ')
    if r == 'Yes':
        ply1 = choose_xo()
        game(ply1)

#######################################################################################################################
ply1 = choose_xo()

print('\n\nThis the game board')
original_board = ['-------------------------','|       |       |       |','|   1   |   2   |   3   |','|       |       |       |','-------------------------','|       |       |       |','|   4   |   5   |   6   |','|       |       |       |','-------------------------','|       |       |       |','|   7   |   8   |   9   |','|       |       |       |','-------------------------']
for i in original_board:
    print(i)
st = input('Are you ready to start the game Yes or No: ')

if st == 'Yes':
    game(ply1)

