import os
import click
import configparser
import multiprocessing as mp
from tqdm.auto import tqdm
from concurrent.futures import ProcessPoolExecutor
from console_logging.console import Console
console = Console()
from . import read, randomize, annotate, community, helper


@click.command()
@click.argument("dir", type=str, default="cnba-default")
def create(dir):

    console.log("==================== CREATE ====================\n")
    
    project_dir = os.path.join(os.getcwd(), dir)
    os.makedirs(project_dir, exist_ok=True)
    result_dir = os.path.join(project_dir, "results")
    os.makedirs(result_dir, exist_ok=True)
    input_dir = os.path.join(project_dir, "input")
    os.makedirs(input_dir, exist_ok=True)

    
    configfile=os.path.join(os.getcwd(), "config.cnba")
    if not os.path.isfile(configfile):
        cfgfile = open(configfile, "w")

        config = configparser.ConfigParser()
        config.add_section("general")
        config.set("general", "project_dir", project_dir)
        config.set("general", "result_dir", result_dir)

        config.add_section("input")
        config.set("input", "primary", os.path.join(input_dir, "primary.txt"))
        with open(os.path.join(input_dir, "primary.txt"), "w") as f:
            for i in range(5):
                f.write("src-"+str(i)+"\t"+"target_"+str(i)+"\n")
        config.set("input", "annotation", os.path.join(input_dir, "annotation.txt"))
        with open(os.path.join(input_dir, "annotation.txt"), "w") as f:
            for i in range(5):
                f.write("target_"+str(i)+"\t"+"function-"+str(i)+"\n")
        config.set("input", "randomization_steps", "10000")
        config.set("input", "parallelize", "False")
        os.makedirs(input_dir, exist_ok=True) 

        config.add_section("annotation")
        config.set("annotation", "fdr_method", "fdr_bh")
        config.set("annotation", "fdr_cutoff", "0.05")

        config.add_section("clustering")
        config.set("clustering", "cutoff", "0.2")

        console.success("Initialized project: " + project_dir)

        console.info("Please modify the configuration file as per your requirements")
        console.info("Dummy data provided inside input folder will throw error if not updated...")
        console.info(">cnba run ⏎ \n")

        config.write(cfgfile)
        cfgfile.close()



@click.command()
@click.option("--primary", "-i", required=True, type=str, help="Path of primary bipartite file.")
@click.option("--annotation", "-a", required=False, type=str, help="Path of anotation file.")
@click.option("--steps", "-s", required=False, type=int, default=10000, help="How many iterations of network randomization to perform.")
@click.option("--fdr-method", "-m", required=False, default="fdr_bh", type=click.Choice(['fdr_bh', 'bonferroni', 'fdr_by']), help="Method of FDR correction to be followed?")
@click.option("--fdr-cutoff", "-c", required=False, type=float, default=0.05)
@click.option("--output-directory", "-o", type=str, default='cnba-output', help="Name of output directory")
@click.option("--parallelize", "-p", is_flag=True, default=False, help="Utilize multithreading.")
@click.option("--cluster-cutoff", "-x", required=False, type=float, default=0.2)
def run(primary, annotation, steps, fdr_method, fdr_cutoff, output_directory, parallelize, cluster_cutoff):

    #with open(os.path.join(os.getcwd(), 'config.cnba')) as f:
    #    sample_config = f.read()
    #    cfg = configparser.SafeConfigParser()
    #    cfg.read_string(sample_config)
    # console.info("Reading configration file...")
    # project_dir = cfg.get("general", "project_dir")
    # result_dir = cfg.get("general", "result_dir")
    # primary = cfg.get("input", "primary")
    # annotation = cfg.get("input", "annotation")
    # randomization_steps = int(cfg.get("input", "randomization_steps"))
    # parallelize = eval(cfg.get("input", "parallelize"))
    # fdr_method = cfg.get("annotation", "fdr_method")
    # fdr_cutoff = float(cfg.get("annotation", "fdr_cutoff"))
    # cluster_cutoff = float(cfg.get("clustering","cutoff"))

    result_dir = os.path.join(output_directory, "results")
    os.makedirs(result_dir, exist_ok=True)
    read.read(primary, result_dir)

    if parallelize:
        chunks = helper.split(steps, mp.cpu_count())
        randomization_args = []
        for chunk in chunks:
            randomization_args.append((result_dir, chunk))
        
        with ProcessPoolExecutor() as executor:
            presults = list(tqdm(executor.map(__randomize_wrapperr, randomization_args), total=len(chunks)))
    else:
        presults = randomize.randomize(result_dir, steps)
    
    console.info("Saving result to disk...")
    randomize.save_syNet(presults, result_dir, parallelize)


    # randomize.randomize(result_dir, randomization_steps, parallelize)
    annotate.annotate(annotation, result_dir, fdr_method, fdr_cutoff)
    community.community(result_dir, cluster_cutoff)

    console.info("Cleaning up...")
    files_in_directory = os.listdir(result_dir)
    filtered_files = [file for file in files_in_directory if file.endswith(".p")]
    for file in filtered_files:
        path_to_file = os.path.join(result_dir, file)
        os.remove(path_to_file)
    os.remove(os.path.join(result_dir,"cleaned.csv"))

    console.success("\n==================== FINISHED ====================\n")


def __randomize_wrapperr(args):
   return randomize.randomize(*args)