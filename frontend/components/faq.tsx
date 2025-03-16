'use client'; 

import { useState } from 'react';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

const faqs = [
  {
    question: 'What is lvSpace?',
    answer:
      'lvSpace is a platform designed for students to find apartments and subleases near their desired cities or universities. It also allows apartment owners to list their properties.',
  },
  {
    question: 'How does the listing process work?',
    answer:
      'Apartment owners can easily list their apartments or subleases by creating an account on lvSpace, filling out property details, and uploading images. The process is quick and user-friendly.',
  },
  {
    question: 'Is there a fee to list my apartment on lvSpace?',
    answer:
      'Yes, we charge a fee based on the number of apartments you are listing. It’s 3% for listings with 50 to 100 units, 5% for 100 to 200 units, and 10% for 200 or more. Students listing subleases pay only 1%.',
  },
  {
    question: 'How can students communicate with apartment owners?',
    answer:
      'Our platform features a built-in chat function, allowing tenants and owners to communicate in real-time to discuss details about the property.',
  },
  {
    question: 'Are there any additional fees for students looking for subleases?',
    answer:
      'Students only pay a 1% fee on their sublease listing price. This makes it affordable for students to list their available spaces.',
  },
  {
    question: 'How do I find apartments near my university?',
    answer:
      'Simply enter your desired city or university into the search bar on our homepage, and you’ll be presented with a list of available apartments and subleases in that area.',
  },
  {
    question: 'What kind of properties can I list on lvSpace?',
    answer:
      'You can list any type of residential property, including apartments, houses, and subleases, as long as they meet our community guidelines.',
  },
  {
    question: 'Can I edit or delete my listing after it’s been posted?',
    answer:
      'Yes, you have the ability to edit or delete your listing at any time through your account dashboard.',
  },
  {
    question: 'What happens if I encounter an issue while using the platform?',
    answer:
      'If you face any issues, you can contact our customer support team via the help section on our website. We’re here to assist you!',
  },
  {
    question: 'How does lvSpace ensure a safe and trustworthy environment for users?',
    answer:
      'We prioritize user safety by verifying listings and offering a chat feature for direct communication. We encourage users to report any suspicious activity to help maintain a safe community.',
  },
];

export default function FAQ() {
  const [activeIndex, setActiveIndex] = useState<number | null>(null);

  const toggleFAQ = (index: number) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  return (
    <section className="flex flex-col justify-center items-center w-full lg:w-1/2 mx-auto font-robo p-6">
      <div className="flex flex-col gap-2 text-center">
        <p className="text-sm lg:text-lg text-gray-500 mb-6">For all your questions & inquiries</p>
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold">
          <span className="text-teal-500">Frequently</span> Asked Questions
        </h1>
        <Accordion type="single" collapsible className="w-full">
          {faqs.map((faq, index) => (
            <AccordionItem key={index} value={`item-${index}`}>
              <AccordionTrigger className="text-lg sm:text-xl md:text-2xl text-left">
                {faq.question}
              </AccordionTrigger>
              <AccordionContent className="text-gray-600">{faq.answer}</AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </section>
  );
}