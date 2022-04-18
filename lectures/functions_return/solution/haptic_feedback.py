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


def give_haptic_feedback(touch_ratio):
    if 0.0 < touch_ratio < 0.5:
        print("Vibrating once...")
    elif 0.5 <= touch_ratio <= 2:
        print("Vibrating twice...")
    else:
        print("Vibrating thrice....")


def register_touch(touch_type, direction=NO_DIRECTION, duration=0.1, strength=0.1):
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

        touch_ratio = round(strength / duration, 1)
        give_haptic_feedback(touch_ratio)


def main():
    user_hold_duration = 0.1
    user_touch_strength = 0.1
    user_direction = NO_DIRECTION

    user_touch_type = input("What type of touch did the user perform? [single/double/swipe/hold] ")
    user_touch_strength = float(input("How strong was the user's touch? [0.0 to 1.0] "))

    if user_touch_type == "swipe":
        user_direction = input("In what direction did the user swipe? ")

    if user_touch_type == "hold":
        user_hold_duration = float(input("For how long did the user hold the touch? "))

    if user_touch_type == "single":
        touch_type = SINGLE_TOUCH
    elif user_touch_type == "double":
        touch_type = DOUBLE_TAP
    elif user_touch_type == "swipe":
        touch_type = SWIPE
    else:
        touch_type = HOLD

    if user_direction == "up":
        direction = UP
    elif user_direction == "down":
        direction = DOWN
    elif user_direction == "left":
        direction = LEFT
    elif user_direction == "right":
        direction = RIGHT
    else:
        direction = NO_DIRECTION

    register_touch(touch_type, direction, user_hold_duration, user_touch_strength)


register_touch(HOLD)
register_touch(HOLD, NO_DIRECTION)
register_touch(HOLD, NO_DIRECTION, 0.2)
register_touch(HOLD, NO_DIRECTION, 0.2, 0.2)
