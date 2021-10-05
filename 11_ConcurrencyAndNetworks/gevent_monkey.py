import gevent
from gevent import monkey


monkey.patch_all()

hosts = [
        'HOST_NAME_TO_FIND_IP_ADDRESS',
        ]

jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
