#question 1
def user(a, b, c):
    x = (a + b + c) / 3
    return x

print(user(50, 20, 10))

#question 2
user = 'this is my assignment'
upper = user.capitalize()
print(upper)

#question 3
sentence = 'I am learning python'
print(sentence.replace('I', 'You'))

#question 4
string = 'i hope you had fun in class today'
print(string.count('a'))

#question 5
def check_fermat(a, b, c, n):
    if n > 2 and (a**b + b**n == c**n) :
        print('Holy smokes,fermat was wrong')
    else:
        print('no that doesnt work')
print(check_fermat(1,2,3,4))

#question6
def user():
    a = int(input('number1 for a:'))
    b = int(input('number2 for b:'))
    c = int(input('number3 for c:'))
    n = int(input('nmuber4 for n:'))
    return check_fermat(a, b, c, n)

print(user())


    

