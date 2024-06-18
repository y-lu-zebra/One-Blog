'use client'

import Image from 'next/legacy/image'
import Link from 'next/link'
import React, { useEffect, useState } from 'react'

import { constants } from '@/lib/constants'
import styles from '@/styles/header.module.css'

/**
 * ヘッダー・コンポーネント
 *
 * @constructor
 */
const Header = () => {
  // スモールヘッダーモードのフラグ
  const [isSmallMode, setIsSmallMode] = useState<boolean>(false)

  useEffect(() => {
    window.addEventListener('scroll', toggleSmallMode)
    return () => {
      window.removeEventListener('scroll', toggleSmallMode)
    }
  }, [])

  /**
   * スモールヘッダーモードを切り替える．
   */
  const toggleSmallMode = () => {
    setIsSmallMode(window.scrollY > 5)
  }

  return (
    <>
      {/* ヘッダー */}
      <header className={`${styles.pageHeader} ${isSmallMode && styles.smallHeader}`}>
        <div className={`pageContainer ${isSmallMode && styles.smallContainer}`}>
          {/* LOGO リンク */}
          <Link href={constants.UI_URL_ROOT}>
            <div className={styles.logoImage}>
              <Image
                src="/logo.png"
                layout={'responsive'}
                width={286}
                height={78}
                alt={process.env.APP_NAME}
                priority
              />
            </div>
          </Link>
        </div>
      </header>
      {/* メインコンテンツの上部マージンを持たせるための要素 */}
      <div className={`transition-all ${isSmallMode ? 'h-16' : 'h-28'}`}></div>
    </>
  )
}

export default Header
