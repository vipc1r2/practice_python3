
import json
data = {
    'name' : 'myname',
    'age' : 100,
}
json_str = json.dumps(data)  # 通过json.dumps(<dict>)转换的字典对象，最后得到的是一个字符串对象
print(json_str)
print(type(json_str))
# '{"name": "myname", "age": 100}'是字符串


# json.loads将一个JSON编码的字符串转换回一个Python数据结构
data = json.loads(json_str)
print(data)
print(type(data))

# json.dump() 和 json.load() 来编码和解码JSON数据,用于处理文件。
with open('1.json', 'w') as f:
    json.dump(data, f)

with open('1.json', 'r') as f:
    data = json.load(f)
    print('=='*10)
    print(data)