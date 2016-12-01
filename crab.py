import random
import csv
from crab.models.datamodel import *


# ---- crea un archivo csv con items y ratings al azar ---#

# fieldnames=['user_id', 'item_id', 'start_rating']
# with open('dataset-recsys2.csv', "w") as myfile:
#     writer= csv.DictWriter(myfile, delimiter=',', fieldnames=fieldnames)
#     writer.writeheader()
#
#     for x in range(1,21):
#         items = random.sample(list(range(1,41)), 20)
#         random.randint(1,5)
#         for item in items:
#             writer.writerow({'user_id':x, 'item_id':item, 'start_rating': random.randint(1,5)})

# --- crea un archivo csv ---#

#se lee le archivo y se crea un diccionarios en python

dataset ={}

with open('dataset-recsys.csv') as myfile:
    reader = csv.DictReader(myfile, delimiter=',')
    i=0
    for line in reader:
        i += 1
        if(i==1):
            continue
        if (int(line['user_id']) not in dataset):
            dataset[int(line['user_id'])] = {}

            dataset[int(line['user_id'])][int(line['item_id'])] = float(line['star_rating'])

# se crea un modelo de datos
# model = MatrixPreferenceDataModel(dataset)

#similarity = ItemSimilarity(model, euclidean_distance, 3)



