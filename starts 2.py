num1=input()               # input nile se sobsomoy string hisabe asbe
print(type(num1))

num1=int(input())           # int dia string k integer a proyojon hole convert kore nibo
print(type(num1))

num1 = int(input())
num2 = int(input())
add = num1+num2
sub = num1-num2
div = num1/num2         # vag kora
mul = num1*num2
rem = num1%num2         # vag ses
exp = num1**num2        # power exmple : 5 r 2 nile 5 ar upore 2 thakbe,result 25
floordiv = num1//num2   # dosomik ar ager tuku, mane purno songkha tuku
print(add)
print(sub)
print(div)
print(mul)
print(rem)
print(exp)
print(floordiv)

num1 = 10
num2 = 20

print(num1 == num2) #false          # duitai soman bojhanor jonno
print(num1 != num2) #true           # duitai soman na bojhanor jonno
print(num1 <= num2) #true           # prothom ta choto othoba soman bojhanor jonno
print(num1 >= num2) #false
print(num1  < num2) #true
print(num1  > num2) #false
print(not num1 > num2) #true
print( not num1  < num2) #false

num = 10
num +=100
print(num)
num -=100
print(num)

# Assignment class 4
num = 10                            # vagses bar kora
num %= 3
print(num)

num = 10                            # vagfol bar kora kintu vagses bar kore na
num //= 3
print(num)

num = 10                            # gun kora                   #
num *= 3
print(num)

num = 5                             # nicher ta power hisebe upore thakbe                         #
num **= 2
print(num)


num = 100
num>50 and num==10 # (duitai sotto hole ans true hobe) true and false(false ans)  # 100, 50 ar chaye boro and 10 ar soman aita bujhay
num>50 or num == 10 # (j kono akta sotto holai ans true hobe) true othoba false(true ans)
not num > 50  # sotto ans k mittha kore day (false ans)

print (num > 50 and num==10)
print (num > 50 or num==10)
print (not num > 50)

num1 = "we love programming"
num2 ="love"
print(num2 in num1) # true                      # number 2,number 1 ar moddhe ache ai kotha bujhay
print(num2 not in num1) #false                  # number 2,number 1 ar moddhe nai ai kotha bujhay

num1 = "we love programming"
num2 ="love"
print(num2 is num1) #false
print(num2 is not num1) #true

