from django.contrib.auth.models import User

from Listing.models import apartmentListingModel, individualListingModel, propertyType
from communication.models import Conversation, ConversationMessage
from item.models import Category, Item


PROPERTY_TYPES = [
    propertyType.TOWNHOUSE,
    propertyType.OFF_CAMPUS_APARTMENT,
    propertyType.ON_CAMPUS_DORM,
]


INDIVIDUAL_LISTINGS = [
    {
        'title': 'Sunny 2BR Near Campus Loop',
        'property_type': propertyType.OFF_CAMPUS_APARTMENT,
        'bedrooms': 2,
        'bedroom_privacy': 'private',
        'bathrooms': 1,
        'bathroom_privacy': 'shared',
        'address': '1847 Maple Ave, College Station, TX',
        'description': 'Bright sublease with balcony, furnished living room, and a short walk to campus shuttle access.',
        'price': 875,
        'website_url': 'https://demo.example.com/sublease/sunny-2br',
    },
    {
        'title': 'Townhouse Room with Garage Parking',
        'property_type': propertyType.TOWNHOUSE,
        'bedrooms': 3,
        'bedroom_privacy': 'private',
        'bathrooms': 2,
        'bathroom_privacy': 'shared',
        'address': '52 Crestline Dr, Austin, TX',
        'description': 'Quiet townhouse setup with in-unit laundry, garage parking, and a roomy kitchen.',
        'price': 790,
        'website_url': 'https://demo.example.com/sublease/townhouse-room',
    },
    {
        'title': 'Dorm Transfer in Honors Hall',
        'property_type': propertyType.ON_CAMPUS_DORM,
        'bedrooms': 1,
        'bedroom_privacy': 'shared',
        'bathrooms': 1,
        'bathroom_privacy': 'shared',
        'address': '1 University Plaza, Madison, WI',
        'description': 'On-campus dorm transfer with utilities included and meal plan access nearby.',
        'price': 620,
        'website_url': 'https://demo.example.com/sublease/honors-hall',
    },
    {
        'title': 'West End Loft for Summer Semester',
        'property_type': propertyType.OFF_CAMPUS_APARTMENT,
        'bedrooms': 1,
        'bedroom_privacy': 'private',
        'bathrooms': 1,
        'bathroom_privacy': 'private',
        'address': '900 West End Blvd, Nashville, TN',
        'description': 'Modern loft with floor-to-ceiling windows and a co-working lounge downstairs.',
        'price': 1195,
        'website_url': 'https://demo.example.com/sublease/west-end-loft',
    },
    {
        'title': 'Budget Room by Engineering Quad',
        'property_type': propertyType.OFF_CAMPUS_APARTMENT,
        'bedrooms': 4,
        'bedroom_privacy': 'private',
        'bathrooms': 2,
        'bathroom_privacy': 'shared',
        'address': '77 Cedar St, Ann Arbor, MI',
        'description': 'Affordable setup with fast Wi-Fi, bike storage, and roommates already vetted.',
        'price': 640,
        'website_url': 'https://demo.example.com/sublease/engineering-quad',
    },
    {
        'title': 'Corner Townhouse with Patio',
        'property_type': propertyType.TOWNHOUSE,
        'bedrooms': 2,
        'bedroom_privacy': 'private',
        'bathrooms': 2,
        'bathroom_privacy': 'private',
        'address': '412 Juniper Row, Raleigh, NC',
        'description': 'Two-floor townhouse with private patio, dishwasher, and guest parking.',
        'price': 980,
        'website_url': 'https://demo.example.com/sublease/corner-townhouse',
    },
    {
        'title': 'Dorm Space at North Commons',
        'property_type': propertyType.ON_CAMPUS_DORM,
        'bedrooms': 1,
        'bedroom_privacy': 'shared',
        'bathrooms': 1,
        'bathroom_privacy': 'shared',
        'address': '12 North Commons, Champaign, IL',
        'description': 'Clean dorm room transfer close to dining hall, library, and gym.',
        'price': 585,
        'website_url': 'https://demo.example.com/sublease/north-commons',
    },
    {
        'title': 'Riverside Apartment with Study Nook',
        'property_type': propertyType.OFF_CAMPUS_APARTMENT,
        'bedrooms': 2,
        'bedroom_privacy': 'shared',
        'bathrooms': 2,
        'bathroom_privacy': 'private',
        'address': '230 River Walk, Tampa, FL',
        'description': 'Riverfront building with pool, secure access, and a built-in study nook.',
        'price': 910,
        'website_url': 'https://demo.example.com/sublease/riverside-nook',
    },
    {
        'title': 'Graduate Housing Dorm Transfer',
        'property_type': propertyType.ON_CAMPUS_DORM,
        'bedrooms': 1,
        'bedroom_privacy': 'private',
        'bathrooms': 1,
        'bathroom_privacy': 'shared',
        'address': '455 Scholar Way, Berkeley, CA',
        'description': 'Grad housing room with quiet-floor policy and campus transit right outside.',
        'price': 730,
        'website_url': 'https://demo.example.com/sublease/grad-housing',
    },
    {
        'title': 'Three-Bed Townhouse Near Stadium',
        'property_type': propertyType.TOWNHOUSE,
        'bedrooms': 3,
        'bedroom_privacy': 'private',
        'bathrooms': 3,
        'bathroom_privacy': 'private',
        'address': '88 Victory Ln, Columbus, OH',
        'description': 'Spacious townhouse with hardwood floors, fenced yard, and quick stadium access.',
        'price': 1050,
        'website_url': 'https://demo.example.com/sublease/stadium-townhouse',
    },
]


APARTMENT_COMPLEXES = [
    ('The Beacon Residences', 'Seattle', 'WA'),
    ('Atlas Student Living', 'Tempe', 'AZ'),
    ('Juniper Commons', 'Boulder', 'CO'),
    ('The Reserve at Midtown', 'Atlanta', 'GA'),
    ('Northline Flats', 'Minneapolis', 'MN'),
    ('Harbor House Collective', 'Boston', 'MA'),
    ('Cedar Yard Apartments', 'Lexington', 'KY'),
    ('Summit Point Living', 'Knoxville', 'TN'),
    ('The Harlow on 9th', 'Lincoln', 'NE'),
    ('Parkside Union', 'Eugene', 'OR'),
]


MESSAGES = [
    'Hi, is the unit still available?',
    'Yes, it is. I can share a walkthrough video and move-in timeline.',
    'That works. What utilities are included each month?',
    'Water and internet are included, electricity is separate.',
]


def get_or_create_user(username, email, first_name, last_name):
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        },
    )
    if created:
        user.set_password('DemoPass123!')
        user.save()
    return user


def run():
    owner = User.objects.order_by('id').first() or get_or_create_user(
        'demoowner', 'owner@example.com', 'Demo', 'Owner'
    )

    guest = get_or_create_user('demoguest', 'guest@example.com', 'Demo', 'Guest')
    helper = get_or_create_user('demohost', 'host@example.com', 'Demo', 'Host')

    property_type_map = {
        name: propertyType.objects.get_or_create(name=name)[0]
        for name in PROPERTY_TYPES
    }

    category, _ = Category.objects.get_or_create(name='Housing Inquiry')

    for payload in INDIVIDUAL_LISTINGS:
        listing, created = individualListingModel.objects.get_or_create(
            title=payload['title'],
            defaults={
                **payload,
                'property_type': property_type_map[payload['property_type']],
                'created_by': owner,
            },
        )
        if not created:
            for key, value in payload.items():
                if key == 'property_type':
                    setattr(listing, key, property_type_map[value])
                else:
                    setattr(listing, key, value)
            listing.created_by = owner
            listing.save()

    for index, (company, city, state) in enumerate(APARTMENT_COMPLEXES, start=1):
        apartmentListingModel.objects.get_or_create(
            company=company,
            defaults={
                'first_name': f'Leasing{index}',
                'last_name': 'Manager',
                'email': f'leasing{index}@demoexample.com',
                'phone': f'555-100-{index:04d}',
                'city': city,
                'zipCode': f'{70000 + index}',
                'state': state,
                'country': 'USA',
                'website_url': f'https://demo.example.com/apartments/{company.lower().replace(" ", "-")}',
                'created_by': owner,
            },
        )

    items = []
    for listing in individualListingModel.objects.order_by('id')[:3]:
        item, _ = Item.objects.get_or_create(
            name=f'{listing.title} Info Packet',
            defaults={
                'category': category,
                'description': f'Info packet for {listing.title}',
                'price': 0,
                'created_by': owner,
            },
        )
        items.append(item)

    pairs = [
        (items[0], owner, guest),
        (items[1], owner, helper),
        (items[2], guest, owner),
    ]

    for item, first_user, second_user in pairs:
        convo, _ = Conversation.objects.get_or_create(item=item)
        convo.members.add(first_user, second_user)
        if convo.messages.count() == 0:
            for idx, content in enumerate(MESSAGES):
                author = first_user if idx % 2 == 0 else second_user
                ConversationMessage.objects.create(
                    conversation=convo,
                    content=content,
                    created_by=author,
                )

    print('Seed complete:')
    print(f'Individual listings: {individualListingModel.objects.count()}')
    print(f'Apartment complexes: {apartmentListingModel.objects.count()}')
    print(f'Conversations: {Conversation.objects.count()}')


run()
