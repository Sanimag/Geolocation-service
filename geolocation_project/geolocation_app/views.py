import geoip2.database
from django.http import JsonResponse, HttpResponse

# from geolocation_pb2 import GeolocationResponse
# from geolocation_pb2_grpc import GeolocationServiceServicer

# class GeolocationService(GeolocationServiceServicer):
#     def GetGeolocation(self, request, context):
#         ip_address = request.ip_address
#         # Replace 'path/to/your/database.mmdb' with the path to your MaxMind GeoIP2 database file
#         reader = database.Reader('GeoLite2-City_20240109/GeoLite2-City.mmdb')
#         try:
#             response = reader.city(ip_address)
#             return GeolocationResponse(
#                 country=response.country.name,
#                 city=response.city.name,
#                 # Add other relevant geolocation information here
#             )
#         except database.AddressNotFoundError:
#             context.set_code(grpc.StatusCode.NOT_FOUND)
#             context.set_details(f"Geolocation not found for IP address: {ip_address}")
#             return GeolocationResponse()

def index(request):
    return HttpResponse("Assalamualeikum dunya")

def GetGeolocation(request):
    ip_address = request.META["REMOTE_ADDR"]
    response_data = {}
    with geoip2.database.Reader("GeoLite2-City_20240109/GeoLite2-City.mmdb") as reader:
        try:
            response = reader.city(ip_address)
        except:
            return JsonResponse({"Error":"This ip address: {ip_addr} is not listed in database. Will be solved in the future".format(ip_addr=ip_address)})
        response_data["city"] = response.city.name
        response_data["subdivision"] = response.subdivisions.most_specific.name
        return JsonResponse(response_data)