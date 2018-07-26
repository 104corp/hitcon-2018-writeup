Crack shadow

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/01.crack%20shadow.png)

Fast check subnet port 8080 open

```bash
#!/bin/bash

for ip in $(seq 0 255); do
nc -zv -w 1 192.168.2.$ip 8080 2>&1 | grep succeeded &
done
```

Ex.
```
Connection to 192.168.2.172 8080 port [tcp/http-alt] succeeded!
Connection to 192.168.2.203 8080 port [tcp/http-alt] succeeded!
```

Tunnel
```
ssh -L 8888:192.168.2.203:8080 hitcon2018@18.182.82.221
```

Weak password for using dig

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/02.weak%20password.png)

Command injection

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/03.command%20injection.png)

Get the key

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/04.get%20key.png)

Another tunnel
```
ssh -L 8888:192.168.2.172:8080 hitcon2018@18.182.82.221
```

Use the key

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/05.use%20key.png)

SQL injection page

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/06.SQL%20injection.png)

Looks like blind SQL injection

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/07.blind%20SQL%20injection.png)

Blind SQL ture test

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/08.blind%20SQL%20true%20test.png)

Blind SQL false test

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/09.blind%20SQL%20false%20test.png)

Use [bsqli.py](https://github.com/104corp/hitcon-2018-writeup/blob/master/NETWORK/bsqli.py) and get Flag

![](https://github.com/104corp/hitcon-2018-writeup/raw/master/NETWORK/10.bsqli.py%20get%20flag.png)
