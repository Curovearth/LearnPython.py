def getRatios(vect1, vect2):
    '''
    Assumes vect1 and vect2 are equal length lists of numbers
    Returns a list containing the meaningful values of vect1[i]/vect2[i]
    '''

    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('getRatios called with bad arguments.')

    return ratios

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
print(getRatios(l1,l2))