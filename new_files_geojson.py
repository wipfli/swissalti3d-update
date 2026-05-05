import json
from rasterio.warp import transform_bounds

def read_bounds(filepath):
    bounds = []
    with open(filepath) as f:
        lines = [line.strip() for line in f.readlines()]
        lines = lines[1:]
        for line in lines:
            parts = line.split(',')
            filename = parts[0]
            left, bottom, right, top, _, __ = [float(a) for a in parts[1:]]
            bounds.append({
                'filename': filename,
                'left': left,
                'bottom': bottom,
                'right': right,
                'top': top,
            })
    return bounds

def to_geojson(data):
    src_crs = "EPSG:3857"
    dst_crs = "EPSG:4326"

    left, bottom, right, top = transform_bounds(
        src_crs, dst_crs,
        data['left'], data['bottom'],
        data['right'], data['top']
    )

    return {
        "type": "Feature",
        "properties": {
            "filename": data["filename"]
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [left, bottom],
                [right, bottom],
                [right, top],
                [left, top],
                [left, bottom]
            ]]
        }
    }

old_bounds = read_bounds('source-store/oldswissalti3d/bounds.csv')
bounds = read_bounds('source-store/swissalti3d/bounds.csv')

old_filenames = set([item['filename'] for item in old_bounds])

features = []
for item in bounds:
    if item['filename'] not in old_filenames:
        features.append(to_geojson(item))

with open('new_files.geojson', 'w') as f:
    json.dump({'type': 'FeatureCollection', 'features': features}, f, indent=2)