board = COM()
for port in board.serialList():
    print(port)
board.serOpen("COM3")
for x in range(25):
    print(board.startEgram())
board.stopEgram()
print(board.serRead())
board.serWrite([4, 60, 120, 5.0, 1, 5.0, 1, 320, 250, 0.6, 4.5, 0, 120, 1.75, 2000, 8, 5, 150])
print(board.serRead())
board.serClose()