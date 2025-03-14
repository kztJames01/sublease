'use client';
import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';
import { IonIcon } from '@ionic/react';

// Static assets
import logo from '@/public/logo.png';
import logoWhite from '@/public/logo-white.png';


export default function Layout({ children }: { children: React.ReactNode }) {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <script
          type="module"
          src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"
        ></script>
        <script
          noModule
          src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"
        ></script>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="/app/globals.css" rel="stylesheet" />
        <title>lvSpace</title>
        <style>
          {`
            @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&display=swap');
          `}
        </style>
      </head>
      <body>
        <nav className="flex py-6 px-6 justify-around items-center font-robo">
          <Link href="/">
            <Image src={logo} alt="lvSpace Logo" className="w-[20vw] md:w-[12vw] lg:w-[12vw]" />
          </Link>
          <div className="hidden md:flex lg:flex space-x-6 items-center px-6">
            <Link href="/items/new" className="text-sm font-semibold hover:text-teal-500">
              Find Subleases
            </Link>
            <Link href="/items/browse" className="text-sm font-semibold hover:text-teal-500">
              Search Apartments
            </Link>
            <Link href="/listings/create" className="text-sm font-semibold hover:text-teal-500">
              List Your Property
            </Link>
          </div>
          <div className="flex space-x-3 items-center md:hidden lg:hidden px-6">
            <button className="menu-toggle" onClick={toggleMobileMenu}>
              <IonIcon name="menu-outline" />
            </button>
          </div>
          {/* Replace with actual authentication logic */}
          {false ? (
            <div className="flex justify-center space-x-3">
              <button className="menu-toggle hidden md:block lg:block" onClick={toggleMobileMenu}>
                <IonIcon name="menu-outline" className="text-2xl text-center" />
              </button>
              <Link
                href="/dashboard"
                className="px-6 py-3 text-sm font-semibold bg-gray-700 rounded-xl text-white hover:bg-teal-500"
              >
                Dashboard
              </Link>
            </div>
          ) : (
            <>
              <button className="menu-toggle hidden md:block lg:block" onClick={toggleMobileMenu}>
                <IonIcon name="menu-outline" className="text-2xl text-center" />
              </button>
              <Link
                href="/signup"
                className="px-6 py-3 text-sm font-semibold rounded-xl bg-teal-500 text-white hover:bg-teal-700"
              >
                Sign Up
              </Link>
            </>
          )}
        </nav>

        {/* Mobile Menu */}
        <div
          id="mobile-menu"
          className={`absolute right-0 ${
            isMobileMenuOpen ? 'flex' : 'hidden'
          } flex-col font-robo space-y-4 p-6 bg-gray-700 w-1/2 md:w-1/3 lg:w-1/4 justify-center rounded-xl text-white`}
        >
          <Link href="/contact" className="text-sm font-semibold hover:text-teal-500">
            Contact
          </Link>
          <Link href="/faq" className="text-sm font-semibold hover:text-teal-500">
            FAQ
          </Link>
          <Link href="/items/new" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
            Find Subleases
          </Link>
          <Link href="/items/browse" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
            Search Apartments
          </Link>
          <Link href="/listings/create" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
            List Your Property
          </Link>
        </div>

        <div className="px-6 py-6">{children}</div>

        <footer className="py-6 px-8 font-robo flex-col justify-between bg-gray-800 items-center">
          <div className="flex flex-col text-white w-full justify-center items-center">
            <Image src={logoWhite} alt="lvSpace Logo" className="my-6 w-[20vw]" />
            <p className="text-xs mb-6">
              Phone : <span className="text-teal-500">+1 (555) 555-5555</span>
            </p>
            <p className="text-xs mb-6">
              Email : <span className="text-teal-500">QJp0B@example.com</span>
            </p>
            <div className="flex space-x-3 mb-6 text-xs">
              <Link href="/about">About</Link>
              <Link href="/faq">FAQ</Link>
              <Link href="/contact">Contact Us</Link>
              <Link href="/terms">Terms of Use</Link>
              <Link href="/privacy">Privacy Policy</Link>
            </div>
            <div className="flex space-x-3 mb-6">
              <IonIcon name="logo-facebook" className="text-xs text-teal-500 hover:text-teal-700" />
              <IonIcon name="logo-twitter" className="text-xs text-teal-500 hover:text-teal-700" />
              <IonIcon name="logo-instagram" className="text-xs text-teal-500 hover:text-teal-700" />
            </div>
          </div>
          <hr className="bg-white h-0.25 mt-6" />
          <div className="flex justify-between mt-6 mb-6 text-xs text-white">
            <p>© 2021 lvSpace. All rights reserved</p>
            <p>Powered by lvSpace</p>
          </div>
        </footer>
      </body>
    </html>
  );
}