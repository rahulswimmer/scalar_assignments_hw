def insert(intervals, newInterval):
    for i in range(len(intervals)):
        if not(newInterval[0] > intervals[i][1] or intervals[i][0] > newInterval[1]):
            print(intervals[i])

intervals = [[1,3],[4,5],[6,9]]
newInterval = [2,5]
insert(intervals,newInterval)