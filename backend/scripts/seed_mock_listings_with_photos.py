import os
from pathlib import Path
from random import randint, sample

from django.contrib.auth.models import User
from django.core.files import File

from Listing.models import (
    ListingAmentiy,
    ListingImage,
    amenity,
    individualListingModel,
    propertyType,
)


AMENITIES = [
    'Laundry In Unit',
    'Gym Access',
    'Pool',
    'Parking',
    'Pet Friendly',
    'WiFi Included',
    'Air Conditioning',
    'Dishwasher',
    'Elevator',
    'Study Lounge',
]


LISTINGS = [
    ('Sunlit Townhouse Room', propertyType.TOWNHOUSE, '940 Maple St, Austin, TX', 940),
    ('Off-Campus Studio Near Shuttle', propertyType.OFF_CAMPUS_APARTMENT, '221 Oak Ave, Columbus, OH', 860),
    ('Dorm Spot in West Hall', propertyType.ON_CAMPUS_DORM, '1 University Dr, Madison, WI', 620),
    ('Modern 2BR Lease Takeover', propertyType.OFF_CAMPUS_APARTMENT, '76 River Rd, Raleigh, NC', 1120),
    ('Townhouse with Patio Access', propertyType.TOWNHOUSE, '510 Cedar Lane, Nashville, TN', 980),
    ('North Campus Dorm Transfer', propertyType.ON_CAMPUS_DORM, '88 Scholar Way, Seattle, WA', 690),
    ('Downtown Student Apartment', propertyType.OFF_CAMPUS_APARTMENT, '44 Spring St, Tempe, AZ', 1050),
    ('Quiet Townhouse Corner Unit', propertyType.TOWNHOUSE, '120 Juniper Ct, Boulder, CO', 1010),
    ('Shared Dorm Near Library', propertyType.ON_CAMPUS_DORM, '9 Commons Rd, Ann Arbor, MI', 580),
    ('Balcony Apartment Sublease', propertyType.OFF_CAMPUS_APARTMENT, '330 Harbor Blvd, Boston, MA', 1190),
]


def ensure_user():
    user = User.objects.order_by('id').first()
    if user:
        return user
    user = User.objects.create_user(
        username='hostdemo',
        email='hostdemo@example.com',
        password='DemoPass123!',
        first_name='Demo',
        last_name='Host',
    )
    return user


def ensure_property_types():
    for name in [propertyType.TOWNHOUSE, propertyType.OFF_CAMPUS_APARTMENT, propertyType.ON_CAMPUS_DORM]:
        propertyType.objects.get_or_create(name=name)


def ensure_amenities():
    for name in AMENITIES:
        amenity.objects.get_or_create(name=name)


def make_image(path: Path, seed: int):
    from PIL import Image, ImageDraw, ImageFont

    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new('RGB', (1400, 900), (20 + seed * 11 % 180, 33 + seed * 7 % 160, 61 + seed * 5 % 130))
    draw = ImageDraw.Draw(img)
    accent = (252, 163, 17)
    draw.rectangle((80, 80, 1320, 820), outline=accent, width=8)
    draw.rectangle((120, 120, 1280, 260), fill=(255, 255, 255, 40))
    text = f'LVSPACE DEMO LISTING {seed + 1}'
    try:
        font = ImageFont.truetype('arial.ttf', 60)
    except Exception:
        font = ImageFont.load_default()
    draw.text((150, 160), text, fill=accent, font=font)
    img.save(path, format='JPEG', quality=90)


def assign_listing_images(listing, index: int):
    base = Path('media') / 'seed_listings'
    cover = base / f'listing_{index + 1}_cover.jpg'
    gallery_a = base / f'listing_{index + 1}_gallery_a.jpg'
    gallery_b = base / f'listing_{index + 1}_gallery_b.jpg'

    make_image(cover, index)
    make_image(gallery_a, index + 20)
    make_image(gallery_b, index + 40)

    with cover.open('rb') as fp:
        listing.images.save(cover.name, File(fp), save=True)

    listing.gallery_images.all().delete()
    for order, path in enumerate([gallery_a, gallery_b]):
        with path.open('rb') as fp:
            image = ListingImage(listing=listing, order=order)
            image.image.save(path.name, File(fp), save=True)


def run():
    ensure_property_types()
    ensure_amenities()
    host = ensure_user()

    all_amenities = list(amenity.objects.all())

    for index, (title, pt_name, address, price) in enumerate(LISTINGS):
        pt = propertyType.objects.get(name=pt_name)
        listing, _ = individualListingModel.objects.get_or_create(
            title=title,
            defaults={
                'property_type': pt,
                'created_by': host,
                'bedrooms': randint(1, 4),
                'bedroom_privacy': 'private' if index % 2 == 0 else 'shared',
                'bathrooms': randint(1, 3),
                'bathroom_privacy': 'private' if index % 3 == 0 else 'shared',
                'address': address,
                'description': f'{title} with strong natural light, updated finishes, and flexible move-in terms.',
                'price': price,
                'website_url': f'https://demo.example.com/listings/{index + 1}',
                'offer_status': ['accepting', 'pending', 'closed'][index % 3],
                'is_sold': False,
            },
        )

        listing.property_type = pt
        listing.created_by = host
        listing.address = address
        listing.price = price
        listing.website_url = f'https://demo.example.com/listings/{index + 1}'
        listing.description = f'{title} with strong natural light, updated finishes, and flexible move-in terms.'
        listing.offer_status = ['accepting', 'pending', 'closed'][index % 3]
        listing.save()

        listing.amenities.all().delete()
        for am in sample(all_amenities, k=4):
            ListingAmentiy.objects.get_or_create(listing=listing, amenity=am)

        assign_listing_images(listing, index)

    print(f'Seeded listings: {individualListingModel.objects.count()}')
    print(f'Seeded amenities: {amenity.objects.count()}')


run()
