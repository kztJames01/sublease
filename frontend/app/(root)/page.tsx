'use client';
import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';
import { IonIcon } from '@ionic/react';
import Script from 'next/script';

import homeImage from '@/public/home2.jpg';
import logo from '@/public/logo.png';
import logoWhite from '@/public/logo-white.png';
import Reviews from '@/components/review';

export default function Layout({ children }: { children: React.ReactNode }) {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <>
      <Script
        src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"
        strategy="beforeInteractive"
      />
      <Script
        src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"
        strategy="beforeInteractive"
        noModule
      />
      <Script
        src="https://cdn.tailwindcss.com"
        strategy="beforeInteractive"
      />
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
      <div
        id="mobile-menu"
        className={`absolute right-0 ${isMobileMenuOpen ? 'flex' : 'hidden'
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
      <div className="px-6 py-6">
        <section className="flex gap-10 flex-1 justify-center items-center mx-12 font-robo h-[85vh]">
          <div className="w-full lg:w-1/2">
            <h1 className="font-bold text-4xl md:text-6xl lg:text-6xl mb-6 text-center space-y-4">
              <span className="text-teal-500">Finding</span> Perfect Sublease or Apartment
              <span className="text-gray-500 line-through">Is Hard.</span>
              <br />
              Just Got <span className="text-teal-500">Easier.</span>
            </h1>
            <form>
              <div className="flex rounded-xl mb-3 justify-between bg-gray-800 text-white w-full p-3">
                <div className="flex-col w-2/3">
                  <p className="px-3 py-2 mb-2">Where to</p>
                  <input
                    type="text"
                    className="px-3 py-2 text-xs bg-gray-800 w-full outline-none"
                    placeholder="Search by University, or City"
                  />
                </div>
                <Link
                  href="/search"
                  className="rounded-xl bg-teal-500 text-white p-6 m-2"
                >
                  <IonIcon name="search-outline" />
                </Link>
              </div>
            </form>
          </div>
        </section>

        {/* About Section */}
        <section className="flex flex-col justify-center items-center font-robo p-6 mb-12">
          <div className="w-full lg:w-1/2">
            <div className="flex mb-6">
              <h1 className="text-2xl w-1/2 font-bold">
                Find your perfect sublease or apartment with ease on lvSpace
              </h1>
              <p className="text-gray-500 text-xs w-1/2">
                lvSpace offers a user-friendly platform for students to not only search for subleases or apartments within
                their university or city area but also list your property. Our listings are verified to ensure accuracy and
                security, giving you peace of mind during your housing search. With lvSpace, you can easily connect with
                landlords and complete transactions securely, making your housing experience hassle-free.
              </p>
            </div>
            <div className="mt-6">
              <Image src={homeImage} alt="About lvSpace" />
            </div>
          </div>
        </section>

        {/* Discover Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <div className="flex">
              <div className="mr-3">
                <h4 className="text-xs">Discover</h4>
                <h1 className="text-3xl font-bold">
                  Find Your Perfect Sublease or Apartment{' '}
                  <span className="text-teal-500">With Ease.</span>.
                </h1>
              </div>
              <p className="text-gray-500 text-xs ml-3">
                With lvSpace, you can easily connect with landlords or talk with potential tenants, making your housing
                experience hassle-free.
              </p>
            </div>

            <div className="mt-12 mb-12 grid grid-cols-3 gap-4">
              <div>
                <IonIcon name="cube-outline" size="large" />
                <h2 className="text-2xl font-semibold">Search for Subleases</h2>
                <p className="text-xs mt-3 text-gray-500">
                  Browse through a wide selection of options and find the perfect place to call home.
                </p>
              </div>
              <div>
                <IonIcon name="cube-outline" size="large" />
                <h2 className="text-2xl font-semibold">List Your Property</h2>
                <p className="text-xs mt-3 text-gray-500">
                  Easily create a listing for your sublease and reach potential tenants in no time.
                </p>
              </div>
              <div>
                <IonIcon name="cube-outline" size="large" />
                <h2 className="text-2xl font-semibold">Connect and Communicate</h2>
                <p className="text-xs mt-3 text-gray-500">
                  Stay in touch with tenants and landlords through our convenient messaging system.
                </p>
              </div>
            </div>
            <div className="mb-6">
              <button>
                <Link href="#" className="text-xs px-4 py-3 border border-black text-black">
                  Learn More
                </Link>
              </button>
              <button>
                <Link href="#" className="text-xs px-4 py-3 text-black">
                  Sign Up &gt;
                </Link>
              </button>
            </div>
          </div>
        </section>

        {/* Reviews Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2 mb-6">
            <p className="text-gray-500 text-xs mb-6 text-center">Don't just take our word for it</p>
            <h1 className="text-4xl sm:text-5xl md:text-6xl mx-auto text-center font-semibold">
              See What <span className="text-teal-500">Others</span> Have to Say
            </h1>
          </div>
          <Reviews /> 
        </section>

        {/* Newsletter Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <h1 className="text-3xl font-bold mb-4">Stay Updated with Our Newsletter.</h1>
            <p className="text-gray-500 text-xs w-1/2 mb-6">
              Subscribe to our newsletter for the latest updates and new listings.
            </p>
            <form>
              <div className="flex mb-3">
                <input
                  type="text"
                  className="border px-3 py-2 w-2/3 md:w-1/3 lg:w-1/4 text-xs"
                  placeholder="Enter your email"
                />
                <button className="text-xs bg-teal-500 text-white px-3 py-2 mx-3">Sign up</button>
              </div>
            </form>
            <p className="text-gray-500 text-xs w-1/2 mb-6">
              By clicking Sign Up, you agree to our Privacy Policy.
            </p>
          </div>
        </section>

        {/* Support Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <h1 className="text-3xl font-bold mb-6">Contact Us or Support Us</h1>
            <p className="text-gray-500 text-xs mb-6">
              Have a question or want to support us? Feel free to reach out to us through the form below or via email. You
              can also support us via PayPal. We appreciate your help and will get back to your requests and questions as
              soon as possible.
            </p>
            <div className="flex h-[30vh] space-x-6 w-full justify-between">
              <Image src={homeImage} alt="Support Image 1" className="w-1/2 rounded-sm" />
              <Image src={homeImage} alt="Support Image 2" className="w-1/2 rounded-sm" />
            </div>
          </div>
        </section>
      </div>
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
    </>
  );
}