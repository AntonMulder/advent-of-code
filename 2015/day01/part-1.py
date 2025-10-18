data = open("input").read()

print(abs(data.count("(") - data.count(")")))
