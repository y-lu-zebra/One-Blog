'use client'

import { usePathname, useSearchParams } from 'next/navigation'
import { useEffect } from 'react'
import ReactGA from 'react-ga4'

/**
 * Google Analytics (GA4) コンポーネント
 * @constructor
 */
const GoogleAnalytics = () => {
  const pathname = usePathname()
  const searchParams = useSearchParams()

  useEffect(() => {
    if (process.env.GA_TRACKING_ID) {
      const url: string = pathname + searchParams.toString()
      ReactGA.initialize(process.env.GA_TRACKING_ID)
      ReactGA.send({ hitType: 'pageview', page: url })
    }
  }, [pathname, searchParams])

  return <></>
}

export default GoogleAnalytics
