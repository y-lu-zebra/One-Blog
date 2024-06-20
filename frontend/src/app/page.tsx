import Link from 'next/link'
import React from 'react'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchPosts } from '@/lib/api'
import styles from '@/styles/home.module.css'

export const dynamic = 'force-dynamic'
export default async function HomePage() {
  const posts: Post[] = (await fetchPosts()).results as Post[]

  return (
    <>
      <Header />
      <main>
        <div className="pageContainer">
          <div className={styles.postList}>
            {posts.map((post: Post, idx: number) => {
              const dateUpdated: Date = new Date(post.date_updated)
              const dateUpdatedStr: string = `${dateUpdated.getFullYear()}.${(
                '0' +
                ((dateUpdated.getMonth() % 12) + 1)
              ).slice(-2)}.${dateUpdated.getDate()}`
              return (
                <Link
                  key={idx}
                  href={`/${post.id}`}
                  className={styles.postCard}
                  scroll={false}
                >
                  <div className={styles.shutter}>
                    <span className={styles.date}>{dateUpdatedStr}</span>
                    <h3>{post.title}</h3>
                  </div>
                  <p className={styles.overview}>{post.overview}</p>
                </Link>
              )
            })}
          </div>
          <ul></ul>
        </div>
      </main>
      <Footer />
    </>
  )
}
