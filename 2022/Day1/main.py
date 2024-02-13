lines = open('input.txt').read().splitlines()

def split_list(lst, delimiter):
    left_idx = 0
    result = []

    if not lst:
        return result

    for idx, val in enumerate(lst):
        if val == delimiter:
            result.append(lst[left_idx:idx])
            left_idx = idx+1

    if lst[left_idx:]:
        result.append(lst[left_idx:]) # Adds the rightmost segment if it doesn't end with a delimiter

    return result

lst_of_lst = split_list(lines, '')

sumlst = []
for lst in lst_of_lst:
    single_sum = 0
    for item in lst:
        single_sum += int(item)
    sumlst.append(single_sum)
    

max1 = max(sumlst)
sumlst.remove(max1)
max2 = max(sumlst)
sumlst.remove(max2)
max3 = max(sumlst)
sumlst.remove(max3)

print(max1,max2,max3)
print(max1+max2+max3)