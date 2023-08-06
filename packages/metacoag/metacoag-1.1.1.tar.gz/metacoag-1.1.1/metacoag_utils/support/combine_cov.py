#!/usr/bin/python3

"""combine_cov.py: Combine multiple coverage files of samples from CoverM.
"""

import argparse
import glob
import os
import subprocess

import pandas as pd

__author__ = "Vijini Mallawaarachchi"
__copyright__ = "Copyright 2020, MetaCoAG Project"
__license__ = "GPL-3.0"
__type__ = "Support Script"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "viji.mallawaarachchi@gmail.com"


def main():
    # Setup argument parser
    # -----------------------

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--covpath", required=True, help="path to the .tsv files from CoverM"
    )
    ap.add_argument(
        "--output", required=True, type=str, help="path to the output folder"
    )

    args = vars(ap.parse_args())
    covpath = args["covpath"]
    output_path = args["output"]

    # Validate inputs
    # ---------------------------------------------------

    # Handle for missing trailing forwardslash in output folder path
    if output_path[-1:] != "/":
        output_path = output_path + "/"

    # Create output folder if it does not exist
    if not os.path.isdir(output_path):
        subprocess.run("mkdir -p " + output_path, shell=True)

    # Get coverage values from samples
    # ---------------------------------------------------

    # Get coverage files
    cov_files = glob.glob(f"{covpath}/*.tsv")

    final_df = pd.DataFrame()

    for file in cov_files:
        df = pd.read_csv(file, sep="\t", header=0)

        if final_df.empty:
            final_df = df
        else:
            final_df = pd.concat(
                [final_df, df[list(df.columns)[1]]], axis=1, join="inner"
            )

    print(f"Dataframe shape: {final_df.shape}")

    # Save dataframe to file
    final_df.to_csv(output_path + "coverage.tsv", sep="\t", index=False, header=False)
    print(f"The combined coverage values can be found at {output_path}coverage.tsv")

    # Exit program
    # --------------

    print("Thank you for using combine_cov!")


if __name__ == "__main__":
    main()
