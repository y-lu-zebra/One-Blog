import 'tw-elements-react/dist/css/tw-elements-react.min.css'
import '@/styles/globals.css'

import type { Metadata } from 'next'
import React from 'react'

export const metadata: Metadata = {
  title: 'One Blog',
  description: 'One Blog',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  )
}
