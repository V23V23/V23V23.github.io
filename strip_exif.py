import os
from PIL import Image

BASE = r'C:\Users\32902\Desktop\Dphoto\images'

folders = ['Tibet', 'changsha', 'chongqing', 'coast', 'dujiangyan', 'northwest']

for folder in folders:
    path = os.path.join(BASE, folder)
    if not os.path.isdir(path):
        continue
    files = [f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg'))]
    for f in files:
        fp = os.path.join(path, f)
        img = Image.open(fp)
        icc = img.info.get('icc_profile')
        img.save(fp, 'JPEG', quality=95, icc_profile=icc)
        print(f'Stripped: {folder}/{f}')

print('Done — all EXIF data removed, ICC profiles preserved.')
