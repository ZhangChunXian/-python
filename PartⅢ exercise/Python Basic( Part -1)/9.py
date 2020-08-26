'''
exam_st_date = (21, 8, 2014)
#%%
print(f"{exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
'''
exam_st_date = (21, 8, 2014)
print("The examination will start from : %i/%i/%i"%exam_st_date)|

# %% 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import statsmodels as sm

a = np.random.randn(100, 100)

%timeit np.dot(a, a)
#%%
%pwd
#%%
foo = %pwd

#%%
%matplotlib inline

import matplotlib.pyplot as plt
plt.plot(np.random.rand(50).cumsum(),)