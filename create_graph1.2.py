import networkx as nx
import pickle
import kcore_decomposition as kde
import kcorenew as kc
import jaccards as j

f1 = open("density.txt","w")
fu = open('unique_nodes.txt',"w")
topc = []
edges = []
top5c = []
top5b = []
f = open("primaryschool.csv")
count = 31220
counts = 3600
couns1 = 0
couns = 0
for v in f:
  couns=couns+1
  v = v.strip("\n")
  v = v.split("\t")
  t = []
  for x in v:
    try:
    	t.append(int(x))
    except:
	pass
  if t[0] < count+counts:
	edges.append((t[1],t[2]))	
  else:
	couns1 = couns1+1
	count=t[0]
	g = nx.Graph()
	g.add_edges_from(edges)
	c1 = nx.closeness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        cloa = []
        for x in c4:
                cloa.append(x[0])
        c1 = nx.betweenness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        bwoa = []
        for x in c4:
                bwoa.append(x[0])
	#print t[0],nx.number_of_nodes(g),nx.number_of_edges(g)
	top5c.append(cloa)
	top5b.append(bwoa)
	sh = kc.ksize(g)
	v = sh.items()
	topc.append(v[-1][1])
	g1 = g.subgraph(v[-1][1])
  	edges = []
	edges.append((t[1],t[2]))
	f1.write(str(count)+'\t'+str(nx.density(g1))+'\n')
	fu.write(str(count)+'\t'+str(g.number_of_nodes())+'\n')

print counts,count,couns1,couns
j.jaccards(top5c,'close')
j.jaccards(top5b,'bets')
j.jaccards(topc,'kcore')
pickle.dump(top5c,open('topclose5.p','wb'))
pickle.dump(top5b,open('topbet5.p','wb'))
pickle.dump(topc,open('topcore.p','wb'))
f1.close()
fu.close()
