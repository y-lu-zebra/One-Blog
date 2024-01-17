import { CategoryType } from '@/types/category-type'

/**
 * カテゴリーインターフェイス
 */
interface Category {
  // カテゴリー ID
  id: number
  // カテゴリー名
  name: string
  // タイプ
  type: CategoryType
  // カテゴリー別名
  alias: string
  // URL
  url: string
  // メタタイトル
  metaTitle: string
  // メタディスクリプション
  metaDescription: string
  // メタキーワード
  metaKeywords: string
  // 子カテゴリー
  children: Category[]
}
