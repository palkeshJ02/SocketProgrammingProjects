import socket
client = socket.socket()
client.connect(('localhost', 12345))
print("Starting game...")

def update_board(board, pos, player):
    pos = pos -1 
    if pos>=9:
        print("Pos Value Exceeded")
    if player:
        board[(pos//3)][pos%3] = "Y"

    else:
        board[(pos//3)][pos%3] = "O"

    return board

def print_board(board):
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))
        if i < 2:
            print("  ---------")


def check_winner(board):

    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == "Y" for j in range(3)):
            return True
        if all(board[j][i] == "Y" for j in range(3)):  
            return True

    # Check diagonals
    if all(board[i][i] == "Y" for i in range(3)):      
        return True
    if all(board[i][2 - i] == "Y" for i in range(3)):   
        return True

    return False

board = [[' ' for _ in range(3)] for _ in range(3)]

print_board(board)
player = False
for i in range(10):
    if check_winner(board):
        print("You Won!")
        client.send("10".encode())
        break
    if player:
        pos = input("Enter your Square No. :")
        update_board(board,int(pos),player)
        client.send(pos.encode())
        player = False
    else:
        pos = client.recv(1024).decode()
        if "10" in pos:
            print("You Lose!")
            break
        update_board(board, int(pos), player)
        player = True 
    
    print_board(board)
    if i==9:
        print("game Draw")


client.close()
