import sys, re, string

interactions = {}
#user_id -> list of paired users
pair_list = {}
#set of all (id1,id2) pairs
pairs_map = {}
clusters = {}

def add_interaction(id1,id2):
    interactions[(id1,id2)] = True
#end

def process_pairs():
    for id1,id2 in interactions:
        if (id2,id1) in interactions:
            if not id1 in pair_list:
                pair_list[id1] = []
            #end
            pair_list[id1].append(id2)
            pairs_map[(id1,id2)] = True            
        #end
    #end
#end

def build_clusters():
    #try to build a cluster starting at each user
    
    for anchor,adjacent_list in pair_list.iteritems():
        #if any of the users that the adjacent is paired to
        #is also paired to the anchor, then it is a cluster
        #to prevent repeats, only consider anchor < adj < adj_adj
        
        for adj in adjacent_list:
            if adj < anchor:
                continue
            #end
            
            for adj_adj in pair_list[adj]:
            
                if adj_adj < adj or adj_adj < anchor:
                    continue
                #end
                
                if (adj_adj,anchor) in pairs_map:
                    clusters[(anchor,adj,adj_adj)] = True
                #end
            #end            
        #end        
    #end     
#end

def add_cluster(cluster):
    #could be faster. some mapping to see all clusters that a user is a part of?

    #if cluster is completely contained within a larger existing cluster
    #ignore it.
    repeated_subcluster = False
    
    for existing_cluster in clusters:
        #does the new cluster contain at least one original element?
        orig_elem = False
        for elem in cluster:
            if elem not in existing_cluster:
                orig_elem = True
                break
            #end
        #end
        if not orig_elem:
            repeated_subcluster = True
            break
        #end        
    #end
    
    if repeated_subcluster:
        return
    #end
    
    #if any existing cluster is completely contained within this one,
    #remove it
    existing_clusters = clusters.keys()
    
    for existing in existing_clusters:
        superceded = True
        
        for e in existing:
            if e not in cluster:
                superceded = False
                break
            #end
        #end
        
        if superceded:
            del clusters[existing]
        #end
        
    #end
    
    clusters[cluster] = True
    
#end

#given all of the clusters of minimum size 3, try to expand
#only want to output proper clusters, meaning no cluster
#that is part of a larger cluster
#
#
def expand_clusters():
    
    existing_clusters = clusters.keys()
    for cluster in existing_clusters:
        cluster_elements = list(cluster)
        while True:
            prospective_members = {}
            
            #each cluster member will add each adjacent
            #user to prospective_members.
            #any user that had been added len(cluster_element) times
            #is paired to every cluster member 
            for user in cluster_elements:
                for adj in pair_list[user]:
                
                    #avoid duplicates when expanding as well by only considering
                    #lexically greater users
                    if adj < user:
                        continue
                    #end
                
                    if not adj in prospective_members:
                        prospective_members[adj] = 1
                    else:
                        prospective_members[adj] += 1    
                    #end
                #end
            #end
        
            added = False
            member_count = len(cluster_elements)
            for prospective,count in prospective_members.iteritems():
                if count == member_count:
                    cluster_elements.append(prospective)
                    added = True
                #end
            #end

            if not added:
                break
            #end
        #end
        
        add_cluster(tuple(cluster_elements))
        
    #end
#end

def build_cluster_strings():
    cluster_strings = []
    #sort elements within a cluster lexically and append ', ' separator
    #then sort the list of cluster strings
    
    for cluster in clusters:
        cluster_elems = list(cluster)
        cluster_elems.sort()
        cluster_addresses = [user + '@facebook.com' for user in cluster_elems]
        cluster_line = string.join(cluster_addresses, ', ')
        cluster_strings.append(cluster_line)
    #end
    
    cluster_strings.sort()
    
    return cluster_strings
    
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')

    for line in fin:
    
        emails = re.finditer(r' (\S+)@facebook\.com\s+(\S+)@facebook', line)
        
        for email in emails:
            id1, id2 = email.group(1),email.group(2)
            add_interaction(id1,id2)
        #end        
    #end
    
    process_pairs()    
    build_clusters()
    expand_clusters()
    
    for line in build_cluster_strings():
        print(line)
    #end
    
#end
