from geopy.geocoders import Nominatim


def get_coordinates(address):
    print("Start find location")
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="name-of-your-user-agent")
    country = "Malaysia"
    address_parts = address.split(',')
    # Start from the 2nd part of the address becauase geolocator cant find coordinate when there is NO
    for i in range(1, len(address_parts)):  
        partial_address = ','.join(address_parts[i:]).strip()

        try:
            # Retrieve location details
            location = geolocator.geocode(f"{partial_address}, {country}", timeout=None)

            if location:
                # Extract latitude and longitude
                latitude = location.latitude
                longitude = location.longitude
                print(
                    f"Coordinates for '{partial_address}, {country}': Latitude {latitude}, Longitude {longitude}")
                return latitude, longitude
            else:
                print(f"No location found for '{partial_address}, {country}'")

        except Exception as e:
            print("There was an error")
            print(e)

    print("No coordinates found for any part of the address")
    return None, None
