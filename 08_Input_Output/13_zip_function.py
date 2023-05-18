import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']
# for row in albums:
#     zip_object = zip(keys, row)
#     for thing in zip(keys, row):
#         print("\t", thing)
# for row in albums:
#     zip_object = zip(keys, row)
#     albums_dict = dict(zip_object)
#     print(albums_dict)

filename = "albums.csv"
with open(filename, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)
