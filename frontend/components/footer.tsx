'use client';

import Link from 'next/link';
import Image from 'next/image';
import { IonIcon } from '@ionic/react';

import logoWhite from '@/public/logo-white.png';

export default function Footer() {
  return (
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
          <Link href="/faq">FAQ</Link>
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
  );
}