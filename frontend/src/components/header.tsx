import Image from 'next/legacy/image'
// import Link from 'next/link'
import React from 'react'

import { constants } from '@/lib/constants'
import styles from '@/styles/header.module.css'
// import { Category } from '@/types/category'

// interface HeaderProps {
//   navItems: Category[]
// }

/**
 * ヘッダー・コンポーネント
 *
 * @constructor
 */
export default function Header() {
  return (
    <header className={styles.header}>
      <nav className={styles.headerContainer}>
        <menu className={styles.menuPanel}>
          {/*  <ul className="columns-2">*/}
          {/*    <li className="py-5">*/}
          {/*      <Link href={''}>ABC</Link>*/}
          {/*    </li>*/}
          {/*    <li className="py-5">*/}
          {/*      <Link href={''}>DEF</Link>*/}
          {/*    </li>*/}
          {/*  </ul>*/}
        </menu>
        <div className={styles.logoPanel}>
          <a className="logoLink" href={constants.UI_URL_ROOT}>
            <Image
              className="logoImg"
              src="/logo.svg"
              alt={process.env.APP_NAME}
              width={60}
              height={60}
              priority
            />
          </a>
        </div>
        <menu className={styles.menuPanel}>
          {/*  <ul className={`columns-${props.navItems.length}`}>*/}
          {/*    {props.navItems.map((cat: Category, idx: number) => {*/}
          {/*      return (*/}
          {/*        <li key={idx} className="py-5">*/}
          {/*          <button type="button">{cat.name}</button>*/}
          {/*        </li>*/}
          {/*      )*/}
          {/*    })}*/}
          {/*  </ul>*/}
        </menu>
      </nav>
    </header>
  )
}
