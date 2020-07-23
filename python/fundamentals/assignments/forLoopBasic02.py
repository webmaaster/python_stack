def biggie_size(num_list):
    '''
        Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
        Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
    '''

    modified_num_list = []

    for num in num_list:
        if num >= 0:
            modified_num_list.append("big")

        else:
            modified_num_list.append(num)

    return modified_num_list

result = biggie_size([-1, 3, 5, -5])
#print(result)

def count_positives(num_list):
    '''
        Count Positives 
            - Given a list of numbers, create a function to replace the last value with the number of positive values. 
            (Note that zero is not considered to be a positive number).
        Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
        Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
    '''

    num_of_positives = 0

    for num in num_list:
        if num > 0:
            num_of_positives += 1

    num_list[-1] = num_of_positives
    return num_list

result = count_positives([-1,1,1,1])
#print(result)

result = count_positives([1,6,-4,-2,-7,-2])
#print(result)


def sum_total(num_list):
    '''
        Sum Total 
            - Create a function that takes a list and returns the sum of all the values in the list.

        Example: sum_total([1,2,3,4]) should return 10
        Example: sum_total([6,3,-2]) should return 7
    '''

    total = 0
    for num in num_list:
        total += num

    return total

result = sum_total([1,2,3,4])
#print(result)

result = sum_total([6, 3, -2])
#print(result) 

def average(num_list):
    '''
        Average 
            - Create a function that takes a list and returns the average of all the values.x
        
        Example: average([1,2,3,4]) should return 2.5
    '''

    total = 0
    num_of_values = 0

    for num in num_list:
        total += num
        num_of_values += 1

    avg = total / num_of_values
    return avg

result = average([1,2,3,4])
#print(result)


def length(num_list):
    '''
        Length 
            - Create a function that takes a list and returns the length of the list.
        
        Example: length([37,2,1,-9]) should return 4
        Example: length([]) should return 0
    '''

    num_of_values = 0

    for num in num_list:
        num_of_values += 1

    return num_of_values


result = length([37, 2, 1, -9])
#print(result)

result = length([])
#print(result)


def minimum(num_list):
    '''
        Minimum 
            - Create a function that takes a list of numbers and returns the minimum value in the list.
            If the list is empty, have the function return False.
        
        Example: minimum([37,2,1,-9]) should return -9
        Example: minimum([]) should return False
    '''
    if not num_list:
        return False

    smallest = num_list[0]

    for num in num_list:
        if num < smallest:
            smallest = num

    return smallest

result = minimum([37,2,1,-9])
#print(result)

result = minimum([])
#print(result)

def maximum(num_list):
    '''
        Maximum 
            - Create a function that takes a list and returns the maximum value in the list. 
            If the list is empty, have the function return False.
        
        Example: maximum([37,2,1,-9]) should return 37
        Example: maximum([]) should return False
    '''
    if not num_list:
        return False

    biggest = num_list[0]

    for num in num_list:
        if num > biggest:
            biggest = num

    return biggest

result = maximum([37,2,1,-9])
#print(result)

result = maximum([])
#print(result)


def ultimate_analysis(num_list):
    '''
        Ultimate Analysis 
         - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
        
        Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
    '''

    return {
        'sumTotal': sum_total(num_list),
        'average': average(num_list),
        'minimum': minimum(num_list),
        'maximum': maximum(num_list),
        'length': length(num_list)
    }

result = ultimate_analysis([37,2,1,-9])
#print(result)

def reverse_list(num_list):
    '''
        Reverse List
            - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
            (This challenge is known to appear during basic technical interviews.)
        
        Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
    '''

    return num_list[::-1]


result = reverse_list([37, 2, 1, -9])
print(result)
