#include <iostream>

int main()
{
    int q;
    std::cin >> q;
    for (int _i = 0; _i < q; _i++)
    {
        int n;
        std::cin >> n;
        int p[n];
        for (int j = 0; j < n; j++)
            std::cin >> p[j];
        int sizes[n];
        for (int i = 0; i < n; i++)
        {
             
        }
    }
for _ in range(int(input())):
    input()
    p = [0] + list(map(int, input().split()))
    sizes = dict()
    for i in range(1, len(p)):
        if i in sizes:
            continue
        count = 1
        visited = set()
        visited.add(i)
        n = p[i]
        while n != i:
            visited.add(i)
            n = p[n]
            count += 1
        for v in visited:
            sizes[v] = count
    print(' '.join(map(lambda x: str(x[1]), sorted(sizes.items(), key=lambda y: y[0]))))
}
