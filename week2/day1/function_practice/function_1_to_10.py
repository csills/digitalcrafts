def oneToTen(start, end):
    for x in range(start, end):
        print (x)

start = int(raw_input("Start?"))
end = int(raw_input("End?"))

oneToTen(start, end + 1)