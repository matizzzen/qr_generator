import requests

key = r'jOBFVqLS82zBVh6skcr77g_sE2IzjB_y7zQrSeKHvOII3F1DGt9ttZZ9UBDV5rJn'
url = r'https://api.qr-code-generator.com/v1/create?access-token='

url = url + key

link = input('url:')
name = input('name:')

payload = {
    'frame_name': 'no-frame',
    'qr_code_text': link,
    'image_format': 'SVG',
    'qr_code_pattern': 'rounded-2',
}


r = requests.post(url, data=payload)

with open(f'qr_{name}.svg', 'w') as f:
    f.write(r.text)
