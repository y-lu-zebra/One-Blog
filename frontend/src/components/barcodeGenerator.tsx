import React, { useEffect, useId, useRef, useState } from 'react'
import { ReactBarcode, Renderer } from 'react-jsbarcode'

import { downloadWithATag } from '@/lib/functions'
import styles from '@/styles/barCodeGenerator.module.css'

/**
 * バーコード・ジェネレーター
 *
 * @constructor
 */
const BarcodeGenerator = () => {
  // ダウンロード画像拡張子の配列
  const EXT_IMG: string[] = ['SVG', 'GIF', 'JPG', 'PNG']
  // コンポーネント ID
  const uuid = useId()
  // バーコード SVG の親要素
  const barcodeElm = useRef<HTMLDivElement>(null)
  // コード
  const [code, setCode] = useState<string>('')
  const [imgExt, setImgExt] = useState<string>(EXT_IMG[0])

  useEffect(() => {}, [])

  /**
   * バーコードを生成する．
   *
   * @param e
   */
  const generateBarcode = (e: React.ChangeEvent<HTMLTextAreaElement>): void => {
    console.log(e.target.value)
    setCode(e.target.value)
  }

  const download = (): void => {
    const svgElm = barcodeElm.current?.children[0]
    if (svgElm instanceof Node) {
      const ext = imgExt.toLowerCase()
      const canvas = document.createElement('canvas')
      canvas.width = svgElm.clientWidth
      canvas.height = svgElm.clientHeight
      const blog = new Blob([new XMLSerializer().serializeToString(svgElm)], {
        type: 'image/svg+xml;charset=utf-8',
      })

      if (imgExt === EXT_IMG[0]) {
        const fileUrl: string = URL.createObjectURL(blog)
        downloadWithATag(fileUrl, `${code}.${ext}`)
      } else {
        const ctx = canvas.getContext('2d')
        const img = new Image()
        if (ctx) {
          img.onload = () => {
            ctx.drawImage(img, 0, 0)
            const fileUrl = canvas.toDataURL(`image/${ext}`)
            downloadWithATag(fileUrl, `${code}.${ext}`)
          }
          img.src = URL.createObjectURL(blog)
        }
      }
    }
  }

  return (
    <>
      <div className={styles.barcodeForm}>
        <div className={styles.barcodeInput}>
          <textarea onChange={generateBarcode}></textarea>
        </div>
        <div className={styles.barcodeOptions}>
          {EXT_IMG.map((ext: string, idx: number) => (
            <span key={idx} className={styles.radioSet}>
              <input
                type="radio"
                name={`${uuid}-ext`}
                value={ext}
                defaultChecked={ext === EXT_IMG[0]}
                onChange={(e) => {
                  setImgExt(e.target.value)
                }}
                id={ext}
              />
              <label htmlFor={ext}>{ext}</label>
            </span>
          ))}
          <span className={styles.buttonSet}>
            <input type="button" onClick={download} className={styles.downloadButton} />
          </span>
        </div>
      </div>
      <div ref={barcodeElm} className={styles.barcodeImg}>
        {code && (
          <ReactBarcode
            value={code}
            options={{ format: 'code128', width: 2 }}
            renderer={Renderer.SVG}
            className="max-w-[100%] h-[100%]"
          />
        )}
      </div>
    </>
  )
}

export default BarcodeGenerator
