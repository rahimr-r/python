import numpy as np
marks = np.array([[70, 80, 90],[60, 75, 85],[88, 92, 79],[55, 65, 70]])

print("Shape:",marks.shape)
print("Data type:",marks.dtype)
print("Size:",marks.size)
print("Slicing of first 2 students and last subjects:",marks[0:2,2])

print("Students average:",np.mean(marks,axis=1))
print("Subjects average:",np.mean(marks,axis=0))

grace=marks+5
print("Grace marks:",grace)

weights=np.array([0.3,0.3,0.4])
scores=np.dot(marks,weights)
print("Weighted scores:",scores)

order=np.arange(12)
reshaped=order.reshape(3,4)
print("Reshaped:\n",reshaped)
