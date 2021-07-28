import joblib 
#load the model 
loaded_model = joblib.load('dib_79.pkl')
pred = loaded_model.predict([[10,20,30,40,50,60,70,80]])
if pred[0] == 1:
    print('the person is diabetic')
else:
    print('the person is not diabetic')