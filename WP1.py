from timeit import default_timer as timer
my_list = [1,2,3,4,7,9,3,7,5,8,2,7,1,23,5,6,1,34,12,67,56,34,3]

# ITERATIVES:

start1 = timer()
def my_list_length_iterative(list_var):
    counter = 0
    for x in list_var:
        counter = counter + 1
    return counter
end1 = timer()

start2 = timer()
def my_list_sum_iterative(list_var):
    sum = 0
    for x in list_var:
        sum = sum + x
    return sum
end2 = timer()

start3 = timer()
def my_list_max_iterative(list_var):
    max = float('-inf')
    for x in list_var:
        if x > max:
            max = x
    return max
end3 = timer()

start4 = timer()
def my_list_min_iterative(list_var):
    min = float('inf')
    for x in list_var:
        if x < min:
            min = x
    return min
end4 = timer()

output1 = "{:.7f}".format(end1 - start1)
output2 = "{:.7f}".format(end2 - start2)
output3 = "{:.7f}".format(end3 - start3)
output4 = "{:.7f}".format(end4 - start4)

print("ITERATIVES:")
print("length: %d" % my_list_length_iterative(my_list))
print("time: %s" % output1)
print("sum: %d" % my_list_sum_iterative(my_list))
print("time: %s" % output2)
print("max: %d" % my_list_max_iterative(my_list))
print("time: %s" % output3)
print("min: %d" % my_list_min_iterative(my_list))
print("time: %s" % output4)
print()

# RECURSIVES:

start = timer()

def my_list_length_recursive(list_var):
    if list_var:
        return 1 + my_list_length_recursive(list_var[1:])
    return 0

def my_list_sum_recursive(list_var):
    if not list_var:
        return 0
    else:
        return list_var[0] + my_list_sum_recursive(list_var[1:])

def my_list_max_recursive(list_var):
    if my_list_length_recursive(list_var) == 1:
        return list_var[0]
    else:
        return list_var[0] if list_var[0] > my_list_max_recursive(list_var[1:]) else my_list_max_recursive(list_var[1:])

def my_list_min_recursive(list_var):
    if list_var:
        return list_var[0]
    else:
        return list_var[0] if list_var[0] > my_list_min_recursive(list_var[1:]) else my_list_min_recursive(list_var[1:])

end = timer()
time_recursive = end - start
output = "{:.7f}".format(time_recursive)

print("RECURSIVES:")
print("length: %d" % my_list_length_recursive(my_list))
print("sum: %d" % my_list_sum_recursive(my_list))
print("max: %d" % my_list_max_recursive(my_list))
print("min: %d" % my_list_min_recursive(my_list))
print("time: %s" % output)
print()

