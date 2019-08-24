#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst=[10,2,3,6,33,45]
result=list(filter(lambda x:x%2==0,lst))
print (result)


# In[2]:


from functools import reduce
lst=[5,10,20]
reduce(lambda x,y:x+y, lst)


# In[3]:


def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner
def num():
    return 5
decor(num())
resultfun=decor(num)
print(resultfun())


# In[4]:


def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner
@decor
def num():
    return 5
# decor(num())
# resultfun=decor(num)
print(resultfun())


# In[5]:


def decor(fun):
    def inner(n):
        result=fun(n)
        result=result+"how are you?"
        return result
    return inner
@decor
def hello(name):
        return "hello "+name
print(hello("palak "))


# In[6]:


def customgen(x,y):
    while x<y:
        yield x
        x+=1 
result=customgen(20,30)

for i in result:print(i)


# In[7]:


lst=[]
for x in range(1,11):
   lst.append(x**3)
print(lst)


# In[8]:


lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)


# In[9]:


lst=[x for x in range(2,21,2)]
print(lst)


# In[10]:


lst=[x for x in range(1,21) if x%2==0]
print(lst)


# In[11]:


a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)


# In[12]:


a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]
z=[a[i]*b[i] for i in range(len(a))]
print(z)


# In[13]:


a=[2,3,4,5]
b=[1,2,3,4]
result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)


# In[14]:


a=[2,3,4,5]
b=[1,2,3,4]
result=[]
# for i in a:
#     if i in b:
#         result.append(i)
result=[i for i in a if i in b]
print(result)


# In[15]:


class Student:
    def __init__(self):
        self.id=123
        self.name="palak"
        
s=Student()
print(s.id)
print(s.name)


# In[16]:


class Student:
    def __init__(self):
        self.__id=123
        self.__name="palak"
        
    def display(self):
        print(self.__id)
        print(self.__name)
        
s=Student()
s.display()
print(s._Student__id);
print(s._Student__name);  #name_mangling


# print(s.__id)
# print(s.__name)


# In[17]:


class Student:
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
s=Student()
s.setId(123)
s.setName("palak")
print(s.getId())
print(s.getName())


# In[18]:


from abc import abstractmethod
class BMW:
        def __init__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year
        
        def start(self):
            print("starting the car")
            
        def stop(self):
            print("stopping the car")
        
        @abstractmethod
        def drive(self):
            pass 
            
            
class ThreeSeries(BMW):
    
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
        
    def display(self):
        print(self.cruiseControlEnabled)
        
class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled
        
threeSeries=ThreeSeries(True,"BMW","328i","2019")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()


# In[19]:


class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hello")
        
def callTalk(obj):
    obj.talk();
    
d=Duck()
callTalk(d)
h=Human()
callTalk(h)


# In[20]:


class Flight:
    def __init__(self,engine):
        self.engine=engine
        
    def startEngine(self):
        self.engine.start();
        
class AirbusEngine:
    def start(self):
        print("starting airbus engine")

class BoingEngine:
    def start(self):
        print("starting boingengine engine")
ae=AirbusEngine()
f=Flight(ae)
f.startEngine()

be=BoingEngine()
f1=Flight(be)
f1.startEngine()


# In[21]:


x=10
y=20
print(x+y)
s1="hello"
s2=" palak"
print(s1+s2)
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)


# In[22]:


from abc import abstractmethod,ABC
class BMW(ABC):
        def __init__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year
        #@abstractmethod
        def start(self):
            print("starting the car")
        #@abstractmethod   
        def stop(self):
            print("stopping the car")
        
        @abstractmethod
        def drive(self):
            pass 
            
            
class ThreeSeries(BMW):
    
    def __init__(self,cruiseControlEnabled,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled
        
    def display(self):
        print(self.cruiseControlEnabled)
        
    def drive(self):
        print("three series is driven")
        
class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled
        
    def drive(self):
        print("five series is driven")
        
threeSeries=ThreeSeries(True,"BMW","328i","2019")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()


# In[23]:


class Product:
    
    def __init__(self):
        self.name='iphone'
        self.description='its awesome'
        self.price=700
        
p1=Product()
print (p1.name)
print (p1.description)
print (p1.price)
       
p2=Product()
print (p2.name)
print (p2.description)
print (p2.price)


# In[24]:


class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def average(self):
        numberofRatings=len(self.ratings)
        average = sum(self.ratings)/numberofRatings
        print("average",self.name,"is",average)
        
c1=Course("java course",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()


# In[25]:


class Programmer:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
    def setSalary(self,s):
        self.salary=s
    def getSalary(self):
        return self.salary

p=Programmer()
p.setName("palak")
p.setSalary(30000)
print("name is",p.getName())
print("salary is",p.getSalary())


# In[26]:


class Student:
    major="CSE"
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s=Student(1,"abc")
s1=Student(2,"xyz")
print(s.major)
print(s.name)
print(s1.name)


# In[27]:


class ObjectCounter:
    numberofObjects=0
    
    def __init__(self):
        ObjectCounter.numberofObjects+=1
    @staticmethod   
    def displayCount():
        print(ObjectCounter.numberofObjects)
        
o1=ObjectCounter()
o2=ObjectCounter()
ObjectCounter.displayCount()
        
        


# In[1]:


import logging
logging.basicConfig(filename="mylog.log",level=logging.ERROR)
logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")


# In[2]:


print("hello")


# In[7]:


import re
str="take up one idea. One idea at a time"
result=re.search(r'o\w\w',str)
print(result.group())


# In[22]:


import time,datetime
epochseconds=time.time()
print(epochseconds)
t=time.ctime(epochseconds)
print (t)
dt=datetime.datetime.today()
print(dt.day,dt.month,dt.year,)


# In[25]:


from datetime import *
d=date(2019,8,23)
t=time(9,24)
dt=datetime.combine(d,t)
print(dt)


# In[33]:


import time 
startTime=time.perf_counter()
ldates=[]
d1=date(2016,8,12)
d2=date(2016,3,12)
d3=date(2018,8,12)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.sort()
for d in ldates:
    print(d)
endTime=time.perf_counter()
print("execution time=",endTime-startTime)

#     time.sleep(3)


# In[34]:


import time 
time.sleep(3)


# In[38]:


import threading
print("current thread that is running:",threading.current_thread().getName())
if threading.current_thread()==threading.main_thread():
    print("main thread")
else:
    print("some other thread")


# In[43]:


from threading import * 
def displayNumbers():
    i=0
    print(current_thread().getName)
    while (i<=10):
        print(i)
        i+=1
print(current_thread().getName)
t=Thread(target=displayNumbers)
t.start()


# In[44]:


from threading import Thread
class MyThread(Thread):
    def run(self):
        i=0
        while (i<=10):
            print(i)
            i+=1
t=MyThread()
t.start()
        


# In[50]:


from threading import *
from time import sleep
class MyThread:
    def displayNumbers(self):
        i=0
        #print(current_thread().getName)
        sleep(3)
        while (i<=10):
            print(i)
            i+=1
obj=MyThread()
t=Thread(target=obj.displayNumbers)
t.start()


# In[64]:


from threading import *
class Bookmybus:
    def __init__(self,availableseats):
        self.availableseats=availableseats
#         self.l=Lock()
        self.l=Semaphore()
            
    def buy(self,seatsrequested):
        self.l.acquire()
        print("total seats available:",self.availableseats)
        
        if(self.availableseats>=seatsrequested):
            print("confirming a seat")
            print("processing payment")
            print("printing ticket")
            self.availableseats-=seatsrequested
            
        else:
            print("no seats available")
        self.l.release()
        
obj=Bookmybus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()
        


# In[81]:


from threading import *;
from time import *;
class Producer:
    def __init__(self):
        self.products=[]
        self.ordersplaced=False
    
    def produce(self):
        for i in range(1,5):
            self.products.append("product"+str(i))
            sleep(1)
            print("item added")
        self.ordersplaced=True

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    
    def consume(self):
        while self.prod.ordersplaced==False:
            sleep(0.2)
            
        print("orders shipped",self.prod.products)
        
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()


# In[82]:


from threading import *;
from time import *;
class Producer:
    def __init__(self):
        self.products=[]
        self.c=Condition()
    
    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("product"+str(i))
            sleep(1)
            print("item added")
        self.c.notify()
        self.ordersplaced=True

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
#         while self.prod.ordersplaced==False:
#             sleep(0.2)
        self.prod.c.release()    
        print("orders shipped",self.prod.products)
        
p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()


# In[85]:


import urllib.request
try:
    url=urllib.request.urlopen("https://www.udemy.com/course/python-data-structures-a-to-z/learn/lecture/14222028#overview")
    content=url.read()
    url.close()
except urllib.error.HTTPError:
    print("url not found")
    exit()
    


# In[ ]:


import socket
host='localhost'
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("server listening on port:",port)
s.listen(1)
c,addr=s.accept()
print("connection from:",str(addr))
c.send(b"hi how are you")  #convert to binary
c.send("bye".encode)#convert to binary
c.close()


# In[ ]:




