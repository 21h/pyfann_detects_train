#28x16 448 neurons
from pyfann import libfann
from PIL import Image
import os

datastruct = []
files=[]
learn=[]

for filename in os.listdir("0"):
    if filename.endswith(".png"):
	files.append("0/"+filename)
	learn.append([0])

for filename in os.listdir("1"):
    if filename.endswith(".png"):
	files.append("1/"+filename)
	learn.append([1])

print len(files)
print files
print len(learn)
print learn

for filename in files:
    im = Image.open(filename, 'r')
    pixel_values = list(im.getdata(0))
    datastruct.append(pixel_values)

desired_error = 0.001
max_epochs = 1000
epochs_between_reports = 1000

ann = libfann.neural_net()
ann.create_standard_array((448,150,1))
ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC_STEPWISE)
ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)
train_data = libfann.training_data()
train_data.set_train_data(datastruct, learn)
ann.train_on_data(train_data,max_epochs, epochs_between_reports, desired_error)
ann.save('fann.data')
ann.destroy()