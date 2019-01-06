def longest_increasing_subsequence(arr):
    max_len = 0
    for i in range(len(arr)):
        print("\n",i)
        j = i + 1
        t_arr = arr[i:]
        while j < len(t_arr):
            print("\tt_arr i:", t_arr[i], "t arr j:", t_arr[j])
            if t_arr[j] > t_arr[i]:
                i = j
                j = j + 1
            else:
                print("\t drop:", t_arr[j])
                del t_arr[j]        
        if len(t_arr) > max_len:
            max_len = len(t_arr)
            print(t_arr)

    return max_len

#Sample Test Cases:
# arr = [10,22, 9, 33, 21, 50, 41, 60, 80]
# arr = [3,10,2,1,20]
# arr = [3,2]
arr = [50, 3, 10, 7, 40, 80]
longest_increasing_subsequence(arr)
