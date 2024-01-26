export interface basicQueryParams{
    pageNum?:number,
    pageSize?:number
}

export interface PagedData<T> { total: number, data: T[] }

