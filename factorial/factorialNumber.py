def factorial_function(number):
 assert number >= 0. and type(number) is int, "The input is not redirect"
 if number == 0:
     return 1
 else:
     return number * factorial_function(number-1)