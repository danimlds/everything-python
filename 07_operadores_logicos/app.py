idade = 18
print(idade >= 18)

verdadeiro = True
falso = False

print(not verdadeiro)
print(not falso)

print(not(10 >= 5))#False


a = 5
b = 10
c = 2
d = 8

print(a > b and c > d)#False
print(a > b and c < d)#False
print(c < d and b < c)#False
print(a < b and b > c)#True

print(a > b or c > d)#False
print(a > b or c < d)#True
print(c < d and b < c)#False
print(a < b and b > c)#True