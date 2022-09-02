nums = [2, 3, 1, 4, 8, 10]
def bubble_sort(lists):
    len_list = len(lists)
    for i in range(len_list):
        for j in range(len_list - i - 1):
            if (lists[j] > lists[j + 1]):
                '''tmp = lists[j + 1]
                lists[j + 1] = lists[j]
                lists[j] = tmp'''
                lists[j],lists[j+1]=lists[j+1],lists[j]
    return lists

bubble_sort(nums)
print(nums)