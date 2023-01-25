
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

# def divirsor(num):
#     lst=[]
#     for i in range (1,num+1):
#         if num % i == 0 :
#             lst.append(i)
#     return lst



# print(get_divisors(12)) # [1, 2, 3, 4, 6, 12]



# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


# def divirsor_second(a,b):
#     a_value =divirsor(a)
#     b_value =divirsor(b)

#     if b in a_value or a in b_value:
#         return True
#     else:
#         return False
# print(divirsor_second(12,5))



# -------------------------------------------------------------------------------------- #

#print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

# def new(letter):

#     id_number = ""
#     for char in letter.lower():
#         id_number += str(alphabet.index(char))
#     return id_number
        
# print(new("s"))



#print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# def new():
#     letter=input("please insert a name: ")
#     id_number = ""
#     for char in letter.lower():
#         id_number += str(alphabet.index(char))
#     return id_number
        
# print(new())



#print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# def new():
#     letter=input("please insert a name: ")
#     id_number = ""
#     for char in letter.lower():
#         id_number += str(alphabet.index(char))
#     return id_number


#A2c:
def generate_id(name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    id_number = ''.join(str(alphabet.index(c) + 1) for c in name.lower())
    return id_number

def generate_password(generate_id,name):
    id_number = generate_id(name)
    id_sum = sum(int(i) for i in id_number)
    password = int(id_number) - id_sum
    return id_number

print(generate_password("Bob","hi")) # 1134
#print(generate_password("John")) # 151406

# -------------------------------------------------------------------------------------- #

#print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
# def checking(n):
#     #n = int(input("Please enter a number: "))
#     for i in range(2,n):
#         if (n%i) == 0:
#             return False
#     return True
# print(checking(17))
# -------------------------------------------------------------------------------------- #
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
# def more_func():
#     #inputn = 3

#     #Taking user input
#     inputn = int(input("Enter a number: "))

#     if inputn > 1:
#     # check for factors
#         for i in range(2,inputn):
#             if (inputn % i) == 0:
#                 print(inputn,"is not a prime number.")
#                 break
#         else:
#             print(inputn,"is a prime number.")
        
#     #If the input number is less than or equal to 1, then it is not prime
#     else:
#         print(inputn,"is not a prime number.")
# more_func()
# -------------------------------------------------------------------------------------- #






