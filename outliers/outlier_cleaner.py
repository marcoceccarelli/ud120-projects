#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    totToRemove = int(len(predictions) * 0.1)
    
    for index in range(len(predictions)):
        data = (ages[index], net_worths[index], predictions[index] - net_worths[index])
        cleaned_data.append(data)
    
    from operator import itemgetter 
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2]) 

    for i in range(0,totToRemove - 1):
        cleaned_data.pop()

    return cleaned_data

