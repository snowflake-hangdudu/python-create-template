
import os
from genTS import genTS
from genVue import genVue
import sys

def genFiles(json_file):
    genTS(json_file)
    genVue(json_file)

    
# 获取终端输入的参数列表
args = sys.argv[1:]



# 如果没有传入任何参数，则遍历整个文件夹生成
if len(args) == 0:
    # 遍历json文件夹下的文件
    for root, dirs, files in os.walk('json'):
        # 遍历文件
        for file in files:
            # 判断文件是否以.json结尾且不是data.json
            if file.endswith('.json') and file != 'data.json':
                # 获取文件路径
                file_path = os.path.join(root, file)
                # 调用genFiles函数生成文件
                genFiles(file_path)
# 如果传入了参数，则根据参数生成单个文件
else:
    json_file = args[0]
    genFiles(json_file)

print(args)