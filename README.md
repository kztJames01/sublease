# sublease

## Supabase + Django setup

1) Create a Supabase project and get the database connection string.
2) Copy .env.example to .env and set either:
	- DATABASE_URL (recommended)
	- or DATABASE_* fields + DATABASE_SSLMODE=require
3) Install Python dependencies:
	- requirements.txt
4) Run migrations and start the app:
	- python manage.py migrate
	- python manage.py runserver