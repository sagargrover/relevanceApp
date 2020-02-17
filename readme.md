# Relevance App

Provided validity for given text

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

What things you need to install the software and how to install them

1. Go to project folder
```
Change resource_dir path in config.yml
```
2. Build

Using docker

```
docker image build -t relevance .
docker run -d --name relevanceContainer -it relevance:latest

```

Using source
```
virtualenv --python=/usr/bin/python3.7 venv
gunicorn service.app:app -b 0.0.0.0:8080 --workers 1 -t=300
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests


```
python -m unittest discover -s tests/ -p '*_test.py'
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Deploy using gcloud
```
gcloud run deploy --image gcr.io/relevantgrab/v1 --platform managed
gcloud builds submit --tag gcr.io/relevantgrab/v1
```

## Built With

* [FLask](https://www.palletsprojects.com/p/flask/) - The web framework used
* [pip] - Dependency Management


## Authors

* **Sagar Grover** - *Initial work* - [SagarGrover](https://github.com/sagargrover)

