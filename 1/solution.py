import math  

def calculateDistance(x1,y1,x2,y2):  
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return distance  

def hyperloopTime(x1,y1,x2,y2):
    return calculateDistance(x1,y1,x2,y2) / 250.0 + 200.0


if __name__ == '__main__':
    with open('level1-4.txt', 'r') as in_file:
        x1,x2,y1,y2 = [0,0,0,0]
        n_locations = int(in_file.readline())
        locations = []
        for _ in range(n_locations):
            location = dict()
            name, x, y = next(in_file).split()
            location[name] = tuple(map(int, [x,y]))
            locations.append(location)

        from_, to_ = next(in_file).split()
        for location in locations:
            for key, value in location.items():
                if(key == from_):
                    x1,y1 = value[0], value[1]
                if(key == to_):
                    x2,y2 = value[0], value[1]
        print(round(hyperloopTime(x1,y1,x2,y2)))

		