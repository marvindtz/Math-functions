

ListToScan = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
NumToSearch = 13





def setMid(FirstIdx, LastIdx):
    mid = round((LastIdx + FirstIdx)/2)
    return mid

def BinarySearch(List,Number):
    cnt = len(ListToScan)
    FirstIdx = 0
    LastIdx = cnt - 1
    while FirstIdx < LastIdx:
        mid = setMid(FirstIdx,LastIdx)
        print(f'FirstIdx: {FirstIdx}, LastIdx: {LastIdx}, mid:{mid}')
        if List[mid] < Number:
            FirstIdx = mid
        elif List[mid] > Number:
            LastIdx = mid - 1
        else:
            break
            
    print(f'Zahl gefunden. Eintrag:{mid}')


#BinarySearch(ListToScan,NumToSearch)
#setMid(30,60)
#print('finished')




cnt = len(ListToScan)
FirstIdx = 0
LastIdx = cnt - 1



def BinarySearchRekursiv(List,Number,FirstIdx,LastIdx):
    if FirstIdx > LastIdx:
        return -1
    mid = round((LastIdx + FirstIdx)/2)
    print(f'Mid: {mid}')
    if List[mid] < Number:
        FirstIdx = mid
    elif List[mid] > Number:
        LastIdx = mid
    else:
        return mid
        print(f'Gefunden: {mid}')
    BinarySearchRekursiv(List,Number,FirstIdx,LastIdx)



BinarySearchRekursiv(ListToScan,NumToSearch,FirstIdx,LastIdx)
