import Link from 'next/link'
import React from 'react'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchPosts } from '@/lib/api'
import styles from '@/styles/home.module.css'

export default async function Home() {
  const posts: Post[] = (await fetchPosts()).results as Post[]
  console.log('[slug]: ', posts)

  return (
    <>
      <Header></Header>
      <main className="main">
        <div className="mainContainer">
          <ul>
            {posts.map((post: Post, idx: number) => {
              return (
                <li key={idx} className="py-5">
                  <Link href={`/${post.id}`} className={styles.listLink}>
                    {post.title}
                  </Link>
                </li>
              )
            })}
          </ul>
        </div>
      </main>
      <Footer></Footer>
    </>
  )
}
