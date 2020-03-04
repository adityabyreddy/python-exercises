# For loop

l = [1, 2, 3, 4, 5]

# type 1 : index based
for i in range(len(l)):
    print(l[i])

# type 2 : item based
for i in l:
    print(i)

# type 3 : index and item together (enumeration)
for idx,item in enumerate(l):
    print(idx, "-->", item)

# get the index of value 4 in the list l
# sol-1
for i in range(len(l)):
    if l[i] == 4:
        print(i)
        break
# sol-2
for i,j in enumerate(l):
    if j == 4:
        print(i)
        break

# count the number of 5's
int_var_list = [1, 5, 9, 12, 4, 3, 3, 5, 5, 9]
count=0
for i in range(len(int_var_list)):
    count=count+1
print(count)

print(max(int_var_list))
print(min(int_var_list))

max_val=0
for item in int_var_list:
    #print("current max: ", max_val, " ----- current item: ", item)
    if max_val<item:
        max_val=item
print(max_val)

min_cal=max_val
for item in int_var_list:
    #print("current min: ", min_cal, " ----- current item: ", item)
    if min_cal>item:
        min_cal=item
print(min_cal)

print(sum(int_var_list))

l_sum=0
for i in int_var_list:
    l_sum=l_sum+i
print(l_sum)