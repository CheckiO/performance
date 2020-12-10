build-all:
	docker build -t "nginx_proxy" -f nginx_proxy/Dockerfile nginx_proxy/
	docker build -t "django" -f django/Dockerfile django/

start-all:
	docker-compose -f nginx_proxy/docker-compose.nginx_proxy.yml \
				   -f django/docker-compose.django.yml \
				   up
