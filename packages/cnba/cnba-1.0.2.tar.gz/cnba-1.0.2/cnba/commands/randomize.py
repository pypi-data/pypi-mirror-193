import pandas as pd
import os
from collections import Counter
import itertools
import random
import tqdm
import statistics as stat
from . import helper as hp
from console_logging.console import Console
console = Console()


# @click.option("--parallelize", "-p", is_flag=True, default=False, help="Utilize multithreading.")
# @click.command()
# @click.option("--input", "-i", required=True, type=str, help="Location of cleaned data saved after initialization.")
# @click.option("--steps", "-s", required=True, type=int, default=10000, help="How many iterations of network randomization to perform.")
def randomize(input, steps):
    
    # console.log("\n================ RANDOMIZATION ===============\n")
    # console.info("Loading network data...")
    cleaned = pd.read_csv(os.path.join(input, "cleaned.csv"))
    syn = list(cleaned.syn.unique())
    targets = list(cleaned.target.unique())
    all_syn_pairs = list(itertools.combinations(syn, 2))
    tar_per_syn = cleaned.syn.value_counts().to_dict()

    randomization_success={}
    randomized_target_count_sum={}
    c = len(syn)
    for i in range(c):
        syn1 = syn[i]
        for j in range(i+1, c):
            syn2 = syn[j]
            key = "~~".join([syn1, syn2])
            randomization_success[key] = 0
            randomized_target_count_sum[key] = 0

    # console.info("Starting network randomization...")
    # for i in tqdm.trange(1, steps+1, desc='Randomization step: '):
    for i in tqdm.trange(steps):
        shuffled_targets = get_shuffled_targets(syn, tar_per_syn, targets)
        for pair in all_syn_pairs:
            syn1, syn2 = pair[0], pair[1]
            key = "~~".join([syn1, syn2])
            syn1_t = shuffled_targets[syn1]
            syn2_t = shuffled_targets[syn2]
            intersection = hp.xintersection_length(syn1_t, syn2_t)

            if intersection < 1:
                continue
            randomization_success[key]+=1
            randomized_target_count_sum[key]+=intersection

    # console.success("Finished network randomization "+ str(steps)+" times.")
    
    return [randomization_success, randomized_target_count_sum]
    save_syNet([randomization_success, randomized_target_count_sum], shared_target_count, input)


def save_syNet(result, output, parallelize):

    stc = {}
    stc = hp.load_pickle(os.path.join(output, "shared_target_count.p"))
    
    syNet = []

    all_success = Counter()
    all_count = Counter()

    if parallelize:
        for res in result:
            all_success += Counter(res[0])
            all_count += Counter(res[1])
    else:
        all_success = Counter(result[0])
        all_count = Counter(result[1])
    
    success = dict(all_success)
    count = dict(all_count)
    avg_shared_target_count = {}
    cc_val = {}

    for syn_pair, c in count.items():
        if success[syn_pair] > 0:
            avg_shared_target_count[syn_pair] = c / success[syn_pair]
        else:
            avg_shared_target_count[syn_pair] = 0

    for syn_pair in avg_shared_target_count.keys():
        if avg_shared_target_count[syn_pair] > 0:
            CC = stc[syn_pair] / avg_shared_target_count[syn_pair]
        else:
            CC = 0

        if CC > 0:
            cc_val[syn_pair] = CC

    shared_targetcount = [v for (k, v) in stc.items() if v > 0]
    threshold = stat.median(sorted(shared_targetcount))
    filtered = [pair for pair, count in stc.items() if count >= threshold]
    cc_filtered = [pair for pair, cc in cc_val.items() if cc > 1]
    merged = hp.xintersection(filtered, cc_filtered)
    merged = list(merged)

    for pair in merged:
        s1, s2 = pair.split('~~')
        syNet.append([s1, s2, cc_val[pair], stc[pair]])
    
    res = pd.DataFrame(syNet, columns=['syn_term1', 'syn_term2', 'cc_value', 'shared_target_count'])

    # Cleaning up
    for item in output:
        if item.endswith(".p"):
            os.remove(os.path.join(output, item))

    res.sort_values(by='cc_value', ascending=False, inplace=True)
    save = os.path.join(output, 'syNet.csv')
    res.to_csv(save, index=False)
    console.success("syNet saved to: "+save)


def get_shuffled_targets(all_syn, targets_per_syn, all_targets):
    shuffled_targets={}
    for syn in all_syn:
        tar_count = targets_per_syn[syn]
        temp = random.sample(all_targets, tar_count)
        shuffled_targets[syn]=temp

    return shuffled_targets