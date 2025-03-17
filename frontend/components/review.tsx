'use client'; 

import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { IonIcon } from '@ionic/react';
import { personOutline } from 'ionicons/icons';

const reviewList = [
  {
    name: 'Alice Johnson',
    review:
      'lvSpace helped me find the perfect apartment right next to campus! The search filters made it easy to find what I wanted.',
    features: ['User-friendly interface', 'Great search filters', 'Fast response times'],
  },
  {
    name: 'Mark Stevens',
    review:
      'Listing my sublease on lvSpace was a breeze! The platform is intuitive and made connecting with potential renters so simple.',
    features: ['Easy listing process', 'Effective communication tools', 'Attractive layout'],
  },
  {
    name: 'Jessica Lee',
    review:
      'I love how lvSpace allows students to find affordable housing options! The community feedback helped me make the best choice.',
    features: ['Affordable options', 'Community-driven reviews', 'Helpful support'],
  },
  {
    name: 'David Smith',
    review:
      'The variety of listings on lvSpace is impressive! I was able to find a place that fit my budget and needs perfectly.',
    features: ['Diverse listings', 'Budget-friendly options', 'Detailed descriptions'],
  },
];

export default function Reviews() {
  return (
    <div className="flex flex-col md:flex-row gap-8 w-fit mx-auto lg:w-1/2 mt-16 mb-8">
      {/* First Column */}
      <div className="flex flex-col gap-6">
        {reviewList.slice(0, 2).map((reviewItem, index) => (
          <Card key={index} className="p-6 shadow-lg">
            <CardHeader>
              <div className="flex items-center gap-2">
                <IonIcon icon={personOutline} style={{ color: 'teal' }} />
                <CardTitle className="text-lg sm:text-xl md:text-2xl">{reviewItem.name}</CardTitle>
              </div>
              <div className="h-[1.5px] bg-gray-800 w-1/4 mr-auto my-2"></div>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2 text-xs sm:text-sm">
                {reviewItem.features.map((keyword, idx) => (
                  <Button
                    key={idx}
                    variant="outline"
                    className="p-2 rounded-md border-teal-500 bg-teal-500 text-white hover:bg-teal-600"
                  >
                    {keyword}
                  </Button>
                ))}
              </div>
              <CardDescription className="mt-4">{reviewItem.review}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Divider */}
      <div className="w-[1px] bg-gray-800 hidden md:flex"></div>

      {/* Second Column */}
      <div className="flex flex-col gap-6">
        {reviewList.slice(2, 4).map((reviewItem, index) => (
          <Card key={index} className="p-6 shadow-lg">
            <CardHeader>
              <div className="flex items-center gap-2">
                <IonIcon icon={personOutline} style={{ color: 'teal' }} />
                <CardTitle className="text-lg sm:text-xl md:text-2xl">{reviewItem.name}</CardTitle>
              </div>
              <div className="h-[1.5px] bg-gray-800 w-1/4 mr-auto my-2"></div>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2 text-xs sm:text-sm">
                {reviewItem.features.map((keyword, idx) => (
                  <Button
                    key={idx}
                    variant="outline"
                    className="p-2 rounded-md border-teal-500 bg-teal-500 text-white hover:bg-teal-600"
                  >
                    {keyword}
                  </Button>
                ))}
              </div>
              <CardDescription className="mt-4">{reviewItem.review}</CardDescription>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}