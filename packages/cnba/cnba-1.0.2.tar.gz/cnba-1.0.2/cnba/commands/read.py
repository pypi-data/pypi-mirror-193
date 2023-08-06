import os
from . import helper as hp
import pandas as pd
from console_logging.console import Console
console = Console()

#@click.command()
#@click.option("--primary", "-p", required=True, type=click.File(), help="Location of the file containing the primary bipartite network data.")
#@click.option("--output-dir", "-o", required=True, type=str, help="Location where all preliminary stats and cleaned data will be saved.")
def read(primary, output_dir):
    
    console.log("\n==================== INIT ====================\n")
    console.info("Reading primary input data...")
    output = output_dir
    data = pd.read_csv(primary, sep='\t', header=None)
    console.info("Cleaning data...")
    data.columns = ["syn", "target"]
    data.syn = data.syn.str.lower()
    data.target = data.target.str.lower()
    data.drop_duplicates(inplace=True)
    save = os.path.join(output, "cleaned.csv")
    data.to_csv(save, index=False)
    console.success("Saved cleaned data to: "+save)
    
    console.log("\n============== PRELIMINARY-STATS =============\n")
    console.info("Extracting frequency distributions...")
    stdd = data.groupby('syn')['target'].apply(list).to_dict()
    tsdd = data.groupby('target')['syn'].apply(list).to_dict()
    hp.dict2disk(stdd, os.path.join(output, 'syn_target_degree_distribution.csv'), ['syn', 'target_count', 'target_list'])
    hp.dict2disk(tsdd, os.path.join(output, 'target_syn_degree_distribution.csv'), ['target', 'syn_count', 'syn_list'])
    all_syn = list(data.syn.unique())
    shared_target_count = {}
    shared_targets = {}
    for i in range(len(all_syn)):
        s1 = all_syn[i]
        for j in range(i+1, len(all_syn)):
            s2 = all_syn[j]
            key = '~~'.join([s1, s2])
            shared_target_count[key]=hp.xintersection_length(stdd[s1], stdd[s2])
            shared_targets[key]=hp.xintersection(stdd[s1], stdd[s2])

    hp.save_pickle(os.path.join(output, 'shared_target_count.p'), shared_target_count)
    hp.save_pickle(os.path.join(output, 'shared_targets.p'), shared_targets)


    shared = []
    for pair, t in shared_targets.items():
        temp = " ".join(t)
        temp_ = pair.split('~~')
        shared.append([temp_[0], temp_[1], len(t), temp])
    
    dx = pd.DataFrame(shared)
    dx.columns = ['pair1', 'pair2', 'shared_target_count', 'shared_target_list']
    save = os.path.join(output, 'shared_targets_per_syn_pair.csv')
    dx.to_csv(save, index=False)
    console.success("Stats saved to: " + save)