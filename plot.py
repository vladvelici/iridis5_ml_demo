import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

import os
import sys
import json
import numpy as np

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
        test_acc = max(df[' test acc'])
        lr_acc += [[lr,test_acc]]
    return np.asarray(lr_acc)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="paths to use for plots")

    args = parser.parse_args()
    results = get_runs(args)
    plt.figure()
    plt.scatter(results[:,0],results[:,1])
    print("got  here")
    plt.savefig(os.path.join(args.path, "lr_test_acc.png"))

if __name__ == "__main__":
    main()
