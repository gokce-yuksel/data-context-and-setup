from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """

        # Path to csv directory
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()

        # List all csv files
        file_paths = list(csv_path.iterdir())

        # Extract file names
        file_names = [p.name for p in file_paths]

        # Clean file names to create dictionary keys
        key_names = [
            name
            .replace("olist_", "")
            .replace("_dataset.csv", "")
            .replace(".csv", "")
            for name in file_names
        ]

        # Build data dictionary
        data = {}
        for key, path in zip(key_names, file_paths):
            data[key] = pd.read_csv(path)

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
