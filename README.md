1.  How to run project:

-> poetry run python manage.py <img-url>

or run with any env which have pillow package installed

2. Explain possible ways to scale up this chop image function to chop 1,000,000 images as fast as possible.

-> Separate 1m images to smaller batch file which has 1-2k images/batch
execute each batch by adding it to Celery MQ, scaling up celery worker will affect the run time too. However, need to notice about scaling will costs money