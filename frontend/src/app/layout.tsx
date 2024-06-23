import 'tw-elements-react/dist/css/tw-elements-react.min.css'
import '@/styles/globals.css'

import type { Metadata } from 'next'
import { Kosugi_Maru } from 'next/font/google'
import { Suspense } from 'react'
import React from 'react'

import GoogleAnalytics from '@/components/ga'

const oneFont = Kosugi_Maru({ weight: '400', subsets: ['latin'] })

export const metadata: Metadata = {
  title: process.env.APP_NAME,
  description: process.env.APP_DESCRIPTION,
  keywords: process.env.APP_KEYWORDS,
  openGraph: {
    title: process.env.APP_NAME,
    description: process.env.APP_DESCRIPTION,
    images: process.env.APP_URL + '/ogp.png',
    locale: 'ja_JP',
    type: 'website',
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ja">
      <body className={oneFont.className}>
        <Suspense>
          <GoogleAnalytics />
        </Suspense>
        {children}
      </body>
    </html>
  )
}
