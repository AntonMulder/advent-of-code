from utils.io import read_input_lines as read_data

connections = {}
for x in read_data():
    devices, connected_devices = x.split(": ")
    connections[devices] = connected_devices.split(" ")

cache = {}


def path(device, has_visited_dac=False, has_visited_fft=False):
    if (device, has_visited_dac, has_visited_fft) in cache:
        return cache[(device, has_visited_dac, has_visited_fft)]

    if device == "out":
        return has_visited_dac and has_visited_fft

    has_visited_dac = device == "dac" or has_visited_dac
    has_visited_fft = device == "fft" or has_visited_fft

    value = sum(
        path(connected_device, has_visited_dac, has_visited_fft)
        for connected_device in connections[device]
    )
    cache[(device, device == "dac" or has_visited_dac, has_visited_fft)] = value
    return value


print(path("svr"))
