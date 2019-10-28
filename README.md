# RoboGen Backend Service (based on Docker)
## Steps to run the sample rest service on docker:
1. Clone the Repository 
2. Move to the cloned directory 
3. Build the docker image: "docker-compose build" 
4. Create and run a container: "docker-compose up" oder "docker-compose up -d" 
5. Navigate to http://0.0.0.0:3000/ or http://localhost:3000/ to get "hello world" 

Note: If the image is built inside a private network, you can mention gateway to proxy through
      Ex: docker build --build-arg proxy=<hostname:port> -t python-rest .
	 
Note: hosted at : https://power2dm.salzburgresearch.at/robogen/
	  
	  
## A Sample Client:
```python 
import requests r = requests.post('http://0.0.0.0:3000/v1/api',verify=False, json={"name": "naren"}) 
headers = {'Content-type': 'application/json'} 
print(r.status_code) 

if r.ok:
    print r.content
```
