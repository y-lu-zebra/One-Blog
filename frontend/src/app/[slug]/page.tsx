import React from 'react'
import Markdown from 'react-markdown'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { tomorrow } from 'react-syntax-highlighter/dist/esm/styles/prism'
import remarkGfm from 'remark-gfm'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchPost } from '@/lib/api'
import styles from '@/styles/post.module.css'

interface PostProps {
  params: { slug: number }
  children: React.ReactElement
  className?: string
}

export const dynamic = 'force-dynamic'

export default async function PostPage(props: PostProps) {
  const slug: number = props.params.slug
  console.log('slug: ', slug)
  const post = await fetchPost(slug)

  return (
    <>
      <Header></Header>
      <main className="main">
        <div className="mainContainer">
          <h1 className={styles.postTitle}>{post.title}</h1>
          <div className={styles.postContent}>
            <Markdown
              remarkPlugins={[remarkGfm]}
              components={{
                code(props) {
                  const { children, className } = props
                  const match = /language-(\w+)/.exec(className || '')
                  return match ? (
                    <SyntaxHighlighter
                      PreTag="div"
                      language={match[1]}
                      style={tomorrow}
                      showLineNumbers={true}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className}>{children}</code>
                  )
                },
              }}
            >
              {post.content}
            </Markdown>
          </div>
        </div>
      </main>
      <Footer></Footer>
    </>
  )
}

export async function generateMetadata(props: PostProps) {
  const slug = props.params.slug
  const post: Post = await fetchPost(slug)

  return {
    title: post.metaTitle || post.title,
    description: post.metaDescription,
    keywords: post.metaKeywords,
  }
}
