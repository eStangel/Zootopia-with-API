import requests

API_KEY = "WY2uY+QjetTXRE4JPQbszQ==4gv9qeukzJkNXygX"


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  headers = {"x-api-key": API_KEY}
  response = requests.get(url, headers=headers)
  response_json = response.json()
  return response_json
