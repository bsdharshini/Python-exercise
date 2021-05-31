'''
1) Create a Cricle class and intialize it with radius.
Make two methods getArea and getCircumference inside this class.

from math import *
class one:
    
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=pi*((self.radius)**2)
        print(area)
    def circum(self):
        circum=2*(pi)*self.radius
        print(circum)

o=one(5)
o.area()
o.circum()
'''

'''
2) Create a Temprature class. Make two methods :
i. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
ii. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class temp:
    def __init__(self,c,f):
        self.c=c
        self.f=f
    def c2f(self):
        return ((self.c)*(9/5))+32
    def f2c(self):
        return ((self.f)-32)*(5/9)
t=temp(5,5)
print(t.c2f())
print(t.f2c())
'''

'''
3) Create a Student class and initialize it with name and roll number.
Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.


class student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def setAge(self,age):
        self.age=age
        return self.age
    def setMark(self,mark):
        self.mark=mark
        return self.mark
    def display(self):
        print(self.name,"\n",self.roll,"\n",self.age,"\n",self.mark)

s=student('dhara',22)
s.setAge(21)
s.setMark(100)
s.display()
'''

'''
4) Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the
Time. E.g.- (1 hr 2 min) should display 62 minute.
   
class Time():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    t3 = Time(0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)/60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
    return t3

  def displayTime(self):
    print "Time is",self.hours,"hours and",self.mins,"minutes."

  def displayMinute(self):
    print (self.hours*60)+self.mins

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
'''  
        
