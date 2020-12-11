#!/usr/bin/python3
import pickle
from operator import itemgetter

def load_sorted_clusters(path): #Taken from Wei
    '''
    load gene clusters and sort 1st by abundance and then by clusterID
    '''
    geneCluster_dt=load_pickle(path+'allclusters_postprocessed.cpk')
    # sort by decreasing abundance (-v[0], minus to achieve decreasing)
    # followed by increasing strain count
    gc_items = geneCluster_dt.items()

    return sorted(geneCluster_dt.items(), key=lambda kv: (-itemgetter(0)(kv[1]),itemgetter(2)(kv[1])), reverse=False)
    #return sorted(geneCluster_dt.iteritems(),
    #            key=lambda (k,v): (-itemgetter(0)(v),itemgetter(2)(v)), reverse=False)

def load_pickle(filename):
    f = open(filename,"rb")
    p = pickle.load(f)
    f.close()
    return(p)


