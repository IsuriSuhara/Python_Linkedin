#Q1
a=1
b=2
def func():
        global b
        b = a + b
func()
print(b)

#Q3
def SetAnnual():
  global annual
  annual=10000
def PrintMonthly():
  print("Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()

#Q4
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)

#Q5
def Calc(currency, *rates):
  for i in rates:
      res=i+i
      print(res)

#Q6
x,y=10,100
max=x if (x>y) else y
#max=y
#if (x>y):
#    max=x
print("max:",max)

#Q9
def Sum10th(data):
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0): sum=sum+d
  return sum

r=Sum10th((1,2,3,4,5,6,6,7,8,15,15,9,9))
print(r)

#Q10
class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex
    print(name)
c= Person()

c.__initialize__("Isuri", 13, "F")
