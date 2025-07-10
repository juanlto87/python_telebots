import requests

data = requests.get('https://fakestoreapi.com/products').json()
print(data[0])  

for prod in data:
    print(f"{prod['title']} - ${prod['price']}")
    
for prod in data:
    if prod['category'] == 'electronics':
        print(f"{prod['title']} - ${prod['price']}")

