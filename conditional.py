# # 1.check number is zero, negative or positive
# num= 2
# if num==0:
#     print("number is zero")
# elif num >0:
#     print("positive number")
# else:
#     print("negative number")

# # 2.Write a program to check if a given number is even or odd
# num = 10
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# # 3. Write a program to display grades based on a percentage:
# #    - A: 90-100
# #    - B: 70-89
# #    - C: 50-69
# #    - F: Below 50
# gread= 49
# if gread>=90:
#     print("you got gread A")
# elif gread>=70:
#     print("you got gread B")
# elif gread>=50:
#     print("you got gread C")
# elif gread<50:
#     print("you are fail")
# else:
#     print("please enter valid marks")

# # 4.Check if a given number is divisible by 3, 5, or both.
# num=7
# if num%3==0:
#     if num%5==0:
#         print("number is divisible by both 3 and 5")
#     else:
#         print('number is divisible by only 3')
# elif num%5==0:
#     print('number is divisible by only 5')
# else:
#     print('the given number is neither divisible by 3 nor by 5')

# 5.Find the smaller number between two given numbers.
# a=5 
# b=8
# if a==b:
#     print("both numbers are equal")
# elif a<b:
#     print(a," is smaller number")
# else:
#     print(b," is smaller number")

# # 6.Given three numbers, find the largest using nested if statements.
# a=8
# b=10
# c=6
# if a>b:
#     if a>c:
#         print(a," is greater number")
#     else:
#         print(c, " is greater")
# else:
#     if b>a:
#         if b>c:
#             print(b, ' is greater')
#         else:
#             print(c,' is greater')

##7.  Write a program to check if a given year is a leap year or not:
#    - Divisible by 4 and not 100, or divisible by 400.
# year=2024
# if year%4==0:
#     print(year,' is leap year')
# else:
#     print(year, " is not leap year")

# 8.Categorize temperature into:
#    - Cold: Below 15°C
#    - Warm: 15°C to 30°C
#    - Hot: Above 30°C 
# temp= 10
# if temp>=15:
#     if temp>30:
#         print('Hot')
#     else:
#         print('warm')
# else:
#     print('cold')

        
# #9.  Check if a given character is a vowel or consonant.
# vowel=['a','e','i','o','u']
# char='b'
# if char in vowel:
#     print("given character is vowel")
# else:
#     print('given character is not vowel')   


# 10. Check if a person is eligible to drive:
    # - Must be 18 or older.
    # - Nested check for possessing a valid license.
# age =20
# lic=True
# if age>=18:
#     if lic:
#         print("you are elidible for driving")
#     else:
#         print("you shoud take you licences for driving ")
# else:
#     print("you must have complete 18 years")

# #11. Check if three sides can form a triangle:
#     # - The sum of any two sides must be greater than the third side
# s1=4
# s2=5
# s3=6
# if s1+s2>s3:
#     if s1+s3>s2:
#         if s2+s3>s1:
#             print('this makes triangle')
#         else:
#             print('this cant make triangle')
#     else:
#         print('this cant make triangle')
# elif s1+s3>s2:
#     if s1+s2>s3:
#         if s2+s3>s1:
#             print('this makes triangle')
#         else:
#             print('this cant make triangle')
#     else:
#         print('this cant make triangle')
# elif s2+s3>s1:
#     if s2+s1>s3:
#         if s1+s3>s2:
#             print('this makes triangle')
#         else:
#             print('this cant make triangle')
#     else:
#         print('this cant make triangle')
# else:
#     print('this cant make triangle')


#12. Determine the tax rate:
    # - Salary ≤ 5,00,000: 5%
    # - 5,00,001 - 10,00,000: 10%
    # - Above 10,00,000: 20%
# salary= 2000000
# if salary>1000000:
#     tax= salary*20/100
#     print("for salary ",salary,' tax is ', tax )
# elif salary>500000:
#     tax= salary*10/100
#     print("for salary ",salary,' tax is ', tax )
# elif salary<=500000:
#     tax= salary*5/100
#     print("for salary ",salary,' tax is ', tax )

#13. Categorize a person's age:
    # - 0-12: Child
    # - 13-19: Teen
    # - 20-59: Adult
    # - 60+: Senio
# age= 11
# if age>60:
#     print('senior')
# elif age>20:
#     print('adult')
# elif age>13:
#     print('teen')
# else:
#     print('child')

# 14.Check if a number is greater than 10 and divisible by 2.
# num=5
# if num>10:
#     if num%2==0:
#         print( num," is greater than 10 and also divisible by 2")
#     else:
#         print(num, ' is greater than 10 but not divisible by 2')
# elif num%2==0:
#     print(num, ' is divisible by 2 but not greater than 10')
# else:
#     print(num, " is neither greater than 10 nor divisible by 2")

# 15.Check if a number is less than 5 or greater than 20
# num=10
# if num<5:
#     print("number is less than 5")
# elif num>20:
#     print('num is greater than 20')
# else:
#     print("number is between 5 and 20")

# # 16. Calculate an electricity bill:
#     - Usage ≤ 100 units: ₹5/unit
#     - 101-200 units: ₹10/unit
#     - Above 200 units: ₹15/unit

# usage=90
# if usage>200:
#     amount= usage*15
#     print('for unit ',usage,' payble amount will be ',amount)
# elif usage>100:
#     amount= usage*10
#     print('for unit ',usage,' payble amount will be ',amount)
# else:
#     amount= usage*5
#     print('for unit ',usage,' payble amount will be ',amount)

#17.Find the season based on the month:
    # - December-February: Winter
    # - March-May: Spring
    # - June-August: Summer
    # - September-November: Autumn
# winter=['December','January',"February"]
# Spring=['March','April','May']
# Summer=['June','July','August']
# Autumn=['Sepetember','October',"November"]

# month='October'
# if month in winter:
#     print('winter')
# elif month in Spring:
#     print('spring')
# elif month in Summer:
#     print('summer')
# else:
#     print("Autumn")

# 18.Check if a password meets these conditions:
    # - At least 8 characters.
    # - Contains the character '@'.
# password= 'H@rshal1'
# a='@'
# if len(password)>=8:
#     if a in password:
#         print('Password is strong')
#     else:
#         print("password must contains @ sign")
# else:
#     print('password length should be greater than 7')

# 19. Categorize Body Mass Index (BMI):
    # - Below 18.5: Underweight
    # - 18.5 - 24.9: Normal
    # - 25 - 29.9: Overweight
    # - 30 or higher: Obese

# BMI=10
# if BMI>=30:
#     print("Obese")
# elif BMI>=25:
#     print('Overweight')
# elif BMI>=18.5:
#     print("NOrmal")
# else:
#     print('Underweight')

# 20.  Check if a given character is:
    # - Alphabet
    # - Digit
    # - Special character
# name='@'
# if name.isalpha():
#     print('alphabates')
# elif name.isdigit():
#     print('digit')
# else:
#     print('special character')