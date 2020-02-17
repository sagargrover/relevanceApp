# Relevance App

Provides validity for given text

## Getting Started

[Swagger documentation](https://v4-bg6nis3tdq-de.a.run.app/apidocs)


Sample URL(on gcloud)
```
curl --location --request POST 'https://v4-bg6nis3tdq-de.a.run.app/api/v1/getRelevance' \
--header 'Content-Type: application/json' \
--header 'x-myntra-abtest: v1=personalised' \
--data-raw '{
    "text": "gnition knock (detonation) sensor senso fits 01 06 bmw 325ci 2 5l l6"
}'
```

HLD -
```
https://docs.google.com/document/d/1j0B70r2YgVEk9hI47v_uKoxew9RxldACrHSbCVtbAGw/edit?usp=sharing
```
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

If everything works, this curl
```
curl --location --request POST 'https://localhost:8080/api/v1/getRelevance' \
--header 'Content-Type: application/json' \
--header 'x-myntra-abtest: v1=personalised' \
--data-raw '{
    "text": "gnition knock (detonation) sensor senso fits 01 06 bmw 325ci 2 5l l6"
}'
```
should return
```
{
    "is_valid": "1"
}
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

