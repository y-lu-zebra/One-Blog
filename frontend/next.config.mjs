/** @type {import('next').NextConfig} */

import dotenv from 'dotenv'

// 環境設定ファイル変更
dotenv.config({ path: '../.env' })

const nextConfig = {
  reactStrictMode: false,
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
    // Google Analytics 測定 ID
    GA_TRACKING_ID: process.env.GA_TRACKING_ID,
  },
  // images: {
  //   // remotePatterns: [
  //   //   {
  //   //     protocol: 'http',
  //   //     hostname: 'localhost',
  //   //     port: '8000',
  //   //   },
  //   //   {
  //   //     protocol: 'https',
  //   //     hostname: 'localhost',
  //   //     port: '8000',
  //   //   },
  //   // ],
  // },
}

export default nextConfig
