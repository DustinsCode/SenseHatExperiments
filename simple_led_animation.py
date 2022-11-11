from sense_hat import SenseHat
import time
import signal

sense = SenseHat()

x = [138,138,138] # Any RBG values, this one's grayish/dimmed
o = [0,0,0] #Led Off

board = [
o,x,o,x,o,x,o,x,
x,o,x,o,x,o,x,o,
o,x,o,x,o,x,o,x,
x,o,x,o,x,o,x,o,
o,x,o,x,o,x,o,x,
x,o,x,o,x,o,x,o,
o,x,o,x,o,x,o,x,
x,o,x,o,x,o,x,o,
]

def handler(signum, frame):
    sense.show_message("bye")
    exit(1)

signal.signal(signal.SIGINT, handler)

def update_board(board):
    for index, pixel in enumerate(board):
        if pixel == o:
            pixel = x
        else:
            pixel = o
        board[index] = pixel
    return board

while True:
    sense.set_pixels(board)
    time.sleep(0.5)
    board = update_board(board)
