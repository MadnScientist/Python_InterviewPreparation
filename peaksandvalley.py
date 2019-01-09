def getPeaksAndValley(given):
    given.insert(0,0)
    given.insert(len(given),0)
    i = 1
    while i < len(given)-1:
        if given[i] > given[i -1] and given[i] > given[i + 1]:
            print("Peak exists")

        elif given[i] > given[i -1] and given[i] <= given[i + 1]:
            t = given[i]
            given[i] = given[i + 1]
            given[i + 1] = t
        elif given[i] <= given[i -1] and given[i] < given[i + 1]:
            t = given[i] 
            given[i] = max(given[i -1], given[i + 1])
            if given[i] == given[i -1]:
                given[i -1] = t
            else:
                given[i + 1] = t
        
        print("updated: peak", given)
        i = i + 2
    return given[1:len(given) - 1]


given = [5,3,1,2,3]
getPeaksAndValley(given)