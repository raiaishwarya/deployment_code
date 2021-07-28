import pickle 
#load the model 
loaded_model = pickle.load(open('dib_79.pkl','rb'))
pred = loaded_model.predict([[10,20,30,40,50,60,70,80]])
if pred[0] == 1:
    print('the person is diabetic')
else:
    print('the person is not diabetic')