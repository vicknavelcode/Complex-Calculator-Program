#Building A Better Calculator
number1=float(input('Enter Your First Number: '))
number2=float(input('Enter Your Second Number: '))
print('Note: Operator only can consists of /,+,-,** or,*.No other symbols allowed')
operator=input(" Enter the type of operator you want to use ")
if operator=='/':
    divide=number1/number2
    print(divide)
elif operator=='+':
    plus=number1+number2
    print(plus)
elif operator=='-':
    minus=number1-number2
    print(minus)

elif operator=='*':
    times=number1*number2
    print(times)

elif operator=='**':
    square=number1**number2
    print(square)
else:
    print('Wrong symbol added')
print('Enjoy Your Day')





