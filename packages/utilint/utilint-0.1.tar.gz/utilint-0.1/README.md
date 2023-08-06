# 🔬 UtilINT
### Turn boring osint data to interesting informations
## 🥇 Abilities
- Determine groups of locations, their center, filters the uneseful ones, based on a simple list of your provided coordinates list. This can be used to **determine your target's location** based on the ones he is frequenting.
- _**Guess timezone** and preview activity over weeks, only based on a list of timestamp you provide._
- ...
## 📲 Installation
```
pip install utilint
```
## 🛠️ Usage
### 🗺️ Geolocation
```py
# First, import the `locations` module of the `utilint` library.
from utilint import locations
import json

# Use the `locations.HashablePoint` object to put a location.
# Here, i have randomly placed 4 locations in Paris, 2 in Spain,
# and one in Africa.
locs = [
    locations.HashablePoint.from_string('''48°51'12.75"N   2°20'52.02"E'''),
    locations.HashablePoint.from_string('''48°50'50.78"N   2°18'43.26"E'''),
    locations.HashablePoint.from_string('''37°53'30.13"N   4°48'09.72"W'''),
    locations.HashablePoint.from_string('''21°13'51.74"N  11°46'45.18"W''')
    locations.HashablePoint.from_string('''48°51'55.07"N   2°18'49.56"E'''),
    locations.HashablePoint.from_string('''37°53'17.48"N   4°46'44.56"W'''),
    locations.HashablePoint.from_string('''48°49'27.84"N   2°19'26.32"E'''),
]
```
The object `locations.HashablePoint` is an instance of `geopy.Point`. As so, you can [read this](https://geopy.readthedocs.io/en/stable/index.html?highlight=point#geopy.point.Point) to learn of to init it with different kind of values. *Note however that `altitude` will always be `0`, even if you init it, because of technical reasons*.
```py
# Then we can estimate groups and center of locations with the
# `locations.estimate()` function.
result = locations.estimate(locs)

# And then i print the results
print(result)
```
Which gives me:
```py
[
    (Point(48.8529599537037, 2.313742592592592, 0.0), 4),
    (Point(37.889945833333336, -4.790872222222222, 0.0), 2),
    (Point(21.23103888888889, -11.779216666666667, 0.0), 1)
]
```
So i can see i have 3 distinct groups:
| Paris, 4 locations | Spain, 2 locations | Africa, 1 location |
| :---: | :---: | :---: |
| ![](./src/paris.png) | ![](./src/spain.png) | ![](./src/africa.png) |
