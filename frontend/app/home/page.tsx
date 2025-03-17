'use client'
import type { NextPage } from 'next';
import Image from 'next/image';
import { useState } from 'react';
import Head from 'next/head';
import { IonIcon } from '@ionic/react';
import { Button } from '@/components/ui/button';
import Link from 'next/link';

const Home: NextPage = () => {
  const [showApartments, setShowApartments] = useState(true);
  
  const togglePricing = (showApts: boolean) => {
    setShowApartments(showApts);
  };

  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Home | lvSpace</title>
        <link
          href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap"
          rel="stylesheet"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Padauk:wght@400;700&family=Roboto+Slab:wght@100..900&display=swap"
          rel="stylesheet"
        />
      </Head>

      <div className="bg-gray-100 min-h-screen font-[Padauk]">
        <nav className="flex justify-between bg-gray-800 space-x-6 py-4 text-xs text-white">
          <div className="flex items-center space-x-6 pl-8">
            <a href="/" className="w-[12vw]">
              <Image
                src="/logo-white.png"
                alt="lvSpace Logo"
                width={150}
                height={50}
                className="object-contain"
              />
            </a>
            <Button className="rounded-xl bg-gray-100 text-black p-2 flex items-center">
              <IonIcon name="location-outline"></IonIcon>
              <span className="ml-2">London</span>
            </Button>
            <form className="flex items-center bg-gray-600 rounded-xl py-2">
              <IonIcon name="search-outline" className="px-3"></IonIcon>
              <input
                type="text"
                placeholder="Search for subleases"
                className="bg-gray-600 outline-none text-white placeholder:text-gray-300"
              />
            </form>
          </div>
          <div className="pr-8">
            <Link
              href="/dashboard"
              className="py-2 flex items-center bg-teal-500 hover:bg-teal-700 px-4 rounded-xl"
            >
              Dashboard
            </Link>
          </div>
        </nav>

        <main className="mt-6 px-8 py-6 w-full font-[Roboto_Slab]">
          <h1 className="text-4xl font-bold mb-3">
            Student accommodation near London University
          </h1>
          <p className="text-gray-500 text-xs mb-6">
            Home\Student Accommodation\London
          </p>

          <div className="flex justify-between items-center mb-6">
            <div className="items-center p-2 flex text-teal-500 bg-white shadow-sm w-1/4">
              <IonIcon name="school-outline" className="mx-3"></IonIcon>
              <p className="font-bold">London University</p>
            </div>
            <div className="flex space-x-2">
              <button
                onClick={() => togglePricing(true)}
                className={`px-4 py-2 transition-colors ease-in duration-300 border ${
                  showApartments
                    ? 'bg-gray-800 text-white'
                    : 'bg-white text-black'
                }`}
              >
                Apartments
              </button>
              <button
                onClick={() => togglePricing(false)}
                className={`px-4 py-2 transition-colors ease-in duration-300 border ${
                  !showApartments
                    ? 'bg-gray-800 text-white'
                    : 'bg-white text-black'
                }`}
              >
                Subleases
              </button>
            </div>
          </div>

          <div className="w-full h-[10vh] bg-white shadow-sm">
            <div className="flex space-x-4 py-6 px-6">
              {/* Assuming 3 room types as an example */}
              {[1, 2, 3].map((_, index) => (
                <button
                  key={index}
                  className="p-3 bg-gray-800 text-white"
                >
                  Room Type
                </button>
              ))}
            </div>
          </div>

          <div className="flex justify-between items-center py-4">
            <span className="text-black">340 properties</span>
            <form id="sortForm" className="shadow-sm">
              <select
                name="sort"
                className="px-6 py-3 text-black"
                defaultValue="Recommended"
              >
                <option value="Recommended">Recommended</option>
                <option value="Distance to University">Distance to University</option>
                <option value="Price: Low to High">Price: Low to High</option>
                <option value="Price: High to Low">Price: High to Low</option>
              </select>
            </form>
          </div>

          <div className="py-6">
            <div className={`font-[Roboto_Slab] ${showApartments ? '' : 'hidden'}`}>
              {/* Replace with your apartment content component */}
              <p>Apartment Listings Here</p>
            </div>
            <div className={`font-[Roboto_Slab] ${!showApartments ? '' : 'hidden'}`}>
              {/* Replace with your sublease content component */}
              <p>Sublease Listings Here</p>
            </div>
          </div>
        </main>
      </div>
    </>
  );
};

export default Home;