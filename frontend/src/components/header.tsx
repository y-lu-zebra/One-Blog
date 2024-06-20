'use client'

import Image from 'next/legacy/image'
import Link from 'next/link'
import React, { useEffect, useRef, useState } from 'react'

import { constants } from '@/lib/constants'
import styles from '@/styles/header.module.css'

// 座右の銘のりすと
const aMottos: string[] = [
  '己の欲せざる所は人に施すこと勿れ',
  '人事を尽くして天命を待つ',
]

/**
 * ヘッダー・コンポーネント
 *
 * @constructor
 */
const Header = () => {
  // 座右の銘へのリファレンス
  const aMottoRef = useRef<HTMLDivElement>(null)
  // スモールヘッダーモードのフラグ
  const [isSmallMode, setIsSmallMode] = useState<boolean>(false)

  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-call,@typescript-eslint/no-unsafe-member-access
    window.scroll(0, 0)
    typing(aMottos[getRandomNum(aMottos.length)])
    toggleSmallMode()
    window.addEventListener('scroll', toggleSmallMode)
    return () => {
      window.removeEventListener('scroll', toggleSmallMode)
    }
  }, [])

  const getRandomNum = (max: number) => {
    return Math.floor(Math.random() * max)
  }
  /**
   * スモールヘッダーモードを切り替える．
   */
  const toggleSmallMode = () => {
    setIsSmallMode(window.scrollY > 5)
  }

  const typing = (sentence: string) => {
    if (aMottoRef.current) {
      aMottoRef.current.textContent = ''
    }
    Array.prototype.forEach.call(sentence, (character: string, idx) => {
      setTimeout(() => {
        if (aMottoRef.current) {
          aMottoRef.current.textContent += character
        }
      }, 200 * ++idx)
    })
  }

  return (
    <>
      {/* ヘッダー */}
      <header className={`${styles.pageHeader} ${isSmallMode && styles.smallHeader}`}>
        <div className={`pageContainer ${isSmallMode && styles.smallContainer}`}>
          {/* LOGO リンク */}
          <Link href={constants.UI_URL_ROOT} scroll={false}>
            <div className={styles.logoImage}>
              <Image
                src="/logo.png"
                layout={'responsive'}
                width={1000}
                height={225}
                alt={process.env.APP_NAME}
                priority
              />
            </div>
          </Link>
        </div>
      </header>
      {/* メインコンテンツの上部マージンを持たせるための要素 */}
      <div className={`transition-all ${isSmallMode ? 'h-14' : 'h-24'}`}></div>
      {/* 座右の銘 */}
      <div className={styles.aMotto}>
        <div className="pageContainer py-1">
          <div ref={aMottoRef} className={styles.aMottoMessage}></div>
        </div>
      </div>
    </>
  )
}

export default Header
