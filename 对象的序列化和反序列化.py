'''
读写JSON格式的数据
'''

import json
'''
my_dict={
    'name':'wyh',
    'age':20,
    'friends':['logo','yz'],
    'car':[
        {'brand':'保时捷'},
        {'type':'911 gt3 rs'}
    ]
}
with open('data.json','w')as file:
    json.dump(my_dict,file)
'''
'''
with open('data.json','r')as file:
    my_dict=json.load(file)
    print(type(my_dict))
    print(my_dict)
'''
'''
使用网络API获取数据
'''
import requests

api_key = input('请输入你的天行 API key：').strip()

resp = requests.get(
    'https://apis.tianapi.com/enmaxim/index',
    params={'key': api_key},
    timeout=10
)
resp.raise_for_status()  # HTTP 请求失败时抛出异常

data_model = resp.json()

if data_model['code'] == 200:
    sentence = data_model['result']
    print(sentence['en'])
    print(sentence['zh'])
else:
    print('接口调用失败：', data_model['code'], data_model['msg'])