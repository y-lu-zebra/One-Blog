/**
 * タグインターフェイス
 */
interface Tag {
  // タグ ID
  id: number
  // タグ名
  name: string
  // タグ別名
  alias: string
  // メタタイトル
  metaTitle: string
  // メタディスクリプション
  metaDescription: string
  // メタキーワード
  metaKeywords: string
  // 子カテゴリー
  children: Category[]
}
