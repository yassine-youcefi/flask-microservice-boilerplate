# flask-microservice-boilerplate
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)

## This is a basic boilerplate of building a Microservice on top of Flask
### Flask application will get the dta from Elasticsearch db and return the results based on the query parameters

## Start-up

### Pleas follow the steps below.

<br>
1. run elasticsearch and kibana 

```bash
docker-compose -f elasticsearch-docker-compose.yml up -d
```

2. build flask image

```bash
docker-compose -f docker-compose.yml up --build
```

<br>

## Fill some data to the Elasticsearch local database

### 1- Create the index :
PUT  http://localhost:9200/property/

Body : json
```json 
{
"settings": {
   "index": {
         "number_of_shards": 1,
         "number_of_replicas": 1
   },
   "analysis": {
     "analyzer": {
       "analyzer-name": {
             "type": "custom",
             "tokenizer": "keyword",
             "filter": "lowercase"
       }
     }
   }
 }  
}
```

### 2- insert data to the elasticsearch:
POST  http://localhost:9200/property/prop/ 

Body : json
```json 
{
"title": "dumy title",
"size" : 4,
"city" : "Dubai"
}
```


