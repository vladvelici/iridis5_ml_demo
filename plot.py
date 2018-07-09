import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


def find_runs(root):
    results = []
    for (dirpath, dirnames, filenames) in os.walk(root, topdown=True, followlinks=True):
        if "meta.json" in filenames:
            results.append(dirpath)

    return results

def get_runs(args):
    lr_acc = []

    paths = find_runs(args.path)

    for p in paths:
        meta_path = os.path.join(p, "meta.json")
        with open(meta_path, "r") as f:
            meta = json.load(f)
        lr = meta["lr"]

        df = pd.read_csv(os.path.join(p, "log.csv"))
        test_acc = max(df['test_acc'])
        lr_acc += [lr,test_acc]
    return np.asarray(lr_acc)

def main(args):


    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="+", type=str, help="paths to use for plots")

    args = parser.parse_args()
    results = get_runs(args)
    plt.figure()
    plt.scatter(results[:,0],results[:,1])
    plt.savefig(os.path.join(args.path, "lr_test_acc.png"))
