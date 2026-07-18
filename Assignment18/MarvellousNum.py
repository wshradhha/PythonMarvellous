def AdditionOfElements(list1):
    sum = 0
    for i in range(len(list1)):
        is_prime = True
        for j in range(2,list1[i]):
            if(list1[i] % j==0):
                is_prime = False
        if(is_prime):
            sum = sum + list1[i]
    return sum

