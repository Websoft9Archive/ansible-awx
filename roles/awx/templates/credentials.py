DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "{{awx_postgres_password}}",
        'HOST': "{{awx_docker_gateway.stdout}}",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "WDBjM1hQNWVoazI3RzctM3lsQ2Q="
