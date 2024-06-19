import { render } from '@testing-library/react'
import PostPage, { generateMetadata } from '../../../app/[slug]/page'

jest.mock(
  '../../../lib/api',

  () => ({
    fetchPost: (postId: number) => {
      if (postId == 1) {
        return new Promise((resolve, reject) =>
          resolve({
            title: 'test',
            content: '```python\n```\n',
            meta_title: 'meta title',
            meta_description: 'meta description',
            meta_keywords: 'meta keywords',
          })
        )
      } else {
        return new Promise((resolve, reject) =>
          resolve({
            title: 'test',
            content: '```python\n```\n',
            meta_title: '',
            meta_description: 'meta description',
            meta_keywords: 'meta keywords',
          })
        )
      }
    },
  })
)

describe('Post Page', () => {
  it('Post Page Render', async () => {
    const jsx = await PostPage({
      params: { slug: 1 },
      children: <></>,
      className: 'python',
    })
    render(jsx)
  })
})

describe('Get Post Page Generate Meta Data', () => {
  it('Get Meta Data 1', async () => {
    const metaData = await generateMetadata({
      params: { slug: 1 },
      children: <></>,
      className: 'python',
    })
    expect(metaData).toEqual({
      title: 'meta title',
      description: 'meta description',
      keywords: 'meta keywords',
    })
  })

  it('Get Meta Data 2', async () => {
    const metaData = await generateMetadata({
      params: { slug: 2 },
      children: <></>,
      className: 'python',
    })
    expect(metaData).toEqual({
      title: 'test',
      description: 'meta description',
      keywords: 'meta keywords',
    })
  })
})
