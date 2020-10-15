# Diamond-price-prediction
### Diamond price analysis ,prediction using regression models and deployment with Flask and REST-API
![](https://github.com/kaouta/Diamond-price-prediction/blob/master/webapp_1.png)
![](https://github.com/kaouta/Diamond-price-prediction/blob/master/webapp_2.png)
This data science project walks through step by step process of how to build a diamond price prediction website. I  first build a model using sklearn and regression algorithms using diamond dataset from kaggle.com. 
Second step I wrote a python flask server that uses the saved model to serve http requests. 
Third component is the website built in html, css and javascript that allows user to enter diamond informations:color,carat etc and it will call python flask server to retrieve the predicted price.
# the model building step cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering etc. 
## Technology and tools wise this project covers,

* Python
* Numpy and Pandas for data cleaning
* Matplotlib for data visualization
* Sklearn for model building
* Jupyter notebook, visual studio code and pycharm as IDE
* Python flask for http server
* HTML/CSS/Javascript for UI

The models used accuracies:

![](https://github.com/kaouta/Diamond-price-prediction/blob/master/accuracies.png)  ![](https://github.com/kaouta/Diamond-price-prediction/blob/master/regressio_models.png)
as we can see , the lasso regression wored the best for our models with accuracy 90%
# Ressources:
for flask and rest-api part:https://rubikscode.net/2020/02/10/deploying-machine-learning-models-pt-1-flask-and-rest-api/
