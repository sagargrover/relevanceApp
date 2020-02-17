# Relevance App

Provided validity for given text

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

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

If everything works, this should return output
```
curl --location --request POST 'https://v3-bg6nis3tdq-de.a.run.app/api/v1/getRelevance' \
--header 'Content-Type: application/json' \
--header 'x-myntra-abtest: v1=personalised' \
--data-raw '{
    "text": "gnition knock (detonation) sensor senso fits 01 06 bmw 325ci 2 5l l6"
}'
```

## Running the tests


```
python -m unittest discover -s tests/ -p '*_test.py'
```

## Deployment

Deploy using gcloud
```
gcloud run deploy --image gcr.io/relevantgrab/v1 --platform managed
gcloud builds submit --tag gcr.io/relevantgrab/v1
```

## Built With

* [Flask](https://www.palletsprojects.com/p/flask/) - The web framework used
* pip - Dependency Management


## Authors

* **Sagar Grover** - *Initial work* - [SagarGrover](https://github.com/sagargrover)

