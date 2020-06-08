from Helper.statBuilder import isWithinPlot, withinValues

if __name__ == '__main__':
    print(withinValues(1, [-1, 1]))
    print(isWithinPlot([0,1], [[-2,2], [-2,2]]))