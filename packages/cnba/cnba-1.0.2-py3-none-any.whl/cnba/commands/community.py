import os
import sys
import pandas as pd
from tqdm.auto import tqdm
from collections import defaultdict
from console_logging.console import Console
console = Console()
from pprint import pprint

# @click.command()
# @click.option("--input", "-i", required=True, help="Location of annotated data")
# @click.argument("cutoff", required=False, type=float, default=0.2)
def community(input, cutoff):

    console.log("\n================ CLUSTERING ===============\n")
    modules = []
    cutoff = 1-cutoff
    edges = defaultdict(set)
    annotation = pd.read_csv(os.path.join(input, "syNet_annotation.csv"))
    annotationx = annotation.copy()
    annotationx = annotationx[['syn_term1','syn_term2']]
    annotationx.drop_duplicates(inplace=True)

    for a, b in zip(annotationx.syn_term1, annotationx.syn_term2):
        edges[a].add(b)
        edges[b].add(a)

    weights = dict((v,1.) for v in edges)
    for i,v in tqdm(enumerate(edges), total=len(edges), desc="Detecting clusters: "):
        if i % 1000 == 0: pass
        neighborhood = set((v,)) | edges[v]
        
        if len(neighborhood) <= 2: continue
        k = 2 
        while neighborhood:
            k_core = neighborhood.copy()
            invalid_nodes = True
            while invalid_nodes and neighborhood:
                invalid_nodes = set(n for n in neighborhood if len(edges[n] & neighborhood) <= k)
                neighborhood -= invalid_nodes
            k += 1 
        weights[v] = (k-1) * (sum(len(edges[n] & k_core) for n in k_core) / (2. * len(k_core)**2))

    unvisited = set(edges)
    num_clusters = 0
    for seed in sorted(weights, key=weights.get, reverse=True):
        if seed not in unvisited: continue

        cluster, frontier = set((seed,)), set((seed,))
        w = weights[seed] * cutoff
        while frontier:
            cluster.update(frontier)
            unvisited -= frontier
            frontier = set(n for n in set.union(*(edges[n] for n in frontier)) & unvisited if weights[n] > w)

        invalid_nodes = True
        while invalid_nodes and cluster:
            invalid_nodes = set(n for n in cluster if len(edges[n] & cluster) < 2)
            cluster -= invalid_nodes
        
        if cluster:        
            num_clusters += 1
            for c in cluster:
                modules.append([c, num_clusters])
    
    data = pd.DataFrame(modules, columns=['term', 'module'])
    data.to_csv(os.path.join(input, 'community_modules.csv'), index=False)
    x = annotation[(annotation.syn_term1.isin(data.term)) & (annotation.syn_term2.isin(data.term))]
    x = x[['syn_term1', 'syn_term2']]
    x.drop_duplicates(inplace=True)
    x.to_csv(os.path.join(input, 'community_syn_terms_for_cytoscape.csv'), index=False)
    
    
    modx = []
    mapper=defaultdict(list)
    for m, t in zip(data.module, data.term):
        mapper[m].append(t)
        
    # print(mapper)
    for mod, terms in mapper.items():
        for s1, s2, a, t, pv, pj in zip(annotation.syn_term1, annotation.syn_term2, annotation.annotation, annotation.targets, annotation.pvalue, annotation.padjusted):
            if s1 in terms and s2 in terms:
                modx.append([s1, s2, a, t, pv, pj, mod])
    #data.columns=['syn_term1', 'module']
    #merged = pd.merge(annotation, data, on='syn_term1', how='left')
    #merged.fillna(99999999999999)
    #merged.sort_values(by=['module'], ascending=True)
    modx = pd.DataFrame(modx, columns=['syn_term1','syn_term2', 'annotation','targets', 'pvalue','padjusted','module'])
    modx.to_csv(os.path.join(input, 'modified_community_module_annotation.csv'), index=False)
    #merged.to_csv(os.path.join(input, 'community_module_annotation.csv'), index=False)
    
if __name__=="__main__":
    community(sys.argv[1], 0.2)