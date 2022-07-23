import matplotlib.pyplot as plt
import math

# Use matplotlib to plot the following equation:
# y=x^2−x+2

# You'll need to write the code that generates the x and y points.

# Add an anotation for the point 0, 0, the origin.

# Create and label 4 separate charts for the following equations (choose a range for x that makes sense):

#       y=√x

x = range(0,10)
y = [math.sqrt(n) for n in x]  

plt.plot(x,y)  
plt.show() 

#       y=x^3

x = range(-10,10)  
y = [n**3 for n in x ]  

plt.plot(x,y)  
plt.show() 

#       y=2^x

x = range(0,10)  
y = [2**n for n in x]  

plt.plot(x,y)  
plt.show() 

#       y=1/(x+1)

x = range(2,10)  
y = [1/(n-1) for n in x]
    
plt.plot(x,y)
plt.show() 
   

# You can use functions from the math module to help implement some of the equations above.
# Combine the figures you created in the last step into one large figure with 4 subplots.
# Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend and an appropriate title for the figure.

#     Title your chart  Big O Notation 
#     Label your x axis  Elements 
#     Label your y axis  Operations 
#     Label your curves or make a legend for the curves
#     Use LaTex notation where possible

plt.figure(figsize=(12.5,6.5))  

x = range(0,10)
y = [math.sqrt(n) for n in x]
plt.subplot(221)
plt.plot(x,y)
plt.title('sqaure root of x')  

x = range(-10,10)  
y = [n**3 for n in x ]
plt.subplot(222)
plt.plot(x,y)
plt.title('x^3')


x = range(0,10)  
y = [2**n for n in x]  
plt.subplot(223)
plt.plot(x,y)
plt.title('n^x')

x = range(2,10)
y = [1/(n-1) for n in x]
plt.subplot(224)
plt.plot(x,y)
plt.title('1/(x-1)')

plt.suptitle('These are my four functions')
plt.show() 

# Curves to graph

# y= 0n+1
# and label the curve  O(1) 

# y= log(n)
# and label the curve  O(log n) 

# y= n
# and label the curve  O(n) 

# y= n * log(n)
# and label it  O(n log n) 

# y= n^2
# and label it  O(n^2) 

# y= 2^n
# and label it  O(2^n) 

# y= n!
# and label it  O(n!) 

# y= n^n
# and label it  O(n^n) 
x = range(1,30)

plt.figure(figsize=(12.5,6.5))

y1 = [(0 * n) + 1 for n in x]  
y2 = [math.log(n) for n in x]  
y3 = [n for n in x]  
y4 = [n * math.log(n) for n in x]  
y5 = [n**2 for n in x]  
y6 = [2**n for n in x]  
y7 = [math.factorial(n) for n in x]  
y8 = [n**n for n in x]  
       
plt.plot(x,y1, label='O(1)')  
plt.plot(x,y2, label='O(log(n))')  
plt.plot(x,y3, label='O(n)')  
plt.plot(x,y4, label='O(n log n)')  
plt.plot(x,y5, label='O($n^{2}$)')  
plt.plot(x,y6, label='O($2^{n}$)')  
plt.plot(x,y7, label='O(n!)')  
plt.plot(x,y8, label='O($n^{n}$)')  

plt.ylim(0,50)  
plt.title('range of big O notations')  
plt.legend()  
plt.show() 

# Bonus Write the code necessary to write your name on a chart. Use box letters.

# Bonus: use curves for letters in your name that have curves in them.
