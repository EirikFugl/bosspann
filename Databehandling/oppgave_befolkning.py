import matplotlib.pyplot as plt
import numpy as np
aarstall = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
antall = [4478497, 4503436, 4524066, 4552252, 4577457, 4606363, 4640219, 4681134, 4737171, 4799252, 4858199, 4920305, 4985870, 5051275, 5109056, 5165802, 5213985, 5258317, 5295619, 5328212, 5367580, 5391369, 5425270]

plt.subplot(2,1,1)
plt.plot(aarstall,antall)

xverdier = np.linspace(1,10,11)

def f(x): return x*1

def g(x): return x*2

def h(x): return x*3

def i(x): return x*4

def j(x): return x*5

plt.subplot(2,1,2)

plt.plot(xverdier,f(xverdier))
plt.plot(xverdier,g(xverdier))
plt.plot(xverdier,h(xverdier))
plt.plot(xverdier,i(xverdier))
plt.plot(xverdier,j(xverdier))

plt.show()