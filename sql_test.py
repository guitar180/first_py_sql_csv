from sqlite3 import Cursor

import pandas as pd
import sqlite3
# 创建数据库
conn = sqlite3.connect('mydata.db')
# 读取csv
df = pd.read_csv('test.csv')
cursor = conn.cursor()
sql = '''
select 类别, sum(金额) as 总金额
from 支出表
group by 类别
order by 总金额 desc
'''
cursor.execute(sql)
result = cursor.fetchall()

print("各项支出:")
for row in result:
    print(f"{row[0]},{row[1]}元")
conn.close()

#把数据存入数据库
# df.to_sql('支出表', con=conn, if_exists='replace', index=False)
# print('数据已导入，共',len(df),'条记录')
# conn.close()
