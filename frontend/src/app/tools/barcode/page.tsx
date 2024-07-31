'use client'

// import { AsyncZipOptions, zip } from 'fflate'
import React from 'react'

import BarcodeGenerator from '@/components/barcodeGenerator'
import Footer from '@/components/footer'
import Header from '@/components/header'
import styles from '@/styles/barcode.module.css'

/**
 * バーコード作成ツール
 * @constructor
 */
const BarCodeTool = () => {
  // バーコード・ジェネレーターの数
  const [generatorNum, setGeneratorNum] = React.useState<number>(3)
  // バーコード生成
  // const [testXml, setTestXml] = useState<string>()

  // const compress = async (
  //   files: File[],
  //   filename: string,
  //   compressOptions: AsyncZipOptions | undefined = undefined
  // ): Promise<File> => {
  //   try {
  //     const options = compressOptions || {}
  //     const fileContents: Record<string, Uint8Array> = {}
  //     const promises = files.map(async (f) => {
  //       const arrayBuffer = await f.arrayBuffer()
  //       fileContents[f.name] = new Uint8Array(arrayBuffer)
  //     })
  //     await Promise.all(promises)
  //     const zippedContent: Uint8Array = await new Promise((resolve, reject) => {
  //       zip(fileContents, options, (err, data) => {
  //         if (err) {
  //           reject(err)
  //         }
  //         resolve(data)
  //       })
  //     })
  //     return new File([zippedContent], filename)
  //   } catch (err) {
  //     return Promise.reject(new Error(`compress failed: ${err}`))
  //   }
  // }
  //
  // //
  // const handleDownload3 = async () => {
  //   if (testXml !== undefined) {
  //     const svgBlob = new Blob([testXml], { type: 'image/svg+xml' })
  //     // const svgUrl = URL.createObjectURL(svgBlob)
  //     const f = new File([svgBlob], 'test123.svg')
  //     const file = await compress([f], 'compressed.zip', { level: 9 })
  //     const a = document.createElement('a')
  //     a.href = URL.createObjectURL(file)
  //     a.download = 'a.gz'
  //
  //     document.body.appendChild(a)
  //     a.click()
  //   }
  // }

  return (
    <>
      <title>{`バーコード作成ツール | ${process.env.APP_NAME}`}</title>
      <meta name="description" content="バーコードを自うどう作成できます。" />
      <meta name="keywords" content="バーコード" />
      <Header />
      <main>
        <div className="pageContainer">
          <div className={styles.generatorList}>
            <div className={styles.generatorHead}>
              <div>No.</div>
              <div>コード値</div>
              <div>バーコード</div>
            </div>
            {Array(generatorNum)
              .fill(0)
              .map((v, idx) => (
                <div key={idx} className={styles.generatorBody}>
                  <div className={styles.generatorNo}>{idx + 1}</div>
                  <BarcodeGenerator />
                </div>
              ))}
            <div className={styles.generatorFoot}>
              <div
                onClick={() => {
                  setGeneratorNum((value) => ++value)
                }}
                className={styles.addGenerator}
              ></div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  )
}

export default BarCodeTool
