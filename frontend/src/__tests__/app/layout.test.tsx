import { render } from '@testing-library/react'
import RootLayout from '../../app/layout'
import { useSearchParams } from 'next/navigation'

jest.mock('next/navigation', () => ({
  usePathname: () => '',
  useSearchParams: () => new URLSearchParams(''),
}))
jest.mock('next/font/google', () => ({
  Kosugi_Maru: () => ({
    style: {
      fontFamily: 'mocked',
    },
  }),
}))

describe('Root Layout', () => {
  it('Root Layout Render', () => {
    render(
      <RootLayout>
        <p></p>
      </RootLayout>
    )
  })
})
