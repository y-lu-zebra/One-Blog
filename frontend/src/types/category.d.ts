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
  meta_title: string
  // メタディスクリプション
  meta_description: string
  // メタキーワード
  meta_keywords: string
  // 子カテゴリー
  children: Category[]
}
