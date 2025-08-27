listtosort = ['aa','ab','af','bx','as','ac','bb','ff','cf','zb','fr','fg']





def sortlist(mylist):
    cnt = len(mylist)
    print(cnt)
    for re in reversed(range(1,cnt)):
        for e in range(0,re):
            print(f'e= {re},{e}')
            if mylist[e] >= mylist[e+1]:
                bckup = mylist[e]
                mylist[e] = mylist[e+1]
                mylist[e+1] = bckup
                
            #    print(f'e= {mylist[e]}')
                



sortlist(listtosort)
print(listtosort)