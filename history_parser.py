import json
with open("history.json", "r") as f:
  history = json.loads(f.read())

locations = {"type": "FeatureCollection", "features": []}


limit = 10
for loc in history["locations"]:
  if limit <= 0:
    break
  limit -= 1
  locations["features"].append({
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [
        loc["latitudeE7"] / (10**7),
        loc["longitudeE7"] / (10**7)
      ]
    },
    "properties": {
      "name": "Point " + str(10 - limit)
    }
  })

with open("history_features.json", "w") as f:
  f.write(json.dumps(locations))