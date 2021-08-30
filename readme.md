# My Stock
Just a python library to consume yahoo finance api to display some of the stocks I own. It is semi hard coded.

## Install and Run
Use run.py file

Create Virtual environment run the requirements and hit
run.py via CLI command
```
python -m venv ~/.venv/my-stock
source ~/.venv/my-stock/Scripts/activate
python -m pip install -r requirements.txt
python run.py -i Yearly
# or
python run.py
deactivate
```

## Deploy to Lambda
```
cd ~/.venv/my-stock/Lib/site-packages
zip -r ~/tmp/deploy.zip .
cd ~/source/repos/my-stock
zip -g ~/tmp/deploy.zip lambda_function.py
zip -g ~/tmp/deploy.zip stock_plot.py
zip -g ~/tmp/deploy.zip stock_profile.py
```
Use lambda_function.py file

[More Details on Deploy](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).
I am not able to do use this since the entirety of the package would
be over 250 MB. Which unless I want to setup EFS for the Lambda function 
this approach is out of the question.

## Deploy to Flask
```
python -m venv ~/.venv/deploy-stock
source ~/.venv/deploy-stock/Scripts/activate
python -m pip install -r requirements.flask.txt
export FLASK_APP=flask_function
export FLASK_ENV=development
flask run -p 5050
#open browser to http://localhost:5050
deactivate
```
Use flask_function.py file

TODO: Complete Soinshane.API to communicate with this endpoint in 
AWS.

## Soinshsnae
```
mkdir /var/www
cd /var/www
git clone https://github.com/DeadlyChambers/my-stock.git /var/www
mkdir /venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.flask.txt
export FLASK_APP=flask_function
flask run -p 5050

```

### Change the stocks that are in the stock_plot.py file to see your stocks
[How to Change Text Color Maybe](https://stackoverflow.com/questions/57919281)
[Use a different graph type](https://plotly.com/python/axes/)