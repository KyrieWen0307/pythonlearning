"""
BMI计算器
author:温宇豪
version:1.2
"""
height = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
bmi = weight/(height/100)**2
if bmi < 18.5:
    print('过轻')
elif bmi< 24:
    print('正常')
elif bmi<27:
    print('过重')
elif bmi<30:
    print('轻度肥胖')
elif bmi<35:
    print('中度肥胖')
else:
    print('重度肥胖')

"""
响应状态码，用match和case构造分支结构
"""
status_code=int(input('请输入响应状态码：'))
match status_code:
    case 200:
        description = '请求成功'
    case 400:
        description = '请求参数错误'
    case 401:
        description = '未授权'
    case 403:
        description = '禁止访问'
    case 404 | 405:
        description = '请求资源不存在'
    case 500:
        description = '服务器内部错误'
    case _:
        description = '未知状态码'
print('状态码描述：',description)

"""
分段函数求值
author:温宇豪
version:1.0
"""
x = float(input('请输入x：'))
if x>1:
    y=3*x-5
elif x>-1:
    y=x+2
else:
    y=5*x+3
print('x=%d,y=%.2f'%(x,y))