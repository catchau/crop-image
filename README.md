```
1.  How to run project:
-> poetry run python manage.py <img-url> or run with any env which have pillow package installed

2. Explain possible ways to scale up this chop image function to chop 1,000,000 images as fast as possible.
-> Separate 1m images to smaller batch file which has 1-2k images/batch
  + execute each batch by adding it to Celery MQ, scaling up celery worker will affect the run time too.
    *pros: autoscaling, auto_retry, easier to write (just need send task to Celery MQ), big support comunity
    *cons: need to setup Celery server separate from main BE server, may costs more
  + using multithreading of python library
    *pros: no need to setup a new server, optimize using the CPU of main server
    *cons: no autoscaling, need to build and design the multithreading by ourself
-> So Celery would be a better choice
```
