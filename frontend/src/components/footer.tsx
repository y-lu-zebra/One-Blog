'use client'

import React from 'react'

import styles from '@/styles/footer.module.css'

/**
 * フッター・コンポーネント
 *
 * @constructor
 */
const Footer = () => {
  return (
    <footer className={styles.pageFooter}>
      <div className="pageContainer">
        <div className={styles.copyright}>&copy; Yu Lu All Rights Reserved.</div>
      </div>
    </footer>
  )
}

export default Footer
