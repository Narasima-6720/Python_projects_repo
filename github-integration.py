
import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

creators={}
if response.status_code==200:
    details=response.json()
    for i in details:
        creator=i["user"]["login"]
        if creator in creators:
            creators[creator]+=1
        else:
            creators[creator]=1
    for creat,count in creators.items():
        print(f"{creat}:{count}")
else:
    print("Failed to retrieve data.Status code:",response.status_code)
