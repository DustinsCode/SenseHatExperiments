from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import signal

sense = SenseHat()

colors = [
    [255,255,255],
    [43,255,0],
    [0,106,255],
    [255,0,255],
    [255,0,0],
]

pixel = colors[0]
x = 3
y = 3


sense.set_pixel(x,y,pixel)

def handler(signum, frame):
    sense.clear()
    exit(1)

signal.signal(signal.SIGINT, handler)

def clamp(value, min_value=0, max_value=7):
    if value < min_value:
        return max_value
    elif value > max_value:
        return min_value
    else:
        return value

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y-1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y+1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x-1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x+1)

def pushed_middle(event):
    global pixel
    if event.action != ACTION_RELEASED:
        index = colors.index(pixel)
        ripple(pixel)
        pixel = colors[index+1] if index + 1 < len(colors) else colors[0]

# ToDo: figure out how to do cool ripple animation when color is changed
def ripple(pixel):
    board = sense.get_pixels()

def update_pixel():
    sense.clear()
    sense.set_pixel(x,y,pixel)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
sense.stick.direction_any = update_pixel
signal.pause()
