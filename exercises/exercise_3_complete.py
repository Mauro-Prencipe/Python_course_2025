# Create a class that provides some statistics drawn from
# a dataset. 

# The dataset is an Excel file that can be read with the
# function read_excel of the Pandas library. Columns headers
# can conveniently be used as the names of the variables
# that are instances of the class. 

# Thus create an instance of the class for each column 
# of the dataset

import numpy as np
import pandas as pd

class Statistics():
    
    variables=None
    num_sets=0
    
    def __init__(self, name, x):
        self.num_data=None
        self.average_flag=False
        self.ave=None
        self.std=None
        self.data=None
        self.data_flag=False
        self.data=x
        self.num_data=len(x)
        self.name=name
            
    def average(self):
        
        x=self.data        
        sum=0.
        for ix in x:
            sum += ix
        
        ave=sum/self.num_data
        
        self.ave=ave
        self.average_flag=True

    def standard(self):
        if not self.average_flag:
           self.average()
           
        x=self.data
        std=0.
        
        for ix in x:
            std=std+(ix-self.ave)**2
            
        self.std=np.sqrt(std/(self.num_data-1.))
        
    def describe(self):
        
        self.average()
        self.standard()
        
        print("\n-------------------\nDataset: ", self.name)
        print("Data:\n", self.data, "\n")
        print("Number of data: %6i" % self.num_data)
        print("Average:        %6.2f" % self.ave)
        print("Standard dev:   %6.2f"% self.std)
        
    
    @classmethod
    def load(cls, file_name):
        cls.data=pd.read_excel(file_name)
        cls.variables=np.array(cls.data.columns)
        cls.num_set=len(cls.variables)
        print("\nData from file  ", file_name)
        print("Number of variables: %3i" % cls.num_set)
        print("Variable's names: ", cls.variables)
        


# Usage:
file_name="exercise_3_data.xlsx"       
Statistics.load(file_name)
    

# For each column in the dataset, create the corresponding instance 
# and describe it
for iv in Statistics.variables:
    idat=np.array(Statistics.data.eval(iv))
    exec(iv+"=Statistics(iv, idat)")
    eval(iv).describe()





