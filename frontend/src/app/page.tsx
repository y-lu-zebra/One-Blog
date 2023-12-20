'use client'

import * as http from 'http'
import Image from 'next/legacy/image'
import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    http.get('http://localhost:8000/users/', (res) => {
      console.log(res)
    })
  })
  return (
    <>
      <Image
        src="/logo.svg"
        alt="One Blog"
        className="dark:invert"
        width={48}
        height={48}
        priority
      />
      <h1>One Blog</h1>
    </>
  )
}
