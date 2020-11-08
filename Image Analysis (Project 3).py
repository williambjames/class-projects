#RaspberryCanary
#Oct 16 2020
#Challenge Number 3
#Sources: Class website, NumPy reference site
import numpy as np
import PIL.Image as image
import os
while True:
    try:
        thresh = int(input("Enter a threshold between 0 and 255: "))
        if 0 <= thresh <= 255:
            break
        raise ValueError()
    except ValueError:
        print("Input must be an integer between 0 and 255.")
path = '/Users/williamjames/Documents/343 Data/ch3/RaspberryCanary/rebelmrkt'
pics = os.listdir(path)
pic_list = [filename for filename in pics]

total = []
for x in pic_list:
  img = np.float32(image.open(path+'/'+x))
  try:
    total = total + img
  except:
    total = img
avg = total/len(pic_list)
avg_image = image.fromarray(avg.astype(np.uint8))
avg_image.show()

#Standard Deviation
std = []
for x in pic_list:
  img = np.float32(image.open(path+'/'+x))
  try:
    diff = (abs(img-avg))**2 #square of |x-mean|
    std = std + diff #sum of |x-mean|^2
  except:
    std = img
std /= len(pic_list) #div by #of sample points
std = std**(1/2) #sqrt of that = STD
std_image = image.fromarray(std.astype(np.uint8))
std_image.show()

#Build new image
new = avg
for row in range(len(std)): #loops over the number of rows in the image
    for col in range(len(std[row])): # loops over the number of columns in the current row
        if (std[row][col]>thresh).any():
          new[row][col] = [255.0,0.0,0.0]
        else:
          new[row][col] = avg[row][col]
image.fromarray(new.astype(np.uint8)).show()

