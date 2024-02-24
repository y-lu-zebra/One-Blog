import 'tw-elements-react/dist/css/tw-elements-react.min.css'
import '@/styles/globals.css'

import type { Metadata } from 'next'
import { Suspense } from 'react'
import React from 'react'

import GoogleAnalytics from '@/components/ga'

export const metadata: Metadata = {
  title: process.env.APP_NAME,
  description: process.env.APP_DESCRIPTION,
  keywords: process.env.APP_KEYWORDS,
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ja">
      <body>
        <Suspense>
          <GoogleAnalytics />
        </Suspense>
        {children}
      </body>
    </html>
  )
}
