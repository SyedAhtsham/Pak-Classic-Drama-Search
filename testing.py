#
# dramas = list()
#
# file = open('IndexingOfDramas1.txt', 'r')
#
# for line in file:
#     data = line.strip('\n').split('*')
#     dramas.append(data[6])
#
#
# for drama in dramas:
#     print(drama)

dramas = list()
file = open('IndexingOfDramas1.txt', 'r')
i = 0
for line in file:
    data = line.strip('\n').split('*')
    if i==0:
        i += 1
        continue
    dramas.append([data[1],data[2], data[4], data[5], data[6]])


for drama in dramas:
    print(drama)

# import glob
#
#
#
#
# imagesNames = list()
#
# imagesNames = glob.glob("static/images/*")
# dramaImages = list()
# for image in imagesNames:
#     data = image.split("/")
#     dramaImages.append(data[2].split('.')[0])
#
# for image in dramaImages:
#     print(image)