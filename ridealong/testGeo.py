import json,requests
googleKey = 'AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk'
coordinates=[]
originAddress='West Lafayette, IN, USA'
destAddress='West Lafayette, IN, USA'
originRequest = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + originAddress+'&fields=geometry&key='+googleKey
destRequest = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + destAddress+'&fields=geometry&key='+googleKey
originResponse = requests.get(originRequest)
destResponse = requests.get(destRequest)
origin_json = json.loads(originResponse.text)
dest_json = json.loads(destResponse.text)
print (origin_json['results']['geometry'][0])
coordinates.append(origin_json['results']['geometry']['location']['lat'])
coordinates.append(origin_json['results']['geometry']['location']['lng'])
coordinates.append(dest_json['results']['geometry']['location']['lat'])
coordinates.append(dest_json['results']['geometry']['location']['lng'])
print (coordinates)

