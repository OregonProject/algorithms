def bidirectional_sum_search(lst, n_sum):

    start_index = 0
    end_index = len(lst) - 1
   
    while (start_index <= len(lst) - 1):
        s = lst[start_index] + lst[end_index]
        
        if s == n_sum:
            return str(lst[start_index]) + " + " + str(lst[end_index]) + " = " + str(n_sum)
        elif s > n_sum:
            end_index = end_index - 1
            continue
        elif s < n_sum:
            start_index = start_index + 1
            continue
        else:
            break

    return "There are no numbers in this collection that equate to the sum."
