a={'one':1,'two':2,'three':3}

#a.setdefault('four',4)
#如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
a.setdefault('one',2)
a.setdefault('four',[]).append('1')
a.setdefault('four',[]).append('2')
print(a)

lista=[
    {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02'}
]
case_list={}
# for i in lista:
#     case_list.setdefault('case_info',[]).append(i)
# print(case_list)

for i in lista:
    case_list.setdefault(i['测试用例编号'],[]).append(i)

for k,v in case_list.items():
    print(k,v)

#字典转成列表
case_dict={}
for i in lista:
    case_dict.setdefault(i['测试用例编号'],[]).append(i)
case_list=[]
for k,v in case_dict.items():
    case_dict={}
    case_dict['case_name']=k
    case_dict['case_info']=v
    case_list.append(case_dict)

for i in case_list:
    print(i)