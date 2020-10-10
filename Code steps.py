$ cd Desktop


$ mkdir fastapi-ml


$ cd fastapi-ml

$ conda create -n env python=3.8


conda activate env  (To deactivate use - conda deactivate env)


$ pip install -r requirements.txt


$ python


>>> from model import train, predict, convert
>>> train()
>>> prediction_list = predict()
>>> convert(prediction_list)


train("FB")

train("AAPL")

train("AMZN")

train("NFLX")

train("GOOG")

train("TSLA")



(CTRL + Z) to exit the shell



$ heroku login



$ git add -A


$ git commit -m "init"

$ heroku create


$ git remote -v


$ git add -A


$ git commit -m "add procfile"


https://fast-crag-09638.herokuapp.com/docs
