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

interface PostProps {
  params: { slug: number }
  children: React.ReactElement
  className?: string
}

export const dynamic = 'force-dynamic'

const PostPage = async (props: PostProps) => {
  const slug: number = props.params.slug
  console.log('slug: ', slug)
  const post = await fetchPost(slug)
  console.log(post)
  const dateUpdated: Date = new Date(post.date_updated)
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
              <span className={styles.date}>{dateUpdatedStr}</span>
            </div>
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

export async function generateMetadata(props: PostProps) {
  const slug = props.params.slug
  const post: Post = await fetchPost(slug)

  return {
    title: post.meta_title || post.title,
    description: post.meta_description,
    keywords: post.meta_keywords,
  }
}

export default PostPage
