<template>
  <div class="app-container">
    <div class="filter-container-flex">
      <!-- 搜索 -->
    </div>
    <el-table
      v-loading="tb.listLoading"
      :data="tb.list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <!-- 内容 -->
      <el-table-column
        class-name="status-col"
        fixed="right"
        label="操作"
        align="center"
        width="120"
      >
        <template #default="scope: ElTableRow<OrderModel>">
          <el-button
            type="primary"
            size="small"
            @click="tb.addDialogVisible = true"
            >查看弹窗</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <!-- 翻页 -->
    <div class="pagination-container" v-if="tb.total">
      <el-pagination
        v-model:current-page="tb.query.pageNum"
        :page-sizes="[5, 20, 30, 50, 100, 200]"
        v-model:page-size="tb.query.pageSize"
        :total="tb.total"
        background
        layout="total, sizes, prev, pager, next, jumper"
        @size-change="(v: number) => actions.sizeChange(v)"
        @current-change="(v: number) => actions.pageChange(v)"
      />
    </div>
    <!-- 添加/删除数据的弹窗 -->
    <el-dialog
      v-model="tb.addDialogVisible"
      :title="actions.dialogTitle"
      width="620px"
      @closed="tb.isNew = false"
      ><div class="dialog-container">
        <div class="dialog-footer">
          <el-button @click="tb.addDialogVisible = false">关闭弹窗</el-button>
        </div>
      </div>
    </el-dialog>
  </div>
</template>
<script lang="ts" setup>
import refTable from "@/public/basic-table";
import { Plus } from "@element-plus/icons-vue";
import TableNameQuery, {
  TableNameModel,
  TableNameQueryParmas,
} from "../../api/tableName";
/** 引用 */

/** 创建表格，与表格相关操作 */
const [tb, actions] = refTable<
  TableNameModel,
  TableNameQueryParmas,
  TableNameQuery
>(new TableNameQuery(), {
  // 默认的搜索值
});
</script>

<style lang="scss" scoped>
.dialog-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  .dialog-footer {
    margin-top: auto;
    display: flex;
    justify-content: flex-end;
  }
}
</style>
