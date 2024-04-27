## Setup
### Clone the repository
```
git clone https://github.com/scottbarnes/haproxy-demo
```
### Edit the configuration
Edit `haproxy-demo/haproxy/haproxy.cfg` and change the IP in the last line from `192.168.0.11` to
the IP of the host running the HAProxy container (possibly your desktop).

These can both be run on the same machines, or different machines. The configuration by default
assumes:
- you're running the FastAPI container on localhost;
- you're running the HAProxy container on a host with IP 192.168.0.11 (which could be localhost),
- you have ports 3001 (FastAPI) and 8082 free (on their respective hosts).

### Run the containers
```
cd haproxy-demo/haproxy
docker compose up
cd ../fastapi
docker compose up
```

### Try it out
Then visit http://<the_ip_you_put_in_haproxy.cfg>:8082/name/whatever

Compare visiting http://localhost:3001/name/whatever directly.
