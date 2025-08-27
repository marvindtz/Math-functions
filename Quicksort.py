import inspect
import traceback
list = [1,23,54,6,2,5,43,4,22,44,24,55,29,44,13,7,22 ]



def quicksort(listtosort):
    links = []
    rechts = [] 
    equal =[]
    level = len(inspect.stack(0))-1
    cnt = len(listtosort)
    print(f"Quicksort: {listtosort} + {level}")
    if cnt <= 2: 
        return listtosort
    mid = round(cnt/2)-1
    piv = listtosort[cnt-1]
    print(f"piv: {piv}")
    for i in range(0,cnt):
        if listtosort[i] > piv:
            rechts.append(listtosort[i])
        elif listtosort[i] == piv:
            equal.append(listtosort[i])
        else:
            links.append(listtosort[i])

    if len(inspect.stack(0)) == 6:
        traceback.print_stack()

    print(f"L={links}")
    print(f"R={rechts}")
    res1 =  quicksort(links) 
    res2 = quicksort(rechts)  
    print(f"RESULT{level}={res1+res2}")
    print(f"Equal{level}={equal}")
    return res1 + equal +  res2
    



list = quicksort(list)
print(list)
