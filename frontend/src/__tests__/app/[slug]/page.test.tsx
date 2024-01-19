import { render } from '@testing-library/react'
import PostPage from '../../../app/[slug]/page'

jest.mock(
  '../../../lib/api',

  () => ({
    fetchPost: () =>
      new Promise((resolve, reject) =>
        resolve({
          title: 'test',
          content: '```python\n```\n',
        })
      ),
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
