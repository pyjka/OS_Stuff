def Burov(red,green,cross):
    if len(green) == 1:
        return cross[0]
    for i in range(0,len(green)-1):
        if green[i+1] >= green[i]: # if the next green light is greater than previous
            if (green[i+1]-green[i]) > cross[i]: #if next green light is less than crossing time we have to wait for the red light
                WAITandGO = (green[i+1]-green[i])+red[i+1]
                print 'test1'
                return WAITandGO+(sum(cross[1:]))
        if green[-1]>=green[-2]:
            if (green[-1]- green[-2])<cross[i]:
                WAITandGO2 = (green[-1]-green[-2])+red[-1]+cross[-1]
                print 'test2'
                return WAITandGO2+(sum(cross[1:]))
        else:
            if green[i+1] < green[i]: #if next green light is less than current one,we have to see how long are we waiting for the next green(if we wait at all)
                if red[i] > (green[i+1]-green[i]): #if red light is greater than difference between
                # current green and next one , we see how long we are waiting for the red to finish
                    wait_that_extra_red = red[i]-(green[i+1]-green[i])
                    print 'test3'
                    return wait_that_extra_red+sum(cross[1:])
            if green[-1] < green[-2]:
                if red[-1] > (green[-1]-green[-2]):
                    wait_that_extra_red2 = red[-1]-(green[-1]-green[-2])
                    print 'test4'
                    return wait_that_extra_red2+sum(cross[1:])
