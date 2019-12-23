def read_paths():
    with open('03_01_input.txt','r') as f:
        paths = [line.strip().split(',') for line in f]
    return paths

def increment_xy(data):
    wPlot = []
    xy = [0,0]
    for i in data:
        for _ in range(int(i[1:])):
            wPlot.append(tuple(xy[:]))
            if i[0] == 'U':
                xy[1] += 1
            elif i[0] == 'D':
                xy[1] -= 1
            elif i[0] == 'L':
                xy[0] -= 1
            elif i[0] == 'R':
                xy[0] += 1
            else:
                print('input error')
                break
    
    
    return wPlot

def walk_through(intercept):
    paths = read_paths()
    path1 = increment_xy(paths[0])
    path2 = increment_xy(paths[1])
    steps = 0
    for point in path1:
        if point == intercept:
            
            for point2 in path2:
                if point2 == intercept:
                    
                    return steps
                else:  
                    steps +=1       
        else:
            steps +=1

        
        


    

def navigate(paths):
    w1Plot = increment_xy(paths[0])
    w2Plot = increment_xy(paths[1])
    
    intercepts = list(set(w1Plot).intersection(set(w2Plot)))

    
    
    sums = map(walk_through,intercepts)

    s = sorted(sums)
    print("Part 2:", s[1])

    abs_intercepts = [(abs(i[0]), abs(i[1])) for i in intercepts]

    print("Part 1:", min([sum(i) for i in abs_intercepts if sum(i) > 0]))

navigate(read_paths())