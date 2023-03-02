#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

def subset(input_list, start_index, end_index):
    return input_list[start_index:end_index]


#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

def every_nth(input_list, step_size):
    return input_list[::step_size]


#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

def unique(input_list):
    return len(input_list) == len(set(input_list))
            

#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

def flatten(input_list):
    result = []
    for i in input_list:
        for j in i:
            result.append(j)
    return result


#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

def merge_lists(*args):
    result = []
    for list in args:
        result = result + list
    return result


#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

def reverse_tuples(input_list):
    result = []
    for i in input_list:
        helper_list = list(i)
        helper = helper_list[0]
        helper_list[0] = helper_list[1]
        helper_list[1] = helper
        result.append(tuple(helper_list))
    return result


#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

def remove_duplicates(input_list):
    helper = set(input_list)
    return list(helper)


#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

def transpose(input_list):
    result = [[0 for j in range(len(input_list))] for i in range(len(input_list[0]))]
    for i in range(len(input_list)):
        for j in range(len(input_list[0])):
            result[j][i] = input_list[i][j]
    return result


#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

def split_into_chunks(input_list, chunk_size):
    result = []

    for i in range(0,len(input_list),chunk_size):
        chunk = input_list[i:i+chunk_size]
        result.append(chunk)
    return result


#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

def merge_dicts(*dict):
    result = {}
    for i in dict:
        result.update(i)
    return result


#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

def by_parity(input_list):
    even = []
    odd = []
    result = {}
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result["even"] = sorted(even)
    result["odd"] = sorted(odd)
    return result


#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

def mean_key_value(input_dict):
    result = {}
    for key,value in input_dict.items():
        result[key] = sum(value) / len(value)
    return result