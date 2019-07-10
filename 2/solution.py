import math  

def calculateDistance(x1,y1,x2,y2):  
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return distance  

def hyperloopTime(x1,y1,x2,y2):
    return calculateDistance(x1,y1,x2,y2) / 250.0 + 200.0

def drivingTime(x1,y1,x2,y2):
    return (calculateDistance(x1,y1,x2,y2)) / 15.0

def walkingTime(x1,y1,x2,y2):
    return (calculateDistance(x1,y1,x2,y2)) / 1.3

if __name__ == '__main__':
    with open('level2-4.txt', 'r') as in_file:
        x1,x2,y1,y2 = [0,0,0,0]
        n_locations = int(in_file.readline())
        locations = []
        for _ in range(n_locations):
            location = dict()
            name, x, y = next(in_file).split()
            location[name] = tuple(map(int, [x,y]))
            locations.append(location)

        journeyStart, journeyEnd = next(in_file).split()
        hyperloop1, hyperloop2 = next(in_file).split()

        for location in locations:
            for key, value in location.items():
                if(key == journeyStart):
                    x1,y1 = value[0], value[1]
                if(key == journeyEnd):
                    x2,y2 = value[0], value[1]
                if(key == hyperloop1):
                    x3,y3 = value[0], value[1]
                if(key == hyperloop2):
                    x4,y4 = value[0], value[1]

        # distance1 = calculateDistance(journeyStart, hyperloop1)
        distance1 = calculateDistance(x1,y1,x3,y3)
        # distance2 = calculateDistance(journeyStart, hyperloop2)
        distance2 = calculateDistance(x1,y1,x4,y4)
        if(distance1 < distance2):
            # total = drivingTime(journeyStart, hyperloop1) + hyperloopTime() + walkingTime(hyperloop2, journeyEnd) 
            total = drivingTime(x1,y1,x3,y3) + hyperloopTime(x3,y3,x4,y4) + drivingTime(x4,y4,x2,y2) 
        else:
            # total = drivingTime(journeyStart, hyperloop2) + hyperloopTime() + walkingTime(hyperloop1, journeyEnd)
            total = drivingTime(x1,y1,x4,y4) + hyperloopTime(x3,y3,x4,y4) + drivingTime(x3,y3,x2,y2) 
        print(round(total))

		