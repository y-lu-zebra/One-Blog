import Link from 'next/link'
import React from 'react'
import Markdown from 'react-markdown'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { tomorrow } from 'react-syntax-highlighter/dist/esm/styles/prism'
import rehypeRaw from 'rehype-raw'
import remarkGfm from 'remark-gfm'

import Footer from '@/components/footer'
import Header from '@/components/header'
import { fetchPost } from '@/lib/api'
import styles from '@/styles/post.module.css'
import { Post } from '@/types/post'

interface PostProps {
  params: { slug: number }
  children: React.ReactElement
  className?: string
}

export const dynamic = 'force-dynamic'

export const generateMetadata = async (props: PostProps) => {
  const slug = props.params.slug
  const post: Post = await fetchPost(slug)

  return {
    title: post.metaTitle || post.title,
    description: post.metaDescription,
    keywords: post.metaKeywords,
  }
}

const PostPage = async (props: PostProps) => {
  const slug: number = props.params.slug
  const post: Post = await fetchPost(slug)
  const dateCreated: Date = new Date(post.dateCreated)
  const dateCreatedStr: string = `${dateCreated.getFullYear()}.${(
    '0' +
    ((dateCreated.getMonth() % 12) + 1)
  ).slice(-2)}.${dateCreated.getDate()}`
  const dateUpdated: Date = new Date(post.dateUpdated)
  const dateUpdatedStr: string = `${dateUpdated.getFullYear()}.${(
    '0' +
    ((dateUpdated.getMonth() % 12) + 1)
  ).slice(-2)}.${dateUpdated.getDate()}`

  return (
    <>
      <Header />
      <main>
        <div className={styles.pageTitlePanel}>
          <div className="pageContainer">
            <h1 className={styles.pageTitle}>{post.title}</h1>
          </div>
        </div>
        <div className={styles.pageContent}>
          <div className="pageContainer">
            <div className={styles.pageMeta}>
              <span className={styles.dateCreated}>{dateCreatedStr}</span>
              <span className={styles.dateUpdated}>{dateUpdatedStr}</span>
              {post.category.name && (
                <span className={styles.category}>{post.category.name}</span>
              )}
              {post.tags.length > 0 && (
                <span className={styles.pageTags}>
                  {post.tags.map((tag: Tag, idx: number) => (
                    <>
                      <Link key={idx} href="">
                        {tag.name}
                      </Link>
                      {post.tags.length - idx !== 1 && ' , '}
                    </>
                  ))}
                </span>
              )}
            </div>
            {post.overview && (
              <div className={styles.pageOverview}>{post.overview}</div>
            )}
            <div className={styles.postContent}>
              <Markdown
                rehypePlugins={[rehypeRaw, remarkGfm]}
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
        </div>
      </main>
      <Footer />
    </>
  )
}

export default PostPage
