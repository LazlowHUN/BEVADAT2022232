#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

def contains_odd(input_list):
    contains = False
    for i in input_list:
        if i % 2 == 1:
            contains = True
    return contains


#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

def is_odd(input_list):
    result = []
    for i in input_list:
        if i % 2 == 0:
            result.append(False)
        else:
            result.append(True)
    return result


#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

def element_wise_sum(input_list_1, input_list_2):
    result = []
    for i in range(len(input_list_1)):
        result.append(input_list_1[i] + input_list_2[i])
    return result


#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict
     
def dict_to_list(input_dict):
    result = []
    for key, value in input_dict.items():
        result.append(tuple([key,value]))
    return result