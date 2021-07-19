def multiply(num1, num2):
    dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
    base = 1
    n1 = 0
    n2 = 0
        
    for ch in num1:
        number = dict[ch]
        n1 += (base * number)
        base *= 10
    print(n1)
            
    base = 1
    for ch in num2:
        number = dict[ch]
        n2 += (base * number)
        base *= 10
    print(n2)
        
    return str(n1 * n2)

n1 = '123'
n2 = '456'
print(multiply(n1, n2))