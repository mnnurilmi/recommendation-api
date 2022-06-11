import csv

class VideoData:
  def __init__(self, id, description, thumbnail, genre):
    self.id = id
    self.genre = genre
    self.thumbnail = thumbnail
    self.description = description

VideoArray = []

with open('data.csv', encoding="utf-8") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      line_count += 1
    else:
      tempVidData = VideoData(row[0], row[1], row[2], row[3])
      VideoArray.append(tempVidData)

def getGenre(id):
  return VideoArray[id-1].genre

def genreSplice(genre):
  x = genre.split("|")
  return x

def genretoInt(array):
  returnValue = []
  switcher = {
    "Kuliner": 2,
    "Homecare": 3,
    "Healthcare": 4,
    "Tutorial": 1,
    "Ecommerce": 5,
    "Marketing": 7,
    "Review": 6
  }

  for element in array:
    returnValue.append(switcher.get(element, 0))

  return returnValue
    

def genreConcat(array):
  returnValue = []
  for element in array:
    x = genreSplice(getGenre(element))
    returnValue += x
  return genretoInt(returnValue[:20])

# inputArray = [1, 2, 3, 4, 5]
# outputArray = genreConcat(inputArray)

# print(outputArray)