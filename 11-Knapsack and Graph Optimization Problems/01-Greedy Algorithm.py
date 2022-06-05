class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<'+self.name+', '+str(self.value)+', '+str(self.weight)+'>'
        return result
    

def value(item):
    return item.getValue()
def weightInverse(item):
    return 1/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()


#################### Implementation of Greedy Algorithm ####################

'''
greedy algo -> The arguments to be passed are items, maxWeight and keyFunction
                - sorting of items list in itemsCopy depending on keyFunction(value or weightInverse or density)
                - initialise totalWeight and totalValue = 0.0
                - for loop in the range of length of itemsCopy
                    - if the totalWeight + weight of Item <= maxWeight
                        - we append it to result list
                        - we now update the totalWeight = totalWeight + the Item Weight
                        - we also update the totalValue = totalValue + the Item Value
                - once done we return the result list and totalValue
'''

def greedy(items, maxWeight, keyFunction):
    '''
    Assumes Items a list, maxWeight>=0, keyFunction maps elements of Items to Numbers
    '''
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0,0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return(result, totalValue)

#################### Using Greedy Algorithm to Choose items ####################

'''
buildItems -> here we specify the items, values and their respective weights
            Items is a list which comprises of items in the format <'item_name',value,weight>
'''

def buildItems():
    names = ['clock','painting','radio','vase','book','computer']
    values = [170,90,20,50,10,200]                        
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items

'''
testGreedy -> the arguments are items, maxweight and keyFunction which is passed on to 'greedy algorithm'
             Here taken is the result list and val is the totalValue obtained from the result list.
'''

def testGreedy(items, maxWeight, keyFunction):
    taken, val=greedy(items, maxWeight, keyFunction)
    print('Total value of items take is',val)
    for item in taken:
        print(' ',item)

'''
testGreedys -> initialises the building of items and then passes the arguments to the function 'testGreedy'
                here, keyfunction is passed as value, weightInverse and density that determines the sorting of lists.
'''

def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size',maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size',maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by density to fill knapsack of size',maxWeight)
    testGreedy(items, maxWeight, density)

testGreedys()

'''
OUTPUT

Use greedy by value to fill knapsack of size 20
Total value of items take is 200.0
  <computer, 200, 20>

Use greedy by weight to fill knapsack of size 20   
Total value of items take is 170.0
  <book, 10, 1>
  <vase, 50, 2>
  <radio, 20, 4>
  <painting, 90, 9>

Use greedy by density to fill knapsack of size 20  
Total value of items take is 250.0
  <vase, 50, 2>
  <clock, 170, 10>
  <book, 10, 1>
  <radio, 20, 4>
'''