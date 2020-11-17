from math import floor


def get_distance(time, speed, speed_seconds, rest_seconds, **kwargs):
    speed = int(speed)
    speed_seconds = int(speed_seconds)

    period_seconds = speed_seconds + int(rest_seconds)
    periods = floor(time / period_seconds)

    # Distance for full periods
    distance = periods * speed_seconds * speed

    remaining_seconds = time - (periods * period_seconds)
    return distance + speed * min(remaining_seconds, speed_seconds)
