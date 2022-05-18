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
ubuntu@ubuntu:~/Documents/mywork$ curl http://127.0.0.1:5000/api/v1/resources/storagevendor/all
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
