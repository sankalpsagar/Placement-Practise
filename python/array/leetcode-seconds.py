def minTimeToVisitAllPoints(points):
    seconds = 0
    for i in range(len(points)-1):
        if points[i][0] == points[i+1][0]:
            seconds += abs(points[i+1][1] - points[i][1])
        
        elif points[i][1] == points[i+1][1]:
            seconds += abs(points[i+1][0] - points[i][0])
            
        else:
            seconds += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
    
    return seconds

res = minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(res)
                