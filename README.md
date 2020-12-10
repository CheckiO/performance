Test Project consists of two containers

1. nginx_proxy
    Dockerfile : nginx_proxy/Dockerfile
    Compose: nxinx_proxy/docker-compose.nginx_proxy.yml
   
2. django
    Dockerfile : django/Dockerfile
    Compose: django/docker-compose.django.yml
    Base Django project that have one rest-framework api: django/project
   
    Django Image consists of python3.9.0 base image, Django, Djangorestframework, Nginx, Gunicorn, Supervisord.
    Supervisord launches Gunicorn, which launches django instance with 4 workers
   
3. Nginx_proxy and Django are only containers than are run on machine

4. In Folder Monitoring we have script that is used to check performance
   Command run_digitalocean.sh is bash script that launch python script every second
   Python script run.py makes one request to djangorestframework API from django container. 
   Upon receiving response script calculates time it took to run and logs it into the file results.txt
   Every line of the file shows how long request took place and time at which it happened
   
5. We run same configuration on digitalocean machine (our instance ID - 219483110) and linode instance
   Configuration of both machines identical (Ubuntu 18.04 with 1 GB memory and 1 cpu - Minimal 5 usd configuration)
   Script to monitor response times were launched at both machines. We provided result of logs in monitoring/recorded_data folder 

6. performance_result folder provides results of running scripts 

Script was running on Both Machines from
Tue Dec  9 17:00:00 UTC 2020
to
Thu Dec 10 09:00:00 UTC 2020
