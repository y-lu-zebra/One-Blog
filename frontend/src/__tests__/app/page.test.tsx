import { render } from '@testing-library/react'
import HomePage from '../../app/page'

jest.mock(
  '../../lib/api',

  () => ({
    fetchPosts: () =>
      new Promise((resolve, reject) =>
        resolve({
          results: [
            {
              title: 'test',
            },
          ],
        })
      ),
  })
)

describe('Home Page', () => {
  it('Home Page Render', async () => {
    const jsx = await HomePage()
    render(jsx)
  })
})
