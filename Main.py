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
# def sort_list(list):
#     temp = None
#     for i in range(len(list)-1):
#         for j in range(i +1,len(list)):
#             if list[i] > list[j]:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list.pop(j)
#                 list.insert(j, temp)
#     return list
# def test_list(list):
#     for i in range(len(list)-1):
#         if list[i]+1 != list[i+1]:
#             return False
#     return True   
# def run_number3():
#     list = [17,15,20,19,21,16,18]
#     list = sort_list(list)
#     print(test_list(list))
# run_number3()

#4.
# def get_pos_num(case):
#     pos_num = 0
#     for i in range(len(case)):
#         if case[i] > 0:
#             pos_num += 1
#     return pos_num
# def get_neg_num(case):
#     neg_num = 0
#     for i in range(len(case)):
#         if case[i] < 0:
#             neg_num += 1
#     return neg_num
# def get_results(pos,neg):
#     results = [pos,neg]
#     return results
# def print_results(results):
#     for i in results:
#         print(i)
# def run_number4():
#     case = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
#     positive_num = get_pos_num(case)
#     negative_num = get_neg_num(case)
#     results = get_results(positive_num, negative_num)
#     print_results(results)
# run_number4()

#5.
# def find_min(case):
#     min_num = case[0]
#     for i in range(len(case)):
#         if case[i].isspace():
#             pass
#         elif min_num > case[i]:
#             min_num = case[i]
#     return min_num
# def find_max(case):
#     max_num = case[0]
#     for i in range(len(case)):
#         if case[i].isspace():
#             pass
#         elif max_num < case[i]:
#             max_num = case[i]
#     return max_num
# def get_results(min_num,max_num):
#     results = 'The minimum number is: ' + min_num + ' the maximum number is: ' + max_num
#     return results
# def run_number5():
#     case = '3 9 0 1 4 8 10 2'
#     min_num = find_min(case)
#     max_num = find_max(case)
#     print(get_results(min_num,max_num))
# run_number5()

#6.
# def validate_email(case):
#     if case.find('@') == -1:
#         return False
#     elif case.find('.com') == -1:
#         return False
#     else:
#         return True
# def run_number6():
#     test = 'mike1@gmail.com'
#     print(validate_email(test))
# run_number6()

#8.
# def run_number8():
#     current_lock = convert_to_list(3893)
#     target_lock = convert_to_list(5296)
#     test = transform_lock(current_lock, target_lock)
#     print(test)
# def convert_to_list(num):
#     list = [int(x) for x in str(num)]
#     return list
# def transform_lock(current, target):
#     count = 0
#     for i in range(len(current)):
#         while current[i] != target[i]:
#             if current[i] < target[i]:
#                 current[i] += 1
#                 count += 1
#             elif current[i] > target[i]:
#                 current[i] -= 1
#                 count += 1
#     return count
# run_number8()


c = ' '

test = 'coding is fun'
alpha= 'abcdefghijklmnopqrstuvwxyz'
x=None
final = ''
for i in range(len(test)):
    if test[i].isspace() == True:
        pass
    else:
        x =((alpha.find(test[i])+ 1))
        final += str(x)
        final += ' '
print(final)