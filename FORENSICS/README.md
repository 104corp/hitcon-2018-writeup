```bash
file flag
flag: 7-zip archive data, version 0.4
```


Decompress 7-zip
```bash
file flag
flag: tcpdump capture file (little-endian) - version 2.4 (Ethernet, capture length 262144)
```


Wireshark
![](https://github.com/104corp/hitcon-2018-writeup/raw/master/FORENSICS/1.Wireshark%20filter.png)

flag.png
![](https://github.com/104corp/hitcon-2018-writeup/raw/master/FORENSICS/2.flag.png)


Unhide Steganography
![](https://github.com/104corp/hitcon-2018-writeup/raw/master/FORENSICS/3.unhide.png)


Get floats
```
435.0783
62.40823
125.69146
60.54885
16.3252
42.5254
125.08209
97.0508
42.38479
17.27052
60.65823
124.75396
42.5176
38.5254
23.2002
38.54885
22.19239
40.38479
23.20802
24.21192
21.19239
17.27442
18.27442
17.22364
24.21974
19.20802
40.3926
22.48927
```

python struct pack each float with format '>d'

```
@{1@..4n
@O4@.q..
@_l@.q..
@NF@..4n
@0S@N...
@EC@N...
@_E@.jU.
@XC@N...
@E1@.x..
@1E@.x..
@NT@.q..
@_0@.q..
@EB@..4n
@CC@N...
@73@N...
@CF@..4n
@61@x...
@D1@.x..
@75@.x..
@86@c.^J
@51@x...
@1F@c.^J
@2F@c.^J
@19@x...
@88@.q..
@35@.x..
@D2@..4n
@6}@.x..
```

Pick second and third bytes from packed floats and get key
```
{1O4_lNF0SEC_EXCE11ENT_0EBCC73CF61D17586511F2F198835D26}
```

# Patch
```python
a = open('flag_unpatch.png', 'rb').read()
b = open('patch.bin', 'rb').read()
c = a[:326875]+b+a[326875:]
open('flag_patched.png', 'wb').write(c)
```
