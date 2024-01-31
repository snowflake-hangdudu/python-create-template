import Queryable, { BasicQueryParams } from "@/public/queryable";
import http from "@/config/axios";
const { request } = http;

/** 模型 */
export interface TableNameModel {
  /** interface */
}

/** 搜索条件 */
export interface TableNameQueryParmas extends BasicQueryParams {
  /** searchable */
}

/** 数据源，增删查改等请求 */
export default class TableNameQuery extends Queryable<
  TableNameModel,
  TableNameQueryParmas
> {
  // 可设置父ID，例如查询用户下的全部文章
  // constructor(id) {
  //     super();
  //     this.id = id;
  // }

  /** 对象名称 */
  get objectName(): string {
    return '/** tableName */';
  }

  // 默认的内容
  get defaultObject(): TableNameModel {
    return {
      /** property */
    };
  }

  // 读取正在输入的数据，用于表单校验
  _valueGetter: () => Partial<TableNameModel> = () => ({});

  // 已输入的数据的Getter
  get currentEditRow(): Partial<TableNameModel> {
    return this._valueGetter();
  }

  // 表单规则
  get rules() {
    return {
      /** rules */
    };
  }

  // 查询全部
  async all(params: TableNameQueryParmas) {
    let res = await request({
      url: `/api/hospital/tableName/list`,
      method: "get",
      params: {
        pageNum: params.pageNum,
        pageSize: params.pageSize,
        /** params */
      },
    });
    if (res.data.count == undefined) return res.data;
    return {
      data: res.data.rows,
      total: res.data.count,
    };
  }

  // // 上传修改
  // async edit(obj: TableNameModel) {
  //   console.log("修改", obj);
  //   obj = Object.assign({}, obj);
  //   let id = obj.id;
  //   delete obj.id;
  //   return request({
  //     url: `/api/hospital/tableName/${id}`,
  //     method: "put",
  //     data: obj,
  //   });
  // }

  // // 添加
  // async add(obj: TableNameModel) {
  //   delete obj.id;
  //   return request({
  //     url: "/api/hospital/tableName",
  //     method: "post",
  //     data: obj,
  //   });
  // }

  // // 通过id删除
  // async deleteObj(obj: TableNameModel) {
  //   return request({
  //     url: `/api/hospital/tableName/${obj.id}`,
  //     method: "delete",
  //   });
  // }
}
