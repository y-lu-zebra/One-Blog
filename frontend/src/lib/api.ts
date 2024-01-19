export const fetchCategories = async (): Promise<ListResponse> => {
  const res: Response = await fetch(`${process.env.API_URL}/categories/?limit=4`)
  return (await res.json()) as Promise<ListResponse>
}

export const fetchPosts = async (): Promise<ListResponse> => {
  const res: Response = await fetch(`${process.env.API_URL}/posts/`)
  return (await res.json()) as Promise<ListResponse>
}

export const fetchPost = async (postId: number): Promise<Post> => {
  const res: Response = await fetch(`${process.env.API_URL}/posts/${postId}`)
  return (await res.json()) as Promise<Post>
}
