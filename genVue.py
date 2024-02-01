import json

def genVue(json_path):
    # 读取 data.json 文件，并指定编码格式为 utf-8
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    template_path = "templateTable.vue"
    output_path = f"pages/{data['title']}.vue"

    # 获取 title 属性的值
    title = data["title"]

    # 获取除了 title 以外的其他属性
    other_properties = {key: value for key, value in data.items() if key != "title"}

    # 读取 Vue 模板文件的内容
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    # 生成搜索组件并插入到模板中
    search_components = ""
    for key, value in other_properties.items():
        if value.get("searchable"):
            search_component = ""
            if value["searchType"] == "input":
                search_component = f"""
                <el-input
                    class="filter-item"
                    style="width: 320px"
                    v-model="tb.query.{key}"
                    clearable
                    placeholder="请输入{value['name']}"
                    @input="actions.queryAll({{ resetPage: true }})"
                >
                    <template #prepend>{value['name']}</template>
                </el-input>
                """
            elif value["searchType"] == "selectText":
                search_component = f"""
                  <el-select
                    class="filter-item"
                    v-model="tb.query.{key}"
                    style="width: 180px"
                    placeholder="请选择{value['name']}"
                    clearable
                    @change="actions.queryAll({{ resetPage: true }})"
                  >
                    <el-option :key="1" label="状态名1" :value="1" />
                    <el-option :key="2" label="状态名2" :value="2" />
                    <el-option :key="3" label="状态名3" :value="3" />
                    <el-option :key="4" label="状态名4" :value="4" />
                  </el-select>
                """
            elif value["searchType"] == "selectApi":
                search_component = f"""
                  <el-select
                    class="filter-item"
                    clearable
                    filterable
                    v-model="tb.query.{key}"
                    placeholder="请选择{value['name']}"
                    @change="actions.queryAll({{ resetPage: true }})"
                  >
                    <el-option v-for="item in list" :key="item.id" :label="`${{ item.name }}`" :value="item.id!" />
                  </el-select>
                """
            search_components += search_component + "\n"

    # 生成表格列并插入到模板中
    columns = ""
    for key, value in other_properties.items():
        if key != "title" and value.get("showInTable"):
            column = ""
            if value["showType"] == "string":
                column = f"""
                <el-table-column label="{key}" align="center" min-width="120">
                  <template #default="scope: ElTableRow<{title}Model>">
                     {{{{ scope.row.{key}}}}}
                  </template>
                  </el-table-column>
                """
            elif value["showType"] == "status":
                column = f"""
                  <el-table-column label="{key}" align="center" min-width="120">
                    <template #default="scope: ElTableRow<{title}Model>">
                      <el-tag v-if="scope.row.{key} == 1" type="info">状态1</el-tag>
                      <el-tag v-if="scope.row.{key} == 2" type="danger">状态2</el-tag>
                      <el-tag v-if="scope.row.{key} == 3" type="warning">状态3</el-tag>
                      <el-tag v-if="scope.row.{key} == 4" type="success">状态4</el-tag>
                    </template>
                  </el-table-column>
                """
            elif value["showType"] == "img":
                column = f"""
                  <el-table-column label="{key}" align="center" width="100">
                    <template #default="scope: ElTableRow<{title}Model>">
                      <img
                        :src="qiniuUrl(scope.row.{key}, [200, 200])"
                        alt=""
                        style="height: 66px; width: 66px; object-fit: cover; display: inline-block" />
                    </template>
                  </el-table-column>
                """
            columns += column + "\n"
            columns += f"""
                  <template #default="scope: ElTableRow<{title}Model>">
                      <el-button
                          type="primary"
                          size="small"
                          @click="tb.addDialogVisible = true"
                      >查看弹窗</el-button>
                  </template>
              """

    #生成引用内容
    import_components = ""
    has_img_show_type = False
    for key, value in other_properties.items():
        if value.get("showType") == "img" and not has_img_show_type:
            import_components += "import { qiniuUrl } from '@/config/qiniu'\n"
            import_components += "import Upload from '@/widget/upload-qiniu/index.vue'\n\n"
            has_img_show_type = True

    # 同时替换模板中的 "TableName" 和 "tableName" 为 title 属性的值
    template = template.replace("TableName", title).replace("tableName", title)

    # 替换模板中的搜索组件
    template = template.replace("<!-- 搜索 -->", search_components)

    # 替换模板中的表格列
    template = template.replace("<!-- 内容 -->", columns)

    # 替换模板中的引用
    template = template.replace("/** 引用 */", import_components)

    # 将生成的模板写入新的文件中
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(template)

# 使用示例
genVue("json/data.json")