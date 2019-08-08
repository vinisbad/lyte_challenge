#This is a sample Image 
FROM ubuntu
MAINTAINER vinisgood@gmail.com 

RUN apt-get update 
RUN apt-get install python3 python3-requests --no-install-recommends -y
Add get_requests.py /opt/

ENTRYPOINT ["python3", "-u", "/opt/get_requests.py", "5", "30", "https://www.facebook.com"] 
