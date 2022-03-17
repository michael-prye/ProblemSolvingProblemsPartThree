#1.
# def get_indices(case, target):
#     indices = []
#     for i in range(len(case)):
#         for j in range(1,len(case)):
#             if target ==  case[i] + case[j]:
#                 indices = [case[i], case[j]] 
#                 break
#         if target ==  case[i] + case[j]:
#             break
#     return indices
# def print_indices(results):
#     print(f'The two indices are {results[0]} and {results[1]}')
# def run_number1():
#     case_list = [5,17,77,50]
#     target = 55
#     results = get_indices(case_list, target)
#     print_indices(results)
# run_number1()

#3.
def sort_list(list):
    temp = None
    for i in range(len(list)-1):
        for j in range(i +1,len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list.pop(j)
                list.insert(j, temp)
    return list
def test_list(list):
    for i in range(len(list)-1):
        if list[i]+1 != list[i+1]:
            return False
    return True   
def run_number3():
    list = [17,15,20,19,21,16,18]
    list = sort_list(list)
    print(test_list(list))
run_number3()

#4.


