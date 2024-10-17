print("Hello, World!")

z=10j
print(z)
print("type of z is",type(z))

num=10>9
print(num)
# True

print(10 // 3) 
# number without remaining

print(10%3)
# remaining

x=10
print(x**2) 
# power to 2

print(abs(-3))

print(int(5.3))

print(float(3))

print(complex(2,3))
# real imagine

com=complex(2,3)
#2+3j

print(com.conjugate())
# conjugate the complex number 2-3j

print(divmod(10,3)) 
#10 //3 , 10%3

print(pow(2,3))

print(1/2)

print(9 *(1/2))

# name=input("What is Your Name ?\n")
# print("Hello "+name)

# age=int(input("What is your age"))
# print(age)

myname="mahmoud ali"
print(myname.title()) 
# first letter is Capital Mahmoud Ali

print(myname.upper())
print(myname.lower())

x=109
print(x.bit_length())

print(bin(x))







# sets,tuple is immutable
# dictionary , sets unordered

nums=[1,2,3,4]
print(nums)
print(nums[0])
nums[1]="Mahmoud"
print(nums[1])
print(type(nums))

nums.append("Computer Science")
print(nums)

names=["Ahmed","Omar"]
concatenatedArray=names+nums
print(concatenatedArray)


names*=2
print(names)


# extend more than one elements
nums.extend(["Frontend Developer",21])
print(nums) 

# append one element 

nums.append([1,2,3])
# as one element
print (nums)

nums.insert(0,"jog")
print(nums)

del nums[1]
print(nums)
print(nums.pop())
# print last element
nums.pop()
# affetc list itself
print(nums)

nums.pop(1)
print(nums)
nums.remove("Frontend Developer")
print(nums)
numbers=[5,6,4,21,9,8]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)



print(sorted(numbers))
# temporary does not affect original list
numbers.reverse()
print(numbers)
print(len(numbers))
print(list("python"))
print(list(range(5)))

print(list((range(0,9,2))))
# start stop step
# stop not included

print(min([1,2,3]))
print(max([1,2,3]))
print(sum([1,2,3]))
squares=[sq**2 for sq in range(1,11)]
print(squares)

# slicing start stop step
print(squares[0:2:1])
# step 2 means leave one element
print(squares[2:])

# copy by value
sqs=squares[:]
print(sqs)

drinks=squares.copy()
print(drinks)



# copying by reference
sqnums=squares
print(sqnums)




# set is immutable  

tup=(1,2,3,1)
print(tup)
print(tup[0])
# tup[0]="Mahmoud"  # will give error

single = (42,)  # This is a tuple
not_a_tuple = (42)  # This is just an integer
print(tup.count(1))

print(tup.index(2))
# search for specified value 


# string is immutable
print("Mahmoud "*3  )

fc="Faculty Of Computer and Information Science"
print(fc.replace("Faculty","College")) # temporary
print(fc)
print(fc.find("Of"))
print(fc.find("Odaf"))
# in case it did not find it => -1
# sets {}

setOne={1,2,3,4,1}
print(setOne) # prevent repeatition
setOne.add(5)
print(setOne) 
setOne.remove(4)
print(setOne) 
setOne.update([4,5,6],[8,9,10]) 
# add elements Adds multiple elements from an iterable.
print(setOne) 
setOne.discard(1)
print(setOne) 




s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Union
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}
print(s1|s2)
# Intersection

print(s1.intersection(s2))  # Output: {3}
print(s1&s2)
# Difference
print(s1.difference(s2))  # Output: {1, 2}

# Symmetric Difference
print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}