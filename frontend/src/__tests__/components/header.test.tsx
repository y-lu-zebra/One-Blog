import { render } from '@testing-library/react'
import Header from '../../components/header'

window.scroll = jest.fn()

describe('Header Component', () => {
  it('Header Component Render', () => {
    render(<Header />)
  })
})
