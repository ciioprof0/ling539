#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module Docstring:
This script divides a dataset into training and testing subsets with CLI argument parsing
and dynamically generates filenames for output.
"""

# Import Standard Library Modules
import sys  # Used for handling exceptions
import os   # Used for file and path operations
import argparse  # Used for parsing command line arguments

# Import Third-Party Modules
import pandas as pd  # Used for data manipulation and analysis
# pip install pandas

# Define Classes
class DatasetSplitter:
    """
    This class handles the splitting of a dataset into training and testing subsets.
    """

    def __init__(self, filepath, train_size=0.7, seed=42):
        """
        Initialize the DatasetSplitter.

        :param filepath: str, the path to the dataset file.
        :param train_size: float, the proportion of the dataset to include in the train split.
        :param seed: int, the seed for the random number generator.
        """
        self.filepath = filepath
        self.train_size = train_size
        self.seed = seed

    def load_dataset(self):
        """
        Load the dataset from the given file path.

        :return: DataFrame, the loaded dataset.
        """
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f"No file found at {self.filepath}")

        return pd.read_csv(self.filepath)

    def split_dataset(self):
        """
        Split the dataset into training and testing sets.

        :return: tuple(DataFrame, DataFrame), the training and testing sets.
        """
        dataset = self.load_dataset()
        return dataset.sample(frac=self.train_size, random_state=self.seed), dataset.drop(dataset.sample(frac=self.train_size, random_state=self.seed).index)

    def save_splits(self, train_set, test_set):
        """
        Save the training and testing sets to dynamically generated CSV files.

        :param train_set: DataFrame, the training set.
        :param test_set: DataFrame, the testing set.
        """
        base_name, _ = os.path.splitext(self.filepath)
        train_filename = f"{base_name}_train.csv"
        test_filename = f"{base_name}_test.csv"

        train_set.to_csv(train_filename, index=False)
        test_set.to_csv(test_filename, index=False)
        return os.path.dirname(os.path.abspath(train_filename))


# Define Functions
def parse_arguments():
    """
    Parse command line arguments.

    :return: Namespace, the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Split a dataset into training and testing sets.")
    parser.add_argument("filepath", type=str, default='News.csv', help="Path to the dataset file.")
    parser.add_argument("--train_size", type=float, default=0.7, help="Proportion of the dataset to include in the train split (default: 0.7).")
    parser.add_argument("--seed", type=int, default=42, help="Seed for the random number generator (default: 42).")
    return parser.parse_args()


def main():
    # Parse command line arguments
    args = parse_arguments()

    # Define Script Classes
    splitter = DatasetSplitter(args.filepath, args.train_size, args.seed)

    # Split the dataset and save the splits
    try:
        train_set, test_set = splitter.split_dataset()
        split_path = splitter.save_splits(train_set, test_set)
        print("The dataset has been successfully split and saved to:")
        print(f"    {split_path}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    # End of script message
    print("Script completed successfully.")

if __name__ == "__main__":
    main()
