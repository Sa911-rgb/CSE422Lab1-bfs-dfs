filename = input("Enter the file name: ")
#Initialize the matrix/2d list
l = []

##Value initialization for task1
#s = []
d = dict()
#Initialize direction vectors for 
#traversing diagonally, vertically and horizontally
rl1 = [-1,-1,-1,0,1,1,1,0]
cl1 = [-1,0,1,1,1,0,-1,-1]

##Value initialization for task2
#q = []
attacked = []
#Initialize direction vectors for 
#traversing vertically and horizontally
rl2 = [-1, 0, 1, 0]
cl2 = [0, 1, 0, -1]

#Make boolean 2d list to keep track of the visited cells
def vis(r, c):
    return [[False for i in range(c)] for j in range(r)]

#To check if the position is valid, unvisited and inside the matrix or not
def isValid(r, c, v):
    if (r<0 or c<0 or r>=row or c>=col):
        return False
    if (v[r][c]):
        return False
    return True

#Check the adjacent cells that are Y
def checkY(i, j, reg, v):
    if(isValid(i,j,v)):
        if l[i][j] == 'Y':
            dfs(i, j, reg, v)

#Check the adjacent cells that are H
def checkH(i, j, v):
    if (isValid(i, j, v)):
        if l[i][j] == 'H':
            #To keep track of the attacked humans
            if [i, j] in attacked:
                return False
            return True
    return False

def dfs(x, y, reg, v):
    #Increment the value of an existing region in the dictionary
    #and if there's no such region, make one with a value 1
    d[reg] = d.get(reg, 0) + 1
    
    #s.append([x, y])
    v[x][y] = True
    
    #Check for adjacent cells diagonally, vertically and horizontally
    #and recurse the whole method
    for i in range(8):
        adx = x + rl1[i]
        ady = y + cl1[i]
        checkY(adx, ady, reg, v)
    
    #s.remove(s[len(s)-1])

def bfs(x, y, v):
    #q.append([x, y])
    v[x][y] = True
    
    #Counter of adjacent cells
    ad = 0
    #Check for adjacent cells vertically and horizontally
    for i in range(4):
        adx = x + rl2[i]
        ady = y + cl2[i]
        if(checkH(adx, ady, v)):
            attacked.append([adx, ady])
            ad+=1
    if(ad>0):
        return True
    else:
        return False

#To turn the attacked humans into hosts and spawn new aliens
def spawn(v):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(v[i][j]):
                continue
            if [i, j] in attacked:
                l[i][j] = 'A'

def task1():
    max = None
    v = vis(row, col)
    
    #Traverse through each element of the matrix
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 'Y':
                if(isValid(i, j, v)):
                    reg = "Region"+str(i)+str(j)
                    dfs(i, j, reg, v)
    #print(d)
    #Find the value of the region with maximum Y
    for vl in d.values():
        if max is None or vl > max:
            max = vl
    print(max)

def task2():
    #Counter of the minimum time needed and total attacked humans
    time, attack = (0, 0)
    
    #initialize the counter for attack rounds
    c = 1
    v = vis(row, col)
    while(c > 0):
        c = 0
        
        #Traverse through each element of the matrix
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] == 'A':
                    if(isValid(i, j, v)):
                        if(bfs(i, j, v)):
                            c+=1
        attack = len(attacked)
        if(c>0):
            time += 1
            spawn(v)
    
    #print(l)
    print("Time: "+str(time)+" minutes")
    #print(attack)
    
    #To check how many survived
    for i in l:
        if 'H' in i:
            c+=1
    
    if (c>0):
        print(str(c)+" survived")
    else:
        print("No one survived")

#Read the input file and make a matrix/2d list from the contents
with open(filename) as f:
    first = f.readline().rstrip()
    
    #Check if the first line is a number or not
    if (first.isdigit()):
        row = int(first)
        count = 1
        for line in f:
            if(count>1):
                l.append(line.split())
            else:
                col = int(line)
            count+=1
        task2()
    else:
        l.append(first.split())
        for line in f:
            l.append(line.split())
        row = len(l)
        col = len(l[0])
        task1()
#print(l)