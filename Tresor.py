import math
liste = []
def first_n_digits(num, n):
    return (num // 10 ** (int(math.log(num, 10)) - n + 1))%10

for i in range(123456789,987654322):
    liste.clear()
    for d in range(1,10):
        a = first_n_digits(i,d)
        if a == 0:
            break
        if a in liste:
            break
        liste.append(a)
        if d == 9:
            if liste[4] - liste[8] == liste[5] and liste[8] + liste[4] == liste[1] and liste[6] * liste[8] == liste[0] and liste[7] - liste[2] == liste[3] / liste[8]:
                print(i)
    else:
        pass
    