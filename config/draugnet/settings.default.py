# misp config - make sure that you use credentials of a non privileged user meant to handle all requests coming from abracadabra
misp_config = {
    'url': 'https://your-misp-instance/',
    'key': 'YOUR_MISP_API_KEY',
    'verifycert': True
}

# redis config
redis_config = {
    'host': 'redis',
    'port': 6379,
    'db': 5
}

# List all allowed frontend origins here
allowed_origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

# abracadabra config
abracadabra_config = {
   "misp_object_templates": [

   ]
}
