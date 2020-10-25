import requests
def request(countryName):
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"format":"json","name":countryName}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "YOUR API KEY"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
