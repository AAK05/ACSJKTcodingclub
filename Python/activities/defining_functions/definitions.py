def fibonacci(terms):
    sequence = [1,1] #Initialize first 2 terms in the sequence, which are default
    if terms == 0: #Special case if n=0, return empty list
        return([])
    elif terms == 1: #Special case if n=1, return [1]
        return([1])
    else:
        for i in range(terms - 2):
            sequence.append(sequence[-1] + sequence[-2]) #Appends sum of last and second last
        return(sequence) #returns resulting sequence