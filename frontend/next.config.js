/** @type {import('next').NextConfig} */

// 環境設定ファイル変更
require('dotenv').config({ path: '../.env' })

const nextConfig = {
  // 環境設定
  env: {
    // アプリ名称
    APP_NAME: process.env.APP_NAME,
    // UI の URL
    APP_URL: process.env.APP_URL,
    // API の URL
    API_URL: process.env.API_URL,
    // ディスクリプション
    APP_DESCRIPTION: process.env.APP_DESCRIPTION,
    // キーワード
    APP_KEYWORDS: process.env.APP_KEYWORDS,
  },
}

module.exports = nextConfig
