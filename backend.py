import requests

API_KEY = "405f3fe87db99077a1e188bb0e805b64"


def get_data(place, days=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="London", days=2))

#def get_data(days):
#    dates = ["1", "2", "3", "4", "5"]
#    temperatures = [20, 22, 20, 22, 20]
#    temperatures = [days * i for i in temperatures]
#    return dates, temperatures
