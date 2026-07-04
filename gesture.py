import math

def fingers_up(hand):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand.landmark[4].x < hand.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Index, Middle, Ring, Pinky
    for tip in tips[1:]:
        if hand.landmark[tip].y < hand.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def detect_gesture(hand):
    fingers = fingers_up(hand)

    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"

    elif fingers == [1, 1, 1, 1, 1]:
        return "PALM"

    elif fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"

    return "UNKNOWN"