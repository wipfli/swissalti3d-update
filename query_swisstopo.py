import requests
import json

url = 'https://ogd.swisstopo.admin.ch/services/swiseld/services/assets/ch.swisstopo.swissalti3d/search?format=image/tiff; application=geotiff; profile=cloud-optimized&resolution=0.5&srid=2056&state=current&csv=true'

print(f'loading {url}...')
r = requests.get(url)
if r.status_code != 200:
    print(f'Error: status code {r.status_code}. Aborting...')
    exit(1)

link_data = json.loads(r.text)
csv_url = link_data['href']

print(f'loading {csv_url}...')
r = requests.get(csv_url)

lines = sorted(r.text.split('\n'))
print(f'received {len(lines)} lines')

print(f'writing current_file_list.txt')
with open('current_file_list.txt', 'w') as f:
    f.write('\n'.join(lines))