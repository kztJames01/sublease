'use client';

import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';
import { IonIcon } from '@ionic/react';
import { Button } from '@/components/ui/button';
import { menuOutline } from 'ionicons/icons';
import logo from '@/public/logo.png';

export default function Navbar() {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <>
      <nav className="flex py-6 px-6 justify-around items-center font-robo">
        <Link href="/">
          <Image src={logo} alt="lvSpace Logo" className="w-[20vw] md:w-[12vw] lg:w-[12vw]" />
        </Link>
        <div className="hidden md:flex lg:flex space-x-6 items-center px-6">
          <Button asChild variant="link" className="text-sm font-semibold hover:text-teal-500">
            <Link href="/items/new">Find Subleases</Link>
          </Button>
          <Button asChild variant="link" className="text-sm font-semibold hover:text-teal-500">
            <Link href="/items/browse">Search Apartments</Link>
          </Button>
          <Button asChild variant="link" className="text-sm font-semibold hover:text-teal-500">
            <Link href="/listings/create">List Your Property</Link>
          </Button>
        </div>
        <div className="flex space-x-3 items-center md:hidden lg:hidden px-6">
          <Button variant="ghost" onClick={toggleMobileMenu} className="text-2xl text-center">
            <IonIcon icon={menuOutline} />
          </Button>
        </div>
        {false ? (
          <div className="flex justify-center space-x-3">
            <Button variant="ghost" onClick={toggleMobileMenu} className="hidden md:block lg:block text-2xl text-center">
              <IonIcon icon={menuOutline}  />
            </Button>
            <Button asChild variant="default">
              <Link href="/dashboard">Dashboard</Link>
            </Button>
          </div>
        ) : (
          <>
            <Button variant="ghost" onClick={toggleMobileMenu} className="hidden md:block lg:block text-2xl text-center">
              <IonIcon icon={menuOutline}  />
            </Button>
            <Button asChild variant="default">
              <Link href="/auth/sign-up">Sign Up</Link>
            </Button>
          </>
        )}
      </nav>
      <div
        id="mobile-menu"
        className={`absolute right-0 ${isMobileMenuOpen ? 'flex' : 'hidden'
          } flex-col font-robo space-y-4 p-6 bg-gray-700 w-1/2 md:w-1/3 lg:w-1/4 justify-center rounded-xl text-white`}
      >
        <Button asChild variant="link" className="text-sm font-semibold hover:text-teal-500">
          <Link href="/faq">FAQ</Link>
        </Button>
        <Button asChild variant="link" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
          <Link href="/items/new">Find Subleases</Link>
        </Button>
        <Button asChild variant="link" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
          <Link href="/items/browse">Search Apartments</Link>
        </Button>
        <Button asChild variant="link" className="md:hidden lg:hidden text-sm font-semibold hover:text-teal-500">
          <Link href="/listings/create">List Your Property</Link>
        </Button>
      </div>
    </>
  );
}