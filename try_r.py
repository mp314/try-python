#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R"""


import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np   # linear algebra
# We'll also import seaborn, a Python graphing library
#import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
#warnings.filterwarnings("ignore")
import seaborn as sns
#import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)
print(df.head())
print(df.tail(3))
print(df.shape)

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)
print(df2.dtypes)
