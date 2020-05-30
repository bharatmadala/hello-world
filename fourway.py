from matplotlib.pyplot import * 
from numpy import*
import copy
def my_plot(t,y,shape='',x_label='time (s)',fig_num = 1,cl_fig= True,name ='',):
 figure(fig_num)
if cl_fig:
	clf()
if shape:
	plot(t,y,shape)
else:
	plot(t,y)
if name:
	title(name)
if x_lable:
	xlabel(x_label)
t = arrage(0,1,0.01)
y= 2.0*sine(2*pi*t)
a= copy(y)
b= copy(y)
c= copy(y)
d= copy(y)
#cryptic
a[a< 0.5] = 0
my_plot(t,y,shape = "r--")
my_plot(t,a,name= 'cryptic',cl_fig= False)
#for loop
n =len(b)
b_new= zeros(n)

for i in range(n):
 if b[i]>0.5:
	b_new[i] =b[i]
my_plot(t,y,shape ='r--',fig_num=2)
my_plot(t,c_new,name = 'for loop',fig_num=2,cl_fig = false
# where
inds = where(c <0.5)[0]
c[inds]=0
my_plot(t,y,shape ='r--',fig_num=3)
my_plot(t,c,name ='where',fig_num=3,cl_fig = False)
#Enumerete
for i ,item in enumerate(d):
	if item < 0.5:
		d[i] = 0
my_plot(t,y,shape ='r--',fig_num =4 )
my_plot(t,d,name = 'enumerate',fig_num=4,cl,fig= False)

show()		
			
			

