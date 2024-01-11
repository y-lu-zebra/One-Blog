import Link from 'next/link'
import React from 'react'

import Header from '@/components/header'
import { fetchCategories, fetchPosts } from '@/lib/api'

export default async function Home() {
  const categories: Category[] = (await fetchCategories()).results as Category[]
  const posts: Post[] = (await fetchPosts()).results as Post[]
  console.log('[slug]: ', posts)

  return (
    <>
      <Header menu={categories}></Header>
      <footer className="">
        <div className="footer-panel">
          &copy;
          <Link className="footer-link" href="categories/">
            Yu Lu
          </Link>
          All Rights Reserved.
        </div>
      </footer>
    </>
  )
}
