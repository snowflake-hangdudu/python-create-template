import Queryable, { BasicQueryParams } from "@/public/queryable";
import http from "@/config/axios";
const { request } = http;

/** 模型 */
export interface AdminModel {
    name?: string;
  age?: number;
  email?: string;
}

/** 搜索条件 */
export interface AdminQueryParmas extends BasicQueryParams {
    name?: string;
  age?: number;
  email?: string;

}

/** 数据源，增删查改等请求 */
export default class AdminQuery extends Queryable<
  AdminModel,
  AdminQueryParmas
> {
  // 可设置父ID，例如查询用户下的全部文章
  // constructor(id) {
  //     super();
  //     this.id = id;
  // }

  /** 对象名称 */
  get objectName(): string {
    return 'Admin';
  }

  // 默认的内容
  get defaultObject(): AdminModel {
    return {
      /** property */
    };
  }

  // 读取正在输入的数据，用于表单校验
  _valueGetter: () => Partial<AdminModel> = () => ({});

  // 已输入的数据的Getter
  get currentEditRow(): Partial<AdminModel> {
    return this._valueGetter();
  }

  // 表单规则
  get rules() {
    return {
      
  /** name */
  name: [{ required: true, message: '必填', trigger: 'blur' }],
  /** age */
  age: [{ required: true, message: '必填', trigger: 'blur' }],
  /** email */
  email: [{ required: true, message: '必填', trigger: 'blur' }],
    };
  }

  // 查询全部
  async all(params: AdminQueryParmas) {
    let res = await request({
      url: `/api/hospital/tableName/list`,
      method: "get",
      params: {
        pageNum: params.pageNum,
        pageSize: params.pageSize,
       name: params.name,
age: params.age,
email: params.email,

      },
    });
    if (res.data.count == undefined) return res.data;
    return {
      data: res.data.rows,
      total: res.data.count,
    };
  }

  // // 上传修改
  // async edit(obj: AdminModel) {
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
  // async add(obj: AdminModel) {
  //   delete obj.id;
  //   return request({
  //     url: "/api/hospital/tableName",
  //     method: "post",
  //     data: obj,
  //   });
  // }

  // // 通过id删除
  // async deleteObj(obj: AdminModel) {
  //   return request({
  //     url: `/api/hospital/tableName/${obj.id}`,
  //     method: "delete",
  //   });
  // }
}
