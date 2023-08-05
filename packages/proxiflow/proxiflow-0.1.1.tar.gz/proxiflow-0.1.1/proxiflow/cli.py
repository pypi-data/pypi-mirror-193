import click
import polars as pl

from .config import Config
from .utils.logger import get_logger
from .core import DataFlow


def load_data(data_file: str) -> pl.DataFrame:
    """
    Load a CSV file and return a polars DataFrame.

    Parameters:
    data_file (str): The path to the CSV file to load.

    Returns:
    pl.DataFrame: The DataFrame containing the CSV data.

    Raises:
    FileNotFoundError: If the specified file path does not exist.
    ValueError: If the specified file is empty or cannot be parsed as a CSV file.
    """
    try:
        # Attempt to load the CSV file
        df = pl.read_csv(data_file)
        if df.shape[0] == 0:
            raise ValueError("Data file is empty")
        return df
    except FileNotFoundError:
        # If the file is not found, raise a FileNotFoundError
        raise FileNotFoundError("Data file not found")
    except Exception as e:
        # If there is an error loading the CSV file, raise a ValueError with the error message
        raise ValueError(f"Error loading data file: {str(e)}")


# Data writer
def write_data(data: pl.DataFrame, output_file: str) -> None:
    """
    Writes a given DataFrame to a CSV file.

    Parameters:
    data (pl.DataFrame): The DataFrame to be written.
    output_file (str): The file path to save the data.

    Raises:
    Exception: If there is an error while writing the data.
    """
    try:
        data.write_csv(output_file, sep=",")
    except Exception as e:
        raise Exception(f"Error writing data to {output_file}: {str(e)}")


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.option(
    "--config-file",
    "-c",
    required=True,
    type=click.Path(exists=True),
    help="Path to configuration file",
)
@click.option(
    "--input-file",
    "-i",
    required=True,
    type=click.Path(exists=True),
    help="Path to input data file",
)
@click.option(
    "--output-file",
    "-o",
    required=True,
    type=click.Path(exists=False),
    help="Path to output data file",
)
@click.pass_context
@click.version_option()
def main(ctx, config_file, input_file, output_file):
    # Set up logger
    logger = get_logger(__name__)

    # Load configuration
    config = Config(config_file)

    # Load data
    try:
        data = load_data(input_file)
    except FileNotFoundError as e:
        logger.error("Input file not found: %s", str(e))
    except ValueError as e:
        logger.error("Error parsing input file: %s", str(e))

    # Instantiate preprocessor
    flow = DataFlow(config)

    # Perform data cleaning
    try:
        cleaned_data = flow.clean_data(data)
    except ValueError as e:
        logger.error("Error cleaning data: %s", str(e))
        return

    # TODO: Add data normalization and feature engineering
    # # Perform data normalization

    # # Perform feature engineering

    try:
        write_data(cleaned_data, output_file)
    except Exception as e:
        logger.error(f"Error writing data to file {output_file}: {str(e)}")

    # Log completion message
    logger.info("Data preprocessing complete.")


if __name__ == "__main__":
    main()
