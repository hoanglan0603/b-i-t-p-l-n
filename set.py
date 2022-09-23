# set nó chỉ chấp nhận giá trị ko giống nhau 
a_set = {2,4,5,9,12,21,30,51,76,127,195}
#print(30 in a_set)
b_set = {1,2,3,5,6,8,9,12,15,17,18,21}
union_set = a_set.union(b_set)
# print(union_set)
diffrence_set = a_set.difference(b_set)
print(diffrence_set)
difference_b = b_set.difference(a_set)
print(difference_b)