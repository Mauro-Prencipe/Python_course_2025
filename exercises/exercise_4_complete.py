import numpy as np
import matplotlib.pyplot as plt

class Mini():
    
    thr=1.e-6
    npoint=10
    maxiter=1000
    d_ini=2.
    delta=d_ini/npoint
    fun_call=0
    expand=1.2
    y_der=0.
    
    @classmethod
    def set_precision(cls, thr):
        cls.thr=thr
        
    @classmethod
    def set_range(cls, range):
        cls.d_ini=range
        
    @classmethod
    def set_maxiter(cls, maxiter):
        cls.maxiter=maxiter
        
    @classmethod
    def set_point(cls, point):
        cls.npoint=point
    
    @classmethod
    def set_expand(cls, value):
        if value < 1.1:
           print("*** WARNING *** Expansion factor cannot be les than 1.1")
           cls._expand=1.1
        else:              
           cls._expand=value
        
    
    @classmethod
    def findmin(cls, fun, xa, out=False):
        
        cls.reset()
        
        iteration=1
        
        x_list=np.linspace(xa-cls.d_ini/2., xa+cls.d_ini/2., cls.npoint)
        
        cls.delta=2.*abs(x_list[1]-x_list[0])
        
        y_list=fun(x_list)
        y_list_diff=np.diff(y_list)
        y_derivative=y_list_diff/cls.delta
        
        cls.fun_call=cls.fun_call+cls.npoint
        
        y_min_pos=np.argmin(y_list)
        x_min_approx=x_list[y_min_pos]
        diff=abs(x_min_approx - xa)
        cls.y_der=y_derivative[y_min_pos]
        
        if cls.delta < diff:
           cls.delta=cls.expand*diff
        
        print("\n")
        cls.describe(iteration, cls.d_ini, diff, cls.y_der, x_min_approx)
    
    
        def min_rec():
            nonlocal iteration
    
            x_list=np.linspace(xa-cls.delta, xa+cls.delta, cls.npoint)
            Delta=abs(x_list[1]-x_list[0])                    
            cls.delta=cls.expand*Delta
            
            y_list=fun(x_list)
            y_list_diff=np.diff(y_list)
            y_derivative=y_list_diff/cls.delta
            
            y_list_diff=np.diff(y_list)
            y_derivative=y_list_diff/cls.delta
            
            cls.fun_call=cls.fun_call+cls.npoint
            
            y_min_pos=np.argmin(y_list)
            x_min_approx=x_list[y_min_pos]
            cls.y_der=y_derivative[y_min_pos]
        
            iteration += 1
        
            return x_min_approx
       
        
        while (iteration < 10) or (diff > cls.thr and cls.delta > cls.thr and iteration < cls.maxiter):
            
              x_min_approx=min_rec()

              diff=abs(x_min_approx - xa)
              
              xa=x_min_approx
              cls.describe(iteration, cls.delta, diff, cls.y_der, x_min_approx)
                  

        y_min_approx=fun(x_min_approx)
        
        if not out:
           print("\nNumber of function calls: %i7\n" % cls.fun_call)
           print("Minimum found at  %9.7e;  fun = %6.4f" % (x_min_approx, y_min_approx))          
        else:
           return x_min_approx, y_min_approx  
    
    @classmethod
    def reset(cls):
        cls.delta=cls.d_ini/cls.npoint
        cls.fun_call=0
        
    @classmethod
    def describe(cls, it, rng, diff, der, x_apx):   
        print("Iteration: %3i; range: %8.4e;  x_diff: %8.4e; deriv: %8.4e; x_min_approx: %10.8e" %\
             (it, rng, diff, der, x_apx))

    




