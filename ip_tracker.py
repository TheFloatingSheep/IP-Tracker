import requests

def tracer_ip(adresse_ip):
    # API URL
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check that the IP is valid
        if data['status'] == 'success':
            print(f"IP: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"Postal code: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Internet Service Provider: {data['isp']}")
        else:
            print("Invalid IP address.")
    else:
        print("Error connecting to API.")

if __name__ == "__main__":
    ip_address = input("Enter IP address to trace : ")
    tracer_ip(ip_address)