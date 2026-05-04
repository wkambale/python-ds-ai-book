# A tuple to store geographic coordinates (latitude, longitude)
# This data should not change, so a tuple is a perfect fit.
nairobi_coordinates = (-1.2921, 36.8219)
print(nairobi_coordinates)
# You can access elements by index, just like a list
latitude = nairobi_coordinates[0]
print(f"Nairobi's Latitude: {latitude}")
# But trying to change the tuple will result in an error
# The following line is commented out because it would crash the program
# nairobi_coordinates[0] = -1.3000  # TypeError: 'tuple' object does not support item assignment