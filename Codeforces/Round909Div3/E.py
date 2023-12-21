for _ in range(int(input())):
    input()
    min_value = 10**10
    min_index = -1
    is_sorted_after_min = True
    prev_value = -1
    for i, s in enumerate(input().split()):
        v = int(s)
        if v < min_value:
            min_value = v
            prev_value = v
            min_index = i
            is_sorted_after_min = True
        else:
            if v < prev_value:
                is_sorted_after_min = False
            prev_value = v
    if not is_sorted_after_min:
        print(-1)
    else:
        print(min_index)
