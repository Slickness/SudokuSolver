#!/usr/bin/env python
import time

def getPuzzle():
##    main = "872516349461937258359428761736295184594871632218643597925164873647382915183759426"
##    mask = "010110111011011111101100111011110100101111101001011110111001101111110110111011010"
##    puzzle = []
##    for i in range (81):
##        if mask[i] == "0":
##            puzzle.append(main[i])
##        else:
##            puzzle.append("0")
    puzzle = ["8","0","0","0","0","0","0","0","0","0","0","3","6","0","0","0","0","0","0","7","0","0","9","0","2","0","0","0","5","0","0","0","7","0","0","0","0","0","0","0","4","5","7","0","0","0","0","0","1","0","0","0","3","0","0","0","1","0","0","0","0","6","8","0","0","8","5","0","0","0","1","0","0","9","0","0","0","0","4","0","0"]
    #print len(puzzle)    
    return puzzle

def displayPuzzle(puzzle):
    line = ""
    x = 0
    y = 1
    for item in range(81):
        x =  x + 1
        if len(line)%11 == 0:
            
            y = y + 1
            if y > 3:
                if y%3 == 0:
                    print "---+---+---"
            
            print (line)
            x = 0
            line = ""
        if x == 3:
            line = line + "|"
        if x == 6:
            line = line + "|"
        line = line + str(puzzle[item])
    print line
def Check(puzzle,loc,value):
    a = [0,1,2,9,10,11,18,19,20]
    b = [3,4,5,12,13,14,21,22,23]
    c = [6,7,8,15,16,17,24,25,26]
    d = [27,28,29,36,37,38,45,46,47]
    e = [30,31,32,39,40,41,48,49,50]
    f = [33,34,35,42,43,44,51,52,53]
    g = [54,55,56,63,64,65,72,73,74]
    h = [57,58,59,66,67,68,75,76,77]
    i = [60,61,62,69,70,71,78,79,80]
    grids = [a,b,c,d,e,f,g,h,i]
    #check grids
    for x in grids:
        for y in x:
            if y == loc:
                for y in x:
                    #print puzzle[y]
                    #print value
                    if puzzle[y] == value:
                        return False
                        break
    if loc/9 == 0:
        cells = [0,1,2,3,4,5,6,7,8]
    if loc/9 ==1:
        cells = [9,10,11,12,13,14,15,16,17]    
    if loc/9 ==2:
        cells = [18,19,20,21,22,23,24,25,26]
    if loc/9 ==3:
        cells = [27,28,29,30,31,32,33,34,35]
    if loc/9 ==4:
        cells = [36,37,38,39,40,41,42,43,44]
    if loc/9 ==5:
        cells = [45,46,47,48,49,50,51,52,53]
    if loc/9 ==6:
        cells = [54,55,56,57,58,59,60,61,62]
    if loc/9==7:
        cells = [63,64,65,66,67,68,69,70,71]
    if loc/9 ==8:
        cells = [72,73,74,75,76,77,78,79,80]
    for x in cells:
        if puzzle[x]== value:
            return False
            break
    for x in range(len(puzzle)):
        if loc%9 == x%9:
            if puzzle[x] == value:
                return False
                break
    return True
def Solve2(puzzle):
    #load empty values
    NeedSolve = []
    for x in range(81):
        if puzzle[x] == "0":
            NeedSolve.append([x,"0"])
    #print len(NeedSolve)
    for x in NeedSolve:
        #print x

        ToSolve = 0
        values = ["1","2","3","4","5","6","7","8","9","10"]
        while True:
        
            ToCheck = NeedSolve[ToSolve]
        #print ToCheck
            loc = ToCheck[0]
            value=ToCheck[1]
        
            start = value   
            for x in range(int(value),len(values)):
                #if x ==int(value) or value == "0":
                    #print x
                #print values[x]
                value = values[x]
                if value == "10":
                    ToCheck[0] = loc
                    ToCheck[1] = "0"
                    NeedSolve[ToSolve] = ToCheck

                    ToSolve = ToSolve -1
                    
                    #print ToSolve
                    ToCheck = NeedSolve[ToSolve]
                    loc = ToCheck[0]
                    value=ToCheck[1]
                    
                    puzzle[loc] = "0"
                    break
                if Check(puzzle,loc,value):
                    puzzle[loc] = value
                    ToCheck = [loc,value]
                    NeedSolve[ToSolve]=ToCheck
                    #print ToCheck
                    #displayPuzzle(puzzle)
                    ToSolve = ToSolve + 1
                    #displayPuzzle(puzzle)
                    counter = 0
                    for x in range(81):
                        if puzzle[x] == "0":
                            counter = counter + 1
                    if counter == 0:
                        return puzzle
                    break
                #print values[x] + " fail"  
            if ToSolve == len(NeedSolve)-1:
                break
            

def Solve(puzzle):
    #load empty values
    NeedSolve = []
    for x in range(81):
        if puzzle[x] == "0":
            NeedSolve.append([x,"0"])
    print len(NeedSolve)
    z = 0
    while z < (len(NeedSolve)-1):
        out = NeedSolve[z]
        value = out[1]
        loc = out[0]
        values = ["1","2","3","4","5","6","7","8","9","10"]
        print "trying " + str(out[0]) + " " + str(out[1])
        for a in range(len(values)):
            if values[a] == "10":
                
                z = z - 1
                out = NeedSolve[z]
                value = out[1]
                loc = out[0]
                puzzle[loc] = "0"
                
                break
            else:
                continue
            if values[a-1] == value or value == "0":
                value = values[a]
                #if values[a] = "10":
                #    z = z - 1
                #    out = NeedSolve[z]
                #    value = out[1]
                #    loc = out[0]
                #    puzzle[loc] = "0"
                #    break
                if Check(puzzle,loc,value):
                    puzzle[loc] = value
                        #displayPuzzle(puzzle)
                    #print out
                    out = [loc,value]
                    NeedSolve[z] = out
                    z = z + 1
                    displayPuzzle(puzzle)
                    
                    break
                else:
                    continue
                break
            else:
                continue
        else:
            continue
        #break
        #break
                #elif values[a] == "9":
                #    z = z - 1
                #    out = NeedSolve[z]
                #    value = out[1]
                #    loc = out[0]
                    #puzzle[loc] = "0"
                    #oldout = NeedSolve[z]
                    #value = oldout[1]
                    #break               
        
        #print z
    
    #x = 61
    #for grid in grids:
    #    for y in grid:
    #        if y == x:
    #            print grid
if __name__ == '__main__':
    start = time.time()
    puzzle = getPuzzle()
    displayPuzzle(puzzle)
    if Solve2(puzzle):
        displayPuzzle(puzzle)
    end = time.time()
    elapsed = end - start
    print elapsed
