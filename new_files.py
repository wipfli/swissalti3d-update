old_files = []
with open('mapterhorn/source-catalog/swissalti3d/file_list.txt') as f:
    old_files = [line.strip() for line in f.readlines()]

current_files = []
with open('current_file_list.txt') as f:
    current_files = [line.strip() for line in f.readlines()]

new_files = list(set(current_files) - set(old_files))
new_files.sort()

with open('new_file_list.txt', 'w') as f:
    f.write('\n'.join(new_files))

current_files.sort()

with open('file_list.txt', 'w') as f:
    f.write('\n'.join(current_files))
