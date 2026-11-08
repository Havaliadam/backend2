import pandas as pd 
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
df=pd.read_csv("Student_Grades.csv")
y=df["Scores"]
x=df.drop(columns=["Scores","Grade"])

y=y.values.astype("float32")
x=x.values.astype("float32")


model=Sequential()
model.add(Dense(16))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="linear"))
model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")
model.fit(x,y,epochs=32,batch_size=16,verbose=1)
