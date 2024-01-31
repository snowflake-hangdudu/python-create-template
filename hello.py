import json

# 读取 data.json 文件
with open("json/data.json", "r") as file:
    data = json.load(file)
# 获取 title 属性的值
title = data["title"]

# 获取除了 title 以外的其他属性
other_properties = {key: value for key, value in data.items() if key != "title"}

# 生成必填规则
rules_code = ""
for property_name, property_info in other_properties.items():
    required = property_info.get("required", False)
    message = property_info.get("message", "必填")
    rules_code += f"\n  /** {property_name} */\n"
    rules_code += f"  {property_name}: [{{ required: {str(required).lower()}, message: '{message}', trigger: 'blur' }}],"

# 生成进行筛选的属性
optional_properties_code = ""
for property_name, property_info in other_properties.items():
    searchable = property_info.get("searchable", False)
    if searchable:
        # optional_properties_code += f"\n  /** {property_name} */\n"
        optional_properties_code += f"  {property_name}?: {property_info['type']};\n"



# 生成搜索属性
searchable_properties_code = ""
for property_name, property_info in other_properties.items():
    searchable = property_info.get("searchable", False)
    if searchable:
        searchable_properties_code += f"{property_name}: params.{property_name},\n"


# 读取模板 TypeScript 文件
with open("template.ts", "r", encoding="utf-8") as file:
    template_content = file.read()

# 替换模板文件中的 TableName
new_content = template_content.replace("TableName", title)

# 替换模板文件中的对象名称
new_content = new_content.replace("/** tableName */", title)

# 替换模板文件中的规则
new_content = new_content.replace("/** rules */", rules_code)

# 生成其他属性的可选属性
properties_code = "\n".join([f"  {property_name}?: {property_info['type']};" for property_name, property_info in other_properties.items()])
new_content = new_content.replace("/** interface */", properties_code)


# 替换模板文件中的可选属性
new_content = new_content.replace("/** searchable */", optional_properties_code)

# 替换模板文件中的搜索属性
new_content = new_content.replace(" /** params */", searchable_properties_code)

# 将替换后的内容写入新的文件
with open(f"ts/{title}.ts", "w", encoding="utf-8") as file:
    file.write(new_content)