def remove_columns_from_array(arr_1, index):
    for row in arr_1:
        for ind in index:
            del row[ind]
    return arr_1


def get_col_from_arr(arr_1, col_ind):
    col_arr = []
    for row in arr_1:
        for ind in range(0,len(row)):
            if ind == col_ind:
                col_arr.append(row[ind])
    return col_arr

def initialise_new_arr(row, col, dtype):
    if dtype == "str" :
        new_arr = [[" " for i in range(row)] for j in range(col)]
        return new_arr
    if dtype == "int" :
        new_arr = [[0 for i in range(row)] for j in range(col)]
        return new_arr
 
def extendarray_columnwise(first_arr, second_arr):
    for i in range(0, len(first_arr)):
        first_arr[i].extend(second_arr[i])
    return first_arr


def find_unique_elements_in_col(arr_1, index):
    return set(get_col_from_arr(arr_1, index))

def find_unique_nd_array(arr_1):
    num_of_cols = len(arr_1[0])
    unique_ele = set()
    for col in range(0, num_of_cols):
        unique_ele.update(find_unique_elements_in_col(arr_1, col))
    
    return unique_ele

def get_unique_vals_in_each_col(arr_1):
    unique_ele_dict = dict()
    num_of_cols = len(arr_1[0])
    for col in range(0, num_of_cols):
        
        unique_ele_dict[col] = list(find_unique_elements_in_col(arr_1, col))
    return unique_ele_dict