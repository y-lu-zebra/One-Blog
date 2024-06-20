import { Category } from '@/types/category'

/**
 * 投稿インターフェイス
 */
export interface Post {
  id: number
  title: string
  overview: string
  content: string
  category: Category
  tags: Tag[]
  dateCreated: string
  dateUpdated: string
  metaTitle: string
  metaDescription: string
  metaKeywords: string
}
