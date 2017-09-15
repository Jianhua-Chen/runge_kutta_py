A simple somewhat fast program for the simplest runge-kutta algorithm
in python.  As with all open-source software no guarantee is given.


The program solves the initial value problem described by:

dy_i(t)/dt = f_i(t,y_j)
y_i(t0) = y0

where t0 is the initial time.  The routine which solves the IVP is:


       runge_drive(DIM,t0,tf,y0,function,err,result)


Here:

-- DIM: is the dimension of the problem (number of variables to be
   solved).

-- t0: the initial time (a number)

-- tf: the final time (a number)

-- y0: the initial values (a list of numbers)

-- function (a call to a function:see below for details)

-- err: the desired relative error (see below for details)

-- result: a list of numbers which holds [y_0(tf),y_1(tf), ...].



The function has to be of the form


       def function(i,t,y):
       	   if i==1:
	      return "something"
	   if i==2:
	      return "something"
	      .
	      .
	      .
	   if i==DIM
	      return "something

where "i" is the index of the above equation, and "y" is a list where
y[0] = y_0, y[1] = y_1 etc.  For example, for the system (x'(t) = y *
t; y'[t] = x/y) the function is:

        def function(i,t,y):
	    if i==1:
	       return y[1]*t
	    if i==2:
	       return y[0]/y[1]


The routine completes when the relative error between y(tf)_{h}
(evaluated at step size h) and y(tf)_{h'} (evaluated at step size h/2)
is less than "err".


NOTE: The program is not designed for highly oscillatory behaviour. If
you have highly oscillatory behviour you need to

1) Use the driver for a smaller time-span
2) Get the result
3) Use the result as the initial condition to compute the driver again for another time span (with less oscillatory behaviour).
4) repeat as necessary to get to the desired time.


