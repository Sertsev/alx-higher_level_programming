#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sume = 0
    mule = 0
    for i in range(len(my_list)):
        mule += my_list[i][0] * my_list[i][1]
        sume += my_list[i][1]
    return mule/sume
