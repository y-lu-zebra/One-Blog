import Link from 'next/link'
import React from 'react'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchCategories, fetchPosts } from '@/lib/api'
import styles from '@/styles/home.module.css'
import { Category } from '@/types/category'

export default async function Home() {
  const categories: Category[] = (await fetchCategories()).results as Category[]
  const posts: Post[] = (await fetchPosts()).results as Post[]
  console.log('[slug]: ', posts)

  return (
    <>
      <Header></Header>
      <main className={styles.main}>
        <ul>
          {posts.map((post: Post, idx: number) => {
            return (
              <li key={idx} className="py-5">
                <Link href={`/${post.id}`}>{post.title}</Link>
              </li>
            )
          })}
        </ul>
      </main>
      <Footer></Footer>
    </>
  )
}
