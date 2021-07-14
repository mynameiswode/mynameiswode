
# coding: utf-8

# In[1]:

# pip install xlrd==1.2.0

import pandas as pd
from pandas import DataFrame
import time

T=time.strftime('%Y-%m-%d',time.localtime(time.time()))

# T='2019-01-28'#不固定就注释掉

df= pd.read_excel(T+".xlsx")
mh= pd.read_excel("湖南门户用户数据_2019-01-23.xls")
baimingdan= pd.read_excel("I用考核白名单.xlsx")

df["联系电话"]=df["联系电话"].fillna(-1).astype('int64')
df.loc[df["爱问登陆次数"] == 0, "是否登录"] = "没有登录"
df.loc[df["爱问登陆次数"] > 0, "是否登录"] = "登录过"

df.loc[df["三级部门"] == '客户经营中心（电子渠道运营中心）', "三级部门"] = "客户经营中心（电渠）"
df.loc[df["三级部门"] == '益阳分公司', "三级部门"] = df["四级部门"]
df.loc[df["三级部门"] == '无线维护中心（虚拟）', "三级部门"] = '无线维护中心'
df.loc[df["三级部门"] == '本部客户服务部（虚拟）', "三级部门"] = '本部客户服务部'
df.loc[df["三级部门"] == '客户服务部', "三级部门"] = '本部客户服务部'
df.loc[df["三级部门"] == '新兴业务运营中心(虚拟)', "三级部门"] = '新兴业务运营中心'

df = DataFrame(df,columns=["是否登录","姓名","联系电话","三级部门","四级部门","门户账号","员工代码","门户系统ID","爱问登陆次数"])
df=df.sort_values(["三级部门","是否登录","四级部门"],ascending=[True,False,False])

# mh= pd.read_excel("湖南门户用户数据_2019-01-23.xls")
# baimingdan= pd.read_excel("I用考核白名单.xlsx")
# 开始取差集,添加两次重复,然后删掉两次以上重复的达到取差集的目的
mh = mh.append(baimingdan)
mh = mh.append(baimingdan)
mh = mh.drop_duplicates(subset=['门户UID'],keep=False)#去掉重复2次和3+次的
mh['门户系统ID']=mh['门户UID']
mh=DataFrame(mh,columns=['门户系统ID', '性别名称', 'HRID'])
mh=mh[mh['HRID'].notnull()]
# mh.columns
mg=pd.merge(df,mh)#取交集
# df[(df.是否登录 == '没有登录')&(df["姓名"] == '刘有勇')].head()
# df["三级部门"].unique()
tongji=pd.crosstab(mg.三级部门,mg.是否登录, margins=True,margins_name='合计')#交叉表
tongji=DataFrame(tongji,columns=['没有登录','登录过','合计'])
tongji["百分比"] =(tongji["登录过"]/tongji["合计"])
tongji3=tongji.loc[["合计"]]
tongji2=tongji.drop(index=["合计"])
tongji=tongji2.sort_values("百分比",ascending=False)
tongji=tongji.append(tongji3)

tongji["百分比"]=tongji["百分比"].map(lambda x:format(x,'9.2%'))#格式化百分数9位长度
mg["联系电话"]=mg["联系电话"].map(lambda x:format(x,''))#格式化电话号码成文本格式到excel

writer = pd.ExcelWriter('I用登录'+str(T)+'情况.xlsx')
tongji.to_excel(writer, sheet_name='汇总', index=True,index_label='部门及经营单元', header=True,freeze_panes=(1,5))
mg.to_excel(writer, sheet_name='明细', index=False, header=True,freeze_panes=(1,15))
writer.save()
# for index, row in tongji.iterrows(): print(index ,row[0])
tongji.head(40)
# mg.info()
print(tongji.head(40))
print('保存名为:','I用登录'+str(T)+'情况.xlsx')

