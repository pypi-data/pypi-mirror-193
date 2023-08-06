import os
import pandas as pd
import tqdm
from scipy.stats import hypergeom
import statsmodels.stats.multitest as smm
from . import helper as hp
from console_logging.console import Console
console = Console()


# @click.command()
# @click.option("--annotation", "-a", required=True, type=click.File(), help="Location of annotation data.")
# @click.option("--input", "-i", required=True, type=str, help="Location of cleaned data saved after initialization.")
# @click.option("--fdr-method", "-f", required=True, default=["fdr_bh"], type=click.Choice(['fdr_bh', 'bonferroni', 'fdr_by']), help="Method of FDR correction to be followed?")
# @click.option("--cutoff", "-c", required=True, type=float, default=0.05)
def annotate(annotation, input, fdr_method, cutoff):

    console.log("\n================= ANNOTATION ================\n")
    console.info("Reading annotation data...")
    data = pd.read_csv(annotation, sep='\t', header=None)
    data.columns = ['target', 'function']
    data.target = [t.lower() for t in data.target]
    cleaned = pd.read_csv(os.path.join(input, "cleaned.csv"))
    all_targets = list(cleaned.target.unique())
    data = data[data.target.isin(all_targets)]
    data.drop_duplicates(inplace=True)
    # all_functions = list(data.function.unique())
    targets_per_function = data.groupby('function')['target'].apply(list).to_dict()
    shared_targets = {}
    shared_targets = hp.load_pickle(os.path.join(input, "shared_targets.p"))
    syNet_target_list = []
    syNet = pd.read_csv(os.path.join(input, "syNet.csv"))

    for pair in zip(syNet.syn_term1, syNet.syn_term2):
        for t in shared_targets["~~".join(pair)]:
            syNet_target_list.append(t)
    syNet_target_list = list(set(syNet_target_list))

    significant_functions = data[data.target.isin(all_targets)]['function'].tolist()
    significant_functions = list(set(significant_functions))
    annotation_target_list = []

    for f in significant_functions:
        tar = targets_per_function[f]
        for t in tar:
            annotation_target_list.append(t)
    annotation_target_list = list(set(annotation_target_list))

    target_syn_function_combined = syNet_target_list + annotation_target_list
    target_syn_function_combined = list(set(target_syn_function_combined))
    M = len(target_syn_function_combined)

    console.info("Performing enrichment analysis...")

    PVALS = []
    for pair in tqdm.tqdm(zip(syNet.syn_term1, syNet.syn_term2), desc="P-value extraction: ", total=len(syNet.syn_term1)):
        KEY = '~~'.join(pair)
        N = syNet[(syNet.syn_term1 == pair[0]) & (syNet.syn_term2 == pair[1])]['shared_target_count']
        N = int(N)
        targets_per_synpair = shared_targets[KEY]
        functions_shared_target_subset = data[data.target.isin(targets_per_synpair)]['function'].to_list()

        if len(functions_shared_target_subset) < 1:
            continue
        
        for func in functions_shared_target_subset:
            n = len(targets_per_function[func])
            x_ = hp.xintersection(targets_per_function[func], targets_per_synpair)
            x = len(x_)

            if (M-n) < N:
                continue
            if M < N:
                continue
            if n < x:
                continue

            Pv = hypergeom.cdf(x, M, n, N)
            s1, s2 = pair[0], pair[1]
            PVALS.append([s1, s2, func, ' '.join(x_), (1-Pv)])


    PVALS = pd.DataFrame(PVALS, columns=['syn_term1', 'syn_term2', 'annotation', 'targets', 'pvalue'])
    rejected, padjusted = smm.multipletests(PVALS.pvalue, alpha=cutoff, method=fdr_method)[:2]
    PVALS['padjusted'] = padjusted
    PVALS.sort_values(by=['padjusted'], ascending=True)
    save = os.path.join(input, 'syNet_annotation.csv')
    PVALS.to_csv(save, index=False)
    console.success("Enrichment results saved to: " + save)
