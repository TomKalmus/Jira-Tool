import requests
class APIClient:
  def __init__(self, base_url, api_token):
    self.base_url = base_url
    self.api_token = api_token

  def get_data(self):
    headers = {
        "x-api-token": self.api_token
    }
    response = requests.get(self.base_url, headers=headers)
    print("Response from server:", response.text)

def main():
  client = APIClient("https://example.com", "qk9KiCnUAMJitZwYkcR8")
  client.get_data()

if __name__ == "__main__":
    main()
