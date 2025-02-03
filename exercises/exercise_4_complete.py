import numpy as np
import matplotlib.pyplot as plt

class Mini():
    '''
    Finds the minimum of a function in given range.
    '''
    
    thr=1.e-6
    npoint=10
    maxiter=100
    d_ini=2.
    delta=d_ini/npoint
    fun_call=0
    minimum_x=None
    minimum_y=None
    
    @classmethod
    def set_precision(cls, thr):
        '''
        Sets the required resolution for the position of the minimum
        
        Args:
            thr: resolution required (default: 1e-6)
        '''
        cls.thr=thr
        
    @classmethod
    def set_range(cls, range):
        '''
        Sets the initial range around the guessed minimum (x_min)
        
        Args:
            range: the x interval around the guessed x_min will be set
                   to [x_min-range/2, x_min+range/2] (default: 2.)
        '''
        cls.d_ini=range
        
    @classmethod
    def set_maxiter(cls, maxiter):
        '''
        Sets the maximum number of iteration
        
        Args:
            maxiter: maximum number of iteration (default: 100)
        '''
        cls.maxiter=maxiter
        
    @classmethod
    def set_point(cls, point):
        '''
        Sets the number of sampling points
        
        Args:
            point: number of sampling points in the interval
                   (default: 10)
        '''
        cls.npoint=point
            
    
    @classmethod
    def findmin(cls, fun, xa, out=False):
        '''
        Finds the minimum of the function
        
        Args:
            fun: name of the function to be minimized
            xa:  guessed minimum
            
        kargs:
            out: if True, the values of x and y at the minimum are returned 
                 (default: False)
                 
        Note:
            The x and y values at the minimum are saved as the minimum_x 
            and minimum_y attributes of the class
        '''
        
        def min_rec():
            nonlocal iteration
   
            x_list=np.linspace(xa-cls.delta, xa+cls.delta, cls.npoint)

            cls.delta=abs(x_list[1]-x_list[0])
           
            y_list=fun(x_list)
           
            cls.fun_call=cls.fun_call+cls.npoint
           
            y_min_pos=np.argmin(y_list)
            x_min_approx=x_list[y_min_pos]
       
            iteration += 1
       
            return x_min_approx        
        
        cls.reset()     
        iteration=1        
        x_list=np.linspace(xa-cls.d_ini/2., xa+cls.d_ini/2., cls.npoint)        
        cls.delta=abs(x_list[1]-x_list[0])
        
        y_list=fun(x_list)
        
        cls.fun_call=cls.fun_call+cls.npoint
        
        y_min_pos=np.argmin(y_list)
        x_min_approx=x_list[y_min_pos]
        diff=abs(x_min_approx - xa)
        
        if cls.delta < diff:
           cls.delta=diff
        
        print("\n")
        cls.describe(iteration, cls.d_ini, diff, x_min_approx)
       
        
        while (iteration < 10) or (diff > cls.thr and cls.delta > cls.thr and iteration < cls.maxiter):
            
              x_min_approx=min_rec()

              diff=abs(x_min_approx - xa)
              
              xa=x_min_approx
              
              cls.describe(iteration, cls.delta, diff, x_min_approx)
                  

        y_min_approx=fun(x_min_approx)
        
        cls.minimum_x=x_min_approx
        cls.minimum_y=y_min_approx
        
        if not out:
           print("\nNumber of function calls: %i7\n" % cls.fun_call)
           print("Minimum found at  %9.7e;  fun = %6.4f" % (x_min_approx, y_min_approx))          
        else:
           return x_min_approx, y_min_approx  
    
    @classmethod
    def info(cls):
        print("\nMinimization:\n")
        print("Threshold: %6.1e;\nN. points: %3i;\nMax iterations: %4i;\nInitial Range:  %6.2f" \
              % (cls.thr, cls.npoint, cls.maxiter, cls.d_ini))
    
    @classmethod
    def reset(cls):
        cls.delta=cls.d_ini/cls.npoint
        cls.fun_call=0
        
    @classmethod
    def describe(cls, it, rng, diff, x_apx):   
        print("Iteration: %3i; range: %8.4e;  x_diff: %8.4e; x_min_approx: %10.8e" %\
             (it, rng, diff, x_apx))

    




