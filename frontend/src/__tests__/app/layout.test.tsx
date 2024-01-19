import { render } from '@testing-library/react'
import RootLayout from '../../app/layout'

describe('Root Layout', () => {
  it('Root Layout Render', () => {
    render(
      <RootLayout>
        <p></p>
      </RootLayout>
    )
  })
})
