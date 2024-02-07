#PYTHON Syntax Practice examples
print("Hello Guys!")

#To see the version of the python 
#python --version

#to quicly atsrt the py file in cli mode is
#python hellofile.py

# to start the python in cmf
# python 0r py

#to exit
#exit()

#Indentation
#Should Not give unwanted space in any where in code line

# - this symbol is used to comment for multi line - 

"""
.......
......
.....
"""

#Variables
x=5 
y="john"
z=3.2
# the x,z,y were are variable, the 5 in integer,john is character - this should be insise in "...",3.2 is float value 
print(y)
print(x)
print(z)
# the variables are case sensitive
# variables shouls not start with number or space or the variables shloud not have this "-" symbol
#for space we can use "_"

a,b,c = "ball","sall0","call"
print(a)
print(b)
print(c)
 #or
print(a,b,c)
#using + symbol we can make it as center as like a+b+c

#global variables
aa="earth"
def palnetfunc():
    print("my planet name is" + aa)
    palnetfunc()

#for global x
def aaafunc():
    global c
    c="mannly"
    aaafunc()

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
"""
Example	Data             Type
x = "Hello World"   	str	
x = 20	                int	
x = 20.5	            float	
x = 1j	                complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                               range	
x = {"name" : "John", "age" : 36}	             dict	
x = {"apple", "banana", "cherry"}	              set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                        bool	
x = b"Hello"	                                    bytes	
x = bytearray(5)	                                bytearray	
x = memoryview(bytes(5))	                        memoryview	
x = None	                                        NoneType	
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
"""
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10))

#to print particular word mean
ct = "Hello, World!"
print(ct[1])

# to slice a particlular place mean
bmmm= "Hello, World!"
print(bmmm[2:5])

# to see the length of value
aq = "Hello, World!"
print(len(aq))

#checking via boolean
#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

"""
a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())

a = "                      Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#concartenate

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y	
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
Operator Precedence
Operator precedence describes the order in which operations are performed.

Example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
Example
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR

"""

