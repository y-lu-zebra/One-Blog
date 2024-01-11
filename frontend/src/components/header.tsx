import Image from 'next/legacy/image'
import React from 'react'

interface HeaderProps {
  menu: Category[]
}

export default function Header(props: HeaderProps) {
  return (
    <header className="md:container md:mx-auto px-4">
      <nav className="flex justify-between">
        <div className="logo-panel">
          <a className="logo-link" href="">
            <Image
              className="logo-img"
              src="/logo.svg"
              alt="One Blog"
              width={60}
              height={60}
              priority
            />
          </a>
        </div>
        <div className="nav-panel">
          <ul className="nav-list flex justify-normal">
            {props.menu.map((cat: Category, idx: number) => {
              return (
                <li key={idx} className="nav-item">
                  <button type="button">{cat.name}</button>
                </li>
              )
            })}
          </ul>
        </div>
      </nav>
    </header>
  )
}
