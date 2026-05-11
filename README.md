# swissalti3d-update
Update the swissalti3d source of Mapterhorn

## Steps

Query what the current file list of Swisstopo is and write it to current_file_list.txt with:

```
uv run python query_swisstopo.py
```

Find what files are not yet in Mapterhorn and write them to new_file_list.txt with:

```
uv run python new_files.py
```

Download only the new files to folder `source-store/updateswissalti3d`:

```
mkdir -p source-store/updateswissalti3d
cd source-store/updateswissalti3d
cat ../../new_file_list.txt | parallel -j 100 wget -c -q {} 
```

Normalize input:

```
uv run python source_to_cog.py updateswissalti3d
```

Download old files to source-store/swissalti3d:

```
wget https://download.mapterhorn.com/sources/swissalti3d.tar -O swissalti3d.tar
```

Unpack:

```
mkdir source-store/oldswissalti3d
cd source-store/oldswissalti3d
tar xvf ../../swissalti3d.tar
```

Merge new and old files into `source-store/swissalti3d`:

```
uv run python merge.py
```

Create new bounds:

```
uv run python source_bounds.py swissalti3d
```

To show the new files on a map, run:

```
uv run python new_files_geojson.py
```

Polygonize:

```
uv run python source_polygonize.py swissalti3d 32
```

