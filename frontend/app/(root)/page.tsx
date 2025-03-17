'use client';

import Link from 'next/link';
import Image from 'next/image';
import { useState } from 'react';
import { IonIcon } from '@ionic/react';
import { cubeOutline, searchOutline, } from 'ionicons/icons';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import Reviews from '@/components/review';
import Navbar from '@/components/navbar';
import Footer from '@/components/footer';

export default function HomePage() {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <>
      <Navbar />
      <div
        id="mobile-menu"
        className={`absolute right-0 ${isMobileMenuOpen ? 'flex' : 'hidden'
          } flex-col font-robo space-y-4 p-6 bg-secondary w-1/2 md:w-1/3 lg:w-1/4 justify-center rounded-xl text-primary`}
      >
        <Link href="/contact" className="text-sm font-semibold hover:text-accent">
          Contact
        </Link>
        <Link href="/faq" className="text-sm font-semibold hover:text-accent">
          FAQ
        </Link>
        <Link href="/items/new" className="md:hidden lg:hidden text-sm font-semibold hover:text-accent">
          Find Subleases
        </Link>
        <Link href="/items/browse" className="md:hidden lg:hidden text-sm font-semibold hover:text-accent">
          Search Apartments
        </Link>
        <Link href="/listings/create" className="md:hidden lg:hidden text-sm font-semibold hover:text-accent">
          List Your Property
        </Link>
      </div>
      <div className="px-6 py-6">
        {/* Search Section */}
        <section className="flex gap-10 flex-1 justify-center items-center mx-12 font-robo h-[85vh]">
          <div className="w-full lg:w-1/2">
            <h1 className="font-bold text-4xl md:text-6xl lg:text-6xl mb-6 text-center space-y-4">
              <span className="text-teal-500">Finding</span> Perfect Sublease or Apartment
              <span className="text-muted-foreground line-through dark:text-muted-foreground"> Is Hard.</span>
              <br />
              Just Got <span className="text-accent">Easier.</span>
            </h1>
            <form>
              <div className="flex rounded-xl mb-3 justify-between bg-secondary text-primary w-full p-3">
                <div className="flex-col w-2/3">
                  <p className="px-3 py-2 mb-2">Where to</p>
                  <Input
                    type="text"
                    placeholder="Search by University, or City"
                    className="bg-secondary outline-none text-primary placeholder:text-muted-foreground"
                  />
                </div>
                <Button asChild variant="default" className="rounded-xl p-6 m-2">
                  <Link href="/search">
                    <IonIcon icon={searchOutline} />
                  </Link>
                </Button>
              </div>
            </form>
          </div>
        </section>

        {/* About Section */}
        <section className="flex flex-col justify-center items-center font-robo p-6 mb-12">
          <div className="w-full lg:w-1/2">
            <Card>
              <CardHeader>
                <CardTitle className="text-2xl font-bold">
                  Find your perfect sublease or apartment with ease on lvSpace
                </CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-muted-foreground text-xs">
                  lvSpace offers a user-friendly platform for students to not only search for subleases or apartments within
                  their university or city area but also list your property. Our listings are verified to ensure accuracy and
                  security, giving you peace of mind during your housing search. With lvSpace, you can easily connect with
                  landlords and complete transactions securely, making your housing experience hassle-free.
                </p>
                <div className="mt-6">
                  <Image src="/home2.jpg" alt="About lvSpace" width={600} height={400} />
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Discover Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <Card>
              <CardHeader>
                <CardTitle className="text-3xl font-bold">
                  Find Your Perfect Sublease or Apartment{' '}
                  <span className="text-accent">With Ease.</span>.
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="mt-12 mb-12 grid grid-cols-3 gap-4">
                  <Card>
                    <CardHeader>
                      <IonIcon icon={cubeOutline} size="large" />
                      <CardTitle className="text-2xl font-semibold">Search for Subleases</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-xs mt-3 text-muted-foreground">
                        Browse through a wide selection of options and find the perfect place to call home.
                      </p>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <IonIcon icon={cubeOutline} size="large" />
                      <CardTitle className="text-2xl font-semibold">List Your Property</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-xs mt-3 text-muted-foreground">
                        Easily create a listing for your sublease and reach potential tenants in no time.
                      </p>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <IonIcon icon={cubeOutline} size="large" />
                      <CardTitle className="text-2xl font-semibold">Connect and Communicate</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-xs mt-3 text-muted-foreground">
                        Stay in touch with tenants and landlords through our convenient messaging system.
                      </p>
                    </CardContent>
                  </Card>
                </div>
                <div className="mb-6">
                  <Button asChild variant="outline">
                    <Link href="#">Learn More</Link>
                  </Button>
                  <Button asChild variant="default" className="ml-2">
                    <Link href="#">Sign Up &gt;</Link>
                  </Button>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Reviews Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2 mb-6">
            <p className="text-muted-foreground text-xs mb-6 text-center">Don't just take our word for it</p>
            <h1 className="text-4xl sm:text-5xl md:text-6xl mx-auto text-center font-semibold">
              See What <span className="text-accent">Others</span> Have to Say
            </h1>
          </div>
          <Reviews />
        </section>

        {/* Newsletter Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <Card>
              <CardHeader>
                <CardTitle className="text-3xl font-bold">Stay Updated with Our Newsletter.</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-muted-foreground text-xs mb-6">
                  Subscribe to our newsletter for the latest updates and new listings.
                </p>
                <form>
                  <div className="flex mb-3">
                    <Input
                      type="text"
                      placeholder="Enter your email"
                      className="w-2/3 md:w-1/3 lg:w-1/4"
                    />
                    <Button type="submit" className="ml-2">
                      Sign up
                    </Button>
                  </div>
                </form>
                <p className="text-muted-foreground text-xs mb-6">
                  By clicking Sign Up, you agree to our Privacy Policy.
                </p>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Support Section */}
        <section className="px-6 py-8 font-robo flex flex-col justify-center items-center">
          <div className="w-full lg:w-1/2">
            <Card>
              <CardHeader>
                <CardTitle className="text-3xl font-bold">Contact Us or Support Us</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-muted-foreground text-xs mb-6">
                  Have a question or want to support us? Feel free to reach out to us through the form below or via email. You
                  can also support us via PayPal. We appreciate your help and will get back to your requests and questions as
                  soon as possible.
                </p>
                <div className="flex h-[30vh] space-x-6 w-full justify-between">
                  <Image src="/home2.jpg" alt="Support Image 1" width={300} height={200} className="w-1/2 rounded-sm" />
                  <Image src="/home2.jpg" alt="Support Image 2" width={300} height={200} className="w-1/2 rounded-sm" />
                </div>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>
      <Footer />
    </>
  );
}