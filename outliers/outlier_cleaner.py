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
    error = []
    ### your code goes here
    l = len(net_worths)*0.9
    
    for i in range(len(ages)):
        k = abs(net_worths[i]-predictions[i])
        error.append((ages[i],net_worths[i],k))
    print(error)
    error = sorted(error, key=lambda x: x[2])
    #print(error)
    for j in range(int(l)):
         cleaned_data.append(error[j])
    print(cleaned_data)
    return cleaned_data 

