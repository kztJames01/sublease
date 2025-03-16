import Navbar from '@/components/navbar';
import Footer from '@/components/footer';
import FAQ from '@/components/faq';

export default function FAQPage() {
  return (
    <>
      <Navbar />
      <div className="px-6 py-6">
        <FAQ />
      </div>
      <Footer />
    </>
  );
}