Code = "0 3 4 2 6 3 10 2 12 3 16 2 18 2 20 2 22 2 24 3 28 2 30 3 34 2 36 3 40 2 42 2 44 2 46 2 48 3 52 2 54 3 58 2 60 3 64 2 66 2 "
lent = 0
isTime = True
bcode = ""
Maintime = 0
Substring = ""
breaktime = 0.04

# 0.04


def Encode():
    global Maintime
    global bcode
    global isTime
    global Substring
    if isTime == True:
        isTime = False
        codetime = int(Substring)
        diftime = codetime-Maintime
        Maintime = codetime
        i = 0
        while i < diftime:
            bcode = bcode+'0'
            i = i+0.04
    else:
        isTime = True
        codetime_interval = int(Substring)
        Maintime = Maintime+codetime_interval
        j = 0
        while j < codetime_interval:
            bcode = bcode+'1'
            j = j+0.04
        bcode = bcode+'0'
    Substring=""





while(lent < len(Code)):
    if Code[lent] == " ":
     

        Encode()
    else:
        Substring = Substring+Code[lent]

    lent = lent+1

print(bcode)