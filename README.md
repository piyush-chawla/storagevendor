API for the list of Storage Vendor 

For Mac / Linux users, perform below to setup the environment

$ sudo apt update
$ sudo apt install python3-pip

**Requirement**
$ pip install flask

**RUN**

$ python3 api.py

**Documentation**


GET - To fetch the list of all Storage Vendors

```
ubuntu@ubuntu:~/Documents/mywork$ curl -u piyush:pc1611 -i -X GET http://127.0.0.1:5000/api/v1/resources/storagevendor/all
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 222
Server: Werkzeug/1.0.1 Python/3.10.4
Date: Wed, 18 May 2022 01:58:23 GMT

[
  {
    "Product": "VMAX", 
    "Vendor": "DellEMC", 
    "id": 0
  }, 
  {
    "Product": "Isilon", 
    "Vendor": "DellEMC", 
    "id": 1
  }, 
  {
    "Product": "FAS2012", 
    "Vendor": "NetApp", 
    "id": 2
  }
]
ubuntu@ubuntu:~/Documents/mywork$ 


```

In order to fetch record of any particular vendor/id, run below

```
ubuntu@ubuntu:~/Documents/mywork$ curl -u piyush:pc1611 -i -X GET http://127.0.0.1:5000/api/v1/resources/storagevendor?id=0
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 74
Server: Werkzeug/1.0.1 Python/3.10.4
Date: Wed, 18 May 2022 01:57:17 GMT

[
  {
    "Product": "VMAX", 
    "Vendor": "DellEMC", 
    "id": 0
  }
]
ubuntu@ubuntu:~/Documents/mywork$ 

```
