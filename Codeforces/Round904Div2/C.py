# incomplete

import math
from collections import defaultdict
for _ in range(int(input())):
    n,m = map(int, input().split())
    segments: list[tuple[int,int]] = [tuple(map(int, input().split())) for _ in range(n)]
    value = 0
    instructions = defaultdict(int)
    for seg_l, seg_r in segments:
        instructions[seg_l] += 1
        instructions[seg_r] -= 1
    minimum = math.inf
    min_indices = []
    maximum = -1
    max_indices = []
    for i in range(1,m+1):
        if i in instructions:
            value += instructions[i]
            if value > maximum:
                maximum = value
                max_indices = []
            elif value < minimum:
                minimum = value
                min_indices = []
        if value == maximum:
            max_indices.append(i)
        if value == minimum:
            min_indices.append(i)
    keep = []
    remove = []
    unsure = []
    for seg_l, seg_r in segments:
        ma = [seg_l <= x <= seg_r for x in max_indices]
        mn = [seg_l <= x <= seg_r for x in min_indices]
        if all(ma):
            # all max in segment, keep
            keep.append((seg_l, seg_r))
        elif not any(ma):
            # none max, remove
            remove.append((seg_l, seg_r))
        elif not any(mn):
            # some max, no min, keep
            keep.append((seg_l, seg_r))
        elif all(mn):
            # some max, all min, remove
            remove.append((seg_l, seg_r))
        else:
            unsure.append((seg_l, seg_r))
    

