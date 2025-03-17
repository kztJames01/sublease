'use client';

import Image from 'next/image';
import { Button } from '@/components/ui/button';
import { IonIcon } from '@ionic/react';
import { cashOutline } from 'ionicons/icons';

import homeImage from '@/public/core/home2.jpg';

export default function PropertyCard({
  title,
  description,
  price,
  amenities,
  billsIncluded,
  travelTimes,
  roomOptions,
}: PropertyCardProps) {
  return (
    <div className="col-span-1">
      <div className="flex items-center shadow-sm bg-white">
        {/* Property Image */}
        <Image
          src={homeImage}
          alt={title}
          className="w-[30vh]"
          width={200}
          height={150}
        />

        {/* Property Details */}
        <div className="flex-col items-center mx-4 py-2 space-y-2 w-[45vh]">
          <p className="text-2xl">{title}</p>
          <p className="text-xs text-gray-500">{description}</p>

          {/* Amenities */}
          <div className="flex space-x-4 items-center">
            {amenities.map((amenity, index) => (
              <IonIcon key={index} icon={amenity} style={{ color: 'teal' }} />
            ))}
            <span>|</span>
            <a href="#" className="text-teal-500 hover:text-teal-700">
              Map
            </a>
          </div>

          {/* Bills Included */}
          <div className="flex items-center space-x-2 text-xs">
            <IonIcon icon={cashOutline} style={{ color: 'teal' }} />
            <p className="text-black">
              Bills Included: <span>{billsIncluded.join(', ')}</span>
            </p>
          </div>

          {/* Travel Times */}
          <div className="flex items-center space-x-2 text-sm">
            {travelTimes.map((travel, index) => (
              <div key={index} className="flex items-center space-x-1">
                <IonIcon icon={travel.mode} style={{ color: 'teal' }} />
                <span>{travel.time}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Price and Room Options */}
        <div className="flex-col justify-between text-xs">
          <span>
            From <span className="text-teal-500 text-lg">${price}</span> / month
          </span>
          <div className="flex-col py-2 space-y-2 mt-6">
            {roomOptions.map((room, index) => (
              <p key={index} className="flex items-center justify-between text-gray-500">
                {room.type} <span className="text-teal-500">${room.price}</span>
              </p>
            ))}
            <Button className="bg-gray-800 text-white font-bold py-3 px-8 hover:bg-teal-500 ease-in duration-300">
              View Rooms
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}