#Exercise 5.2
#By: Major Mosley



#import pdb
#pdb.set_trace()
def g(x): #We create our function that we wish to integrate
    return x**4 - 2*x + 1
def G(x): 
    return x**5/5 - x**2 + x

def simpson(f,a,b,n):
    h = (b-a)/n

    v_o = 0
    for i in range(1,n//2 - 1):
        v_o += f(a + 2*i*h)

    v_1 = 0
    for i in range(1,n//2): #use division operator 

        v_1 += f(a +(2*i-1)*h)

        integral = h/3 * (f(a) + f(b) + 4*v_o + 2*v_1)
    return integral


a = 0
b = 2
#n = 10
#n = 100
#n = 55
n = 100000
exact = G(b) - G(a) #get actual value for the integral
answr = simpson(g,a,b,n)
error = (abs(answr - exact)/exact)*100 #here i am checking for the percentage error
print('There is an error of: {0:.2f}'.format(error))
print(exact)
print('Simpson rule gives: {0:.3f}'.format(answr))

###########Graphing part of program begins #########################



import matplotlib.pyplot as plt
import numpy as np

#here we have 250 iterations from a to b
x0 = np.linspace(a,b, 250)
plt.plot(x0, G(x0), '-', label = 'Function')

#creating x axis and steps to be taken which is 10
x = np.linspace(a, b, n+1)
plt.plot(x, G(x), 'o', label = 'Simpson Rule')

verts = [(a, 0)] + list(zip(x, G(x))) + [(b, 0)]
plt.vlines(x, 0, G(x), colors = 'black')

#fill in area under curve with black 
plt.fill_between(x, G(x), color = 'black')
plt.title('Simpson Rule') 
plt.xlabel(r'$x$')
plt.ylabel(r'$Exact Integral$')
plt.legend()
plt.axhline(0, color = 'black')
plt.show()



