# import pandas also need xlrd/xlwt
import numpy as np
import pandas as pd
EXCEL_FILE = './excel.xls'

rg = np.random.Generator(np.random.PCG64())
data = rg.integers(1,15,size=(5, 4))
# https://www.numpy.org.cn/reference/routines/random.html#quick-start
# integers replaces both randint and the deprecated random_integers
# data = np.random.randint(1, 15, size=(5, 4))
df = pd.DataFrame(data, columns=list('ABCD'))
print(df)
print('-' * 20)

# df['NSCAP'] = df['D'].apply(lambda x: x+1)
df['X'] = df.apply(lambda x: sum(x),axis=1)
print(df)
print('-' * 20)

df.to_excel(EXCEL_FILE, index=None)
