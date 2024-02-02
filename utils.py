# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values:list)-> int|float:
    """
    A function that receives a list and returns the sum of the values in that
    sequence

    arguments :
        ---- values : list of numerical values
    """
    total = 0    
    for numbers in values:
        if not isinstance(numbers, (int,float)):
            raise ValueError(" wrong value")
        total += numbers
    return total

#print(sumvalues([1,2,3,4,5,4,7,8,9]))

def maxvalue(values:list)-> int:
    """
    A function that receives a list and returns the index of the maximum
    value in that sequence.

    arguments :
        ---- values : list of numerical values
    """ 
    ind = 0
    valuen =0
    for i in range(len(values)):
        if not isinstance(values[i], (int,float)):
            raise ValueError(" wrong value")
        if values[i] < valuen:
            valuen = values[i]

    for k in range(len(values)):
        if values[k] > valuen:
            valuen = values[k]
            ind =k
    return ind

#print(maxvalue([-9,-230,-46,4,-30,-780,-1,-9,-10]))


def minvalue(values:list)->int:
    """
    A function that receives a list and returns the index of the minimum
    value in that sequence

    arguments :
        ---- values : list of numerical values
    """    
    ind = 0
    valuen =0
    for i in range(len(values)):
        if not isinstance(values[i], (int,float)):
            raise ValueError(" wrong value")
        if values[i] > valuen:
            valuen = values[i]

    for k in range(len(values)):
        if values[k] < valuen:
            valuen = values[k]
            ind =k
    return ind

#print(minvalue([-9,-230,-46,4,-30,-78,-1,-9,-10]))


def meannvalue(values: list)->int|float:
    """
    A function that receives a list and returns the arithmetic mean value
    of that list. the mean values is found by suming all elements exeept the last one and
    dividing the sum by the size of the list

    arguments :
        ---- values : list of numerical values
    """
    result =0    
    for i in range(len(values)):
        if not isinstance(values[i], (int,float)):
            raise ValueError(" wrong value")
        result += values[i]
    return result / len(values)




def countvalue(values,x)->int:
    """
    A function that receives a list values and a value x and returns
    the number of occurrences of the value x in the list of values.

    arguments :
        ---- values : list of numerical values
        ---- x : number to check occurence from
    """
    occurence = 0
    if x not in values:
        return occurence
    for element in values:
        if element == x:
            occurence += 1
    return occurence

#print(countvalue([-9,-230,-46,-9,-30,-78,-1,-9,-10],-9))
        


