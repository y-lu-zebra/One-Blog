import React from 'react'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchPost } from '@/lib/api'
import styles from '@/styles/home.module.css'

interface PostProps {
  params: { slug: number }
}

export default async function Post(props: PostProps) {
  const slug: number = props.params.slug
  console.log('slug: ', slug)
  const post = await fetchPost(slug)

  return (
    <>
      <Header></Header>
      <main className={styles.main}>
        <h1>{post.title}</h1>
        <div className="postContent">{post.content}</div>
      </main>
      <Footer></Footer>
    </>
  )
}
