
def countsun():

    s = "amol is here amol is there amol is good"
    start = count = 0
    while True:
        start = s.find("amol", start) + 1
        if start > 0:
            count = count + 1
        else:
            return count

cnt = countsun()
print(cnt)
