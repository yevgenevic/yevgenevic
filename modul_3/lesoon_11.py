import httpx
# params = {'key1': 'value1', 'key2': 'value2'}
# r = httpx.get('https://httpbin.org/get', params=params)
# print(r.text)

try:
    response = httpx.get("https://www.example.com/")
    response.raise_for_status()
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")
except httpx.HTTPStatusError as exc:
    print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
