import random

counter = 0

bishop_win_counter = 0
rook_win_counter = 0

while (counter <= 4032):
    bishop = int(random.uniform(1,65))

    rook = int(random.uniform(1,65))
    while (bishop == rook):
        rook = int(random.uniform(1,3))
    #####################################
    bishopRoute = []
    #####################################
    upperLeft = bishop

    while (upperLeft % 8 != 1 ):
        upperLeft = upperLeft - 9
        bishopRoute.append(upperLeft)
        if (upperLeft / 8 <= 1):
            break

    #####################################
    upperRight = bishop

    while (upperRight % 8 != 0 ):
        upperRight = upperRight - 7
        bishopRoute.append(upperRight)
        if (upperRight / 8 <= 1):
            break

    #####################################
    lowerLeft = bishop

    while (lowerLeft % 8 != 1 ):
        lowerLeft = lowerLeft + 7
        bishopRoute.append(lowerLeft)
        if (lowerLeft / 8 > 7):
            break

    #####################################
    lowerRight = bishop

    while (lowerRight % 8 != 0 ):
        lowerRight = lowerRight + 9
        bishopRoute.append(lowerRight)
        if (lowerRight / 8 > 7):
            break
    #####################################

    if (rook in bishopRoute):
        bishop_win_counter = bishop_win_counter + 1
    elif(int((rook - 1) / 8 ) == int((bishop - 1) / 8 ) ):
        rook_win_counter = rook_win_counter + 1

    elif(rook % 8 == bishop % 8):
        rook_win_counter = rook_win_counter + 1
    
    counter = counter + 1
    
print("ビショップが勝った回数は" + str(bishop_win_counter))
print("ルークが勝った回数は" + str(rook_win_counter))