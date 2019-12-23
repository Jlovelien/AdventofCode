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

def navigate(paths):
    print(paths)
    w1Plot = increment_xy(paths[0])
    w2Plot = increment_xy(paths[1])
    intercepts = list(set(w1Plot).intersection(set(w2Plot)))
    abs_intercepts = [(abs(i[0]), abs(i[1])) for i in intercepts]

    print(min([sum(i) for i in abs_intercepts if sum(i) > 0]))

navigate(read_paths())