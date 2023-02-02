def is_armstrong_number(number):
    sum=0
    number1=str(number)
    number_of_digits=len(number1)
    for digit in number1:
        digit=int(digit)
        sum=sum+digit**number_of_digits
    if sum==number:
        return True
    else:
        return False
