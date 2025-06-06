def five_point_summary(l1:list):
    l1.sort()
    mean = sum(l1)/len(l1)
    min_l1 = min(l1)
    max_l1 = max(l1)
    if len(l1)%2!=0:
        median = l1[int((len(l1)+1)/2)]
    else:
        median = (l1[int(len(l1)/2)]+l1[int(len(l1)/2) + 1])/2

    print(f"Minimum:{min_l1}\nMean:{mean}\nMedian:{median}\nMaximum:{max_l1}")
