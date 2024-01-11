import { fetchPost } from '@/lib/api'

interface PostProps {
  params: { slug: number }
}

export default async function Post(props: PostProps) {
  const slug: number = props.params.slug
  console.log('slug: ', slug)
  const post = await fetchPost(slug)

  return <>{post.content}</>
}
