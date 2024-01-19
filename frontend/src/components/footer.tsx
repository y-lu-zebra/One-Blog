import Link from 'next/link'
import React from 'react'

import styles from '@/styles/footer.module.css'

/**
 * フッター・コンポーネント
 *
 * @constructor
 */
export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.footerContainer}>
        &copy;
        <Link className={styles.footerLink} href={''}>
          Yu Lu
        </Link>
        All Rights Reserved.
      </div>
    </footer>
  )
}
