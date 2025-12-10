import requests


def Disney():
    response = requests.get(f"https://www.amiiboapi.com/api/")
    if response.status_code!=200:
        print("Error fetching data!")
        return None
    data=response.json()
    return{

        "amiiboSeries" : data["amiiboSeries"]
        ""

    }
