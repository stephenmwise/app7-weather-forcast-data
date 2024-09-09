import requests


def get_data(place, forecast_days=None):
    API_KEY = "b58037fe771742ec4f59d4cccb900b4f"
    url = (f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))

