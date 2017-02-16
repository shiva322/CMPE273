import psutil

c_count = dict()
p_c_map = dict()


for c in psutil.net_connections(kind='tcp'):
    #print c
    if( c.raddr ) : #and str(c.pid)!='None'
        try :
            c_count[c.pid] += 1
            p_c_map[c.pid].append([c.pid,"%s@%s" % (c.laddr),"%s@%s" % (c.raddr),c.status,])                    
        except KeyError:
            c_count[c.pid] = 1
            p_c_map[c.pid] = []
            p_c_map[c.pid].append([c.pid,"%s@%s" % (c.laddr),"%s@%s" % (c.raddr),c.status,])

#print c_count
#print p_c_map
    
print '"pid","laddr","raddr","status"'
for i in sorted(c_count,key=c_count.get, reverse=True) :
    for v in p_c_map[i]:
        print str(v).replace("'",'').replace("[",'"').replace("]",'"').replace(', ','","')

