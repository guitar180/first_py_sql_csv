import pandas as pd
import matplotlib.pyplot as plt
from unicodedata import category
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv(r'D:\PyCharm 2025.3.1\project\test.csv')
print(df)
print(f'总行数{len(df)}')
category_sum = df.groupby('类别')['金额'].sum()
print('各类别支出:')
print(category_sum)
print()
max_category = category_sum.idxmax()
max_amount = category_sum.max()
print(f"支出最多{max_category},花了{max_amount}元")
print()
category_sum.plot(kind='bar')
plt.title('paycheck')
plt.xlabel('category')
plt.ylabel('amount')
plt.show()
