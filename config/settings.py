import os


DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY', '')
ELASTICSEARCH_HOST=os.environ.get('ELASTICSEARCH_HOST', 'elasticsearch')
ELASTICSEARCH_PORT=os.environ.get('ELASTICSEARCH_PORT', '9200')
