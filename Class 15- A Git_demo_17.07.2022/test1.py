"""
def islucky(n) :
    n1 = str(n)
    sum1 = 0
    sum2 = 0
    for i in n1[0: int(len(n1)/2)]:
        sum1 += int(i)
    for j in n1[int(len(n1)/2):] :
        sum2 += int(j)
    if sum1 == sum2:
        return True
    else:
        return False


print(islucky(1230))
print(islucky(239017))
"""
"""
def fizz_return(n):
    l = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0 :
            l.append("Fizzbuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("buzz")
        else:
            l.append(str(i))
    return l

print(fizz_return(15))

"""

def printPattern(n) :
    j, k = 0, 0
    for i in range(1, n + 1) :
        if i % 2 != 0 :
            for j in range(k + 1, k + i) :
                print(str(j) + " $ ", end = " ")
            j = k + i
            print(j)
            j += 1
            k = j
        else :
            k = k + i - 1
            for j in range(k, k - i + 1, -1) :
\                print(str(j) + " $ ", end = "")
            j = k - i + 1
            print(j)

printPattern(5)