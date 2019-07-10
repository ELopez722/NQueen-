
def print_result(result):
    for path in range(len(result)):
        print()
        print("Solution #", path+1,sep = "")
        for pos in result[path]:
            print("(", pos[0], ",", pos[1], ")" ,sep = "", end = "")
        print()

def queenCollision(positions, newPos, bSize):
    if len(positions) != 0:
        Qloc = {}
        #colission in the same row/col
        for pos in positions:
            if pos[0] == newPos[0] or pos[1] == newPos[1]:
                return True
            Qloc[tuple(pos)] = ""
            
        #colission for diagnol
        #up/right
        temp = newPos + []
        while temp[0]-1 > -1 and temp[1]+1 < bSize:
            temp[0] += -1
            temp[1] += 1
            if tuple(temp) in Qloc:
                return True
        #down/right
        temp = newPos + []
        while temp[0]+1 < bSize and temp[1]+1 < bSize:
            temp[0] += 1
            temp[1] += 1
            if tuple(temp) in Qloc:
                return True
        #down/left
        temp = newPos + []
        while temp[0]+1 < bSize and temp[1]-1 > -1:
            temp[0] += 1
            temp[1] += -1
            if tuple(temp) in Qloc:
                return True
        #up/left
        temp = newPos + []
        while temp[0]-1 > -1 and temp[1]-1 > -1:
            temp[0] += -1
            temp[1] += -1
            if tuple(temp) in Qloc:
                return True             
    return False

def nQueenProblem(n,solutionAmount):
    solutions = []
    queenPlacment = []
    curPos = [0,0]
    print("Please wait, solving.....\n")
    for i in range(solutionAmount):
        while len(queenPlacment) != n:
            #print(curPos, "in main")
            if not queenCollision(queenPlacment, curPos, n):
                queenPlacment.append(curPos+[])
                #print(queenPlacment)
                if len(queenPlacment) == n:
                    break;
                if curPos[0]+1 >= n:
                    if len(queenPlacment) == 0:
                        break
                    curPos = queenPlacment.pop()+[]
                    if curPos[1]+1 >= n:
                        if len(queenPlacment) == 0:
                            break
                        curPos = queenPlacment.pop()+[]
                    curPos[1] += 1   
                else:    
                    curPos[0] += 1
                    curPos[1] = 0
                    
            elif curPos[1]+1 >= n:
                if len(queenPlacment) == 0:
                    break
                curPos = queenPlacment.pop()+[]
                if curPos[1]+1 >= n:
                    if len(queenPlacment) == 0:
                        break
                    curPos = queenPlacment.pop()+[]
                    curPos[1] += 1
                else:
                    curPos[1] += 1
            else:
                curPos[1] += 1
            
        if len(queenPlacment) == 0 and len(solutions) == 0:
            print("No solution")
            return solutions
        if len(queenPlacment) == 0:
            print("Too many solutions entered")
            print(len(solutions), "is the maximum amount of solutions for",n,"Queens")
            return solutions
        solutions.append(queenPlacment+[])
        temp = queenPlacment.pop()+[]
        if temp[1]+1 == n:
            temp = queenPlacment.pop()+[]
            temp[1] += 1
        else:
            temp[1] += 1
        curPos = temp
    print("Solved")
    return solutions

x = True
while x:
    n = int(input("Please enter the NQueen problem you would like to solve: "))
    amount = int(input("Please enter the amount of solutions you would like to see: "))

    result = nQueenProblem(n,amount)

    print_result(result)

    response = input("\nif you would like to quit press \"q\", or press enter to continue")
    print()
    if response == 'q':
        x = False
        
print("Good Bye!")
    
