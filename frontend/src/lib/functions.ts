/**
 * a タグを利用したダウンロード機能．
 *
 * @param url ダウンロードしたいファイルの URL
 * @param fileName ローカルにダウンロードしたファイルの名前
 */
export const downloadWithATag = (url: string, fileName: string): void => {
  const a = document.createElement('a')
  a.href = url
  a.download = fileName

  a.click()
  a.remove()
  URL.revokeObjectURL(url)
}
