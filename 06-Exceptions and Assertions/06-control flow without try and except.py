def getRatios(vect1,vect2):     # input takes in 2 lists
    ratios = []         # defined an empty list
    if len(vect1) != len(vect2):        # to check if the lenght of both lists match or not
        raise ValueError("getRatios called with bad arguments")
    for index in range(len(vect1)):     # if the length match then a for loop initiated with 'index' goes over the range for the length of the list
        vect1elem = vect1[index]        # we specify variables to take the value of the elements in the list
        vect2elem = vect2[index]
        if (type(vect1elem) not in (int, float)) or (type(vect2elem) not in (int, float)):      # if the type is not int or float then we need to raise an error
            raise ValueError("getRatios called with bad arguments")
        elif vect2elem == 0.0:      # since we'll be calculating vect1elem / vect2elem so if the denominator comes out as 0 then it returns 'nan'
            ratios.append(float('nan'))
        else:       # we perform the operation
            ratios.append(vect1elem/vect2elem)
    return ratios

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
print(getRatios(l1,l2))