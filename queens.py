count=0
def check(x,y,board):
    for i in range(x):
        if board[i][y]==1:
            #print('Y',board)
            return False
    for ix in range(8):
        for iy in range(8):
            if (ix+iy==x+y or ix-iy==x-y)and(board[ix][iy]==1):
                #print('X',board)
                return False
    return True

def rec(x,y,board):
    global count
    if x==7:
        count=count+1
        print('D',board)
        return
    else:
        for i in range(8):
            #board[x+1][i]=1
            if check(x+1,i,board):
                board[x+1][i]=1
                rec(x+1,i,board)
                board[x+1][i]=0

board=[[0 for i in range(8)]for i in range(8)]
for i in range(8):
    board[0][i]=1
    rec(0,i,board)
    board[0][i]=0
print(count)
