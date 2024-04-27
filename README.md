# Setup
Clone the repository
```
git clone https://github.com/scottbarnes/haproxy-demo
```

Edit `haproxy/haproxy.cfg` and change the IP in the last line from `192.168.0.11` to
the IP of the host running the FastAPI container (possibly your desktop).

Then visit http://<that_ip>:8082/name/whatever

Compare visiting http://localhost:3001/name/whatever directly.
