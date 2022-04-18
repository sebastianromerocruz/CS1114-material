from touchTypes import TouchType, SwipeDirection

# Don't worry about how these nine constants work (or about the touchTypes module in general)
# Just know that you can use them in your register_touch() function
SINGLE_TOUCH = TouchType.SINGLE_TOUCH
DOUBLE_TAP = TouchType.DOUBLE_TAP
SWIPE = TouchType.SWIPE
HOLD = TouchType.HOLD
UP = SwipeDirection.UP
DOWN = SwipeDirection.DOWN
LEFT = SwipeDirection.LEFT
RIGHT = SwipeDirection.RIGHT
NO_DIRECTION = SwipeDirection.NO_DIR

"""
WRITE YOUR CODE BELOW
"""


def give_haptic_feedback(touch_ratio):
    if 0.0 < touch_ratio < 0.5:
        print("Vibrating once...")
    elif 0.5 <= touch_ratio <= 2.0:
        print("Vibrating twice...")
    else:
        print("Vibrating thrice...")


def register_touch(touch_type, direction, duration, strength):
    if touch_type == SINGLE_TOUCH:
        print("Registering single touch...")
    elif touch_type == DOUBLE_TAP:
        print("Registering double tap...")
    elif touch_type == SWIPE:
        print("Registering swipe...")

        if direction == UP:
            print("Exiting app...")
        elif direction == LEFT or direction == RIGHT:
            print("Changing page...")
        elif direction == DOWN:
            print("Scrolling up...")
    else:
        print("Registering hold...")
        touch_ratio = strength / duration
        give_haptic_feedback(touch_ratio)


register_touch(HOLD, NO_DIRECTION, 3, 1.0)




def main():
    pass
