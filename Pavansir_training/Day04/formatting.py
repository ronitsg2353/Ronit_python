

# name="Ronit"
# age=26
# percentage=34.322

name,age,percentage="Ronit",26,34.22  #we can write variable and value single liine
print(name,age,percentage)

#Approach 02

print("Name is:%s Age:%d salary:%g" %(name,age,percentage))

#Approach 03-->formatting
print("Name is:{} Age is:{} Salary is:{}".format(name,age,percentage))