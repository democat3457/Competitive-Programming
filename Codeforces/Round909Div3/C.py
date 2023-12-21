for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if all(a <= 0 for a in arr):
        print(max(arr))
    else:
        max_max_total = 0
        for i in range(n):
            if arr[i] < 0:
                continue
            total = arr[i]
            max_total = total
            parity = arr[i] % 2 == 0
            for j in range(i+1, n):
                p = arr[j] % 2 == 0
                if p == parity:
                    break
                if (total+arr[j]) < 0:
                    break
                total += arr[j]
                if total > max_total:
                    max_total = total
                parity = p
            if max_total > max_max_total:
                max_max_total = max_total
            if i == 0 and j == n-1:
                break
            # print(total)
        print(max_max_total)