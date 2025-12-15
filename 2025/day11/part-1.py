from utils.io import read_input_lines as read_data

connections = {}
for x in read_data():
    devices, connected_devices = x.split(": ")
    connections[devices] = connected_devices.split(" ")


def path(device):
    if device == "out":
        return 1

    return sum(path(connected_device) for connected_device in connections[device])


print(path("you"))
