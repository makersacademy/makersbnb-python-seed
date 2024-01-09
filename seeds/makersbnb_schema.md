# MakersBnB Database Schema

## Users
- Columns for:
    - ID
    - Username
    - Email
    - Password (hashed)

## Spaces
- Columns for:
    - ID
    - Name
    - Description
    - Price (per night)
    - Host_ID (i.e. a user ID)

## Dates (Space Availability)
- Columns for:
    - ID
    - Date
    - Space ID

## Bookings
- Columns for:
    - ID
    - Guest_ID (i.e. a user ID)
    - Space_ID
    - Date
    - Confirmed (a boolean)

## Relations
One USER can list many SPACES, so spaces contains a host_id column
One SPACE can be available on many DATES
One SPACE can have many BOOKINGS
One USER can make many BOOKINGS
