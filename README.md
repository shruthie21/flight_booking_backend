# flight_booking_backend

## Installation

1. Install the required dependencies using the following command:
   - activate virtualenv
   - pip install -r requirements.txt
3. Run migrations to create the database schema:
   - python manage.py migrate
4. Create migrations based on changes in models:
   - python manage.py makemigrations
   - python manage.py migrate

## Running the Application

Start the Django server by running:
 - python manage.py runserver 8000

## Features Implemented

1. **Flight List**: 
- Endpoint: `/api/flights/`
- Method: GET
- Returns a list of all flights in the database.

2. **Flight Search**: 
- Endpoint: `/api/flights/search/`
- Method: POST
- Accepts source city, destination city, travel date, and return date as input.
- Filters flights based on the provided search criteria and returns matching flights.

3. **Populate Fields**:
- As soon as the application loads, populate_field function runs automatically to populate flight records 
in the database.
- Json file is added Path: flight_booking_backend/flights/flights_records_json/flights.json
  
# Unit Tests

Unit tests have been written and implemented for the given endpoints. 