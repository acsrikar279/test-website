import requests

subscription_key = '01e2e5092e7e4ed4a95c3a0c6ed6e5c6'
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
search_term = "django"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
print(type(search_results))
rows = "\n".join(["""<tr>
                       <td><a href=\"{0}\">{1}</a></td>
                       <td>{2}</td>
                     </tr>""".format(v["url"],v["name"],v["snippet"]) \
                  for v in search_results["webPages"]["value"]])
with open('test.html','w') as f:
    f.write(rows)
    f.close()
print(search_results.keys() )
print(rows)
