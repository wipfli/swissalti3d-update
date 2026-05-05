import os

old_urls = set()
with open('mapterhorn/source-catalog/swissalti3d/file_list.txt') as f:
    old_urls = set([line.strip() for line in f.readlines()])

current_urls = ()
with open('current_file_list.txt') as f:
    current_urls = set([line.strip() for line in f.readlines()])

new_urls = []
with open('new_file_list.txt') as f:
    new_urls = [line.strip() for line in f.readlines()]

os.makedirs('source-store/swissalti3d', exist_ok=True)

for url in current_urls:
    filename = url.split('/')[-1]
    dst = f'source-store/swissalti3d/{filename}'
    src = None
    if url in old_urls:
        src = f'source-store/oldswissalti3d/files/{filename}'
    else:
        src = f'source-store/updateswissalti3d/{filename}'
    os.replace(src, dst)
