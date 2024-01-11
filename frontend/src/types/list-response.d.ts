/**
 * 一覧レスポンスインターフェイス
 */
interface ListResponse {
  count: number
  next: string | null
  previous: string | null
  results: Category[] | Post[] | []
}
