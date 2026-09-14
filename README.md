# patrickcanal.it

## Docker 
Build container 
`docker build . -t patrickcanal.it`

Run docker run 
`docker run -p 8000:8000 patrickcanal.it -v "$(pwd)/patrickcanal.it/local_settings.py:/app/patrickcanal.it/local_settings.py" -v "$(pwd)/patrickcanal.it/db.sqlite:/app/db.sqlite"`

## Required variables
### Portfolio
Email variables will be replaced once `django-post_office` will be updated to support django 6.1 email system
- MAILER_HOST
- EMAIL_CONTACT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- EMAIL_PORT
- EMAIL_USE_TLS
