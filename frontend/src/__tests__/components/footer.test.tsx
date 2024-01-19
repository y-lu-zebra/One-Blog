import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import Footer from '../../components/footer'

describe('Footer Component', () => {
  it('Footer Component Render', () => {
    render(<Footer />)
    expect(screen.getByText('Yu Lu')).toBeInTheDocument()
  })
})
