# ------------------------------------------
# Imports
# ------------------------------------------
import os
import json
from datetime import datetime as dt
import logging
logger = logging.getLogger(__name__)


class Ingestion:
    """
    Class for handling the ingestion process.

    Args:
        None

    Attributes:
        * start_time (datetime): The start time of the ingestion process.
        * end_time (datetime): The end time of the ingestion process.
        * model (object): The model object.
        * train_data (dict): The train data dict.
        * test_data (dict): The test data dict.
    """

    def __init__(self):
        """
        Initialize the Ingestion class.

        """
        self.start_time = None
        self.end_time = None
        self.model = None
        self.train_data = None
        self.test_data = None

    def start_timer(self):
        """
        Start the timer for the ingestion process.
        """
        self.start_time = dt.now()

    def stop_timer(self):
        """
        Stop the timer for the ingestion process.
        """
        self.end_time = dt.now()

    def get_duration(self):
        """
        Get the duration of the ingestion process.

        Returns:
            timedelta: The duration of the ingestion process.
        """
        if self.start_time is None:
            logger.warning("Timer was never started. Returning None")
            return None

        if self.end_time is None:
            logger.warning("Timer was never stopped. Returning None")
            return None

        return self.end_time - self.start_time

    def save_duration(self, output_dir=None):
        """
        Save the duration of the ingestion process to a file.

        Args:
            output_dir (str): The output directory to save the duration file.
        """
        duration = self.get_duration()
        duration_in_mins = int(duration.total_seconds() / 60)
        duration_file = os.path.join(output_dir, "ingestion_duration.json")
        if duration is not None:
            with open(duration_file, "w") as f:
                f.write(json.dumps({"ingestion_duration": duration_in_mins}, indent=4))

    def load_train_data(self):
        """
        Load the training data.

        """
        logger.info("Loading Train data")
        self.train_data = None  # TODO: replace by actual data loading logic

    def load_test_data(self):
        """
        Load the test data.

        """
        logger.info("Loading Test data")
        self.test_data = None  # TODO: replace by actual data loading logic

    def init_submission(self, Model):
        """
        Initialize the submitted model.

        Args:
            Model (object): The model class.
        """
        logger.info("Initializing Submmited Model")

        self.model = Model()

    def fit_submission(self):
        """
        Fit the submitted model.
        """
        logger.info("Fitting Submmited Model")
        self.model.fit(self.train_data)

    def predict_submission(self):
        """
        Make predictions using the submitted model.
        """
        logger.info("Calling predict method of submitted model")
        self.predictions = self.model.predict(self.test_data)

    def compute_result(self):
        """
        Compute the ingestion result.
        """
        logger.info("Computing Ingestion Result")

        self.ingestion_result = {
            "predictions": self.predictions
        }

    def save_result(self, output_dir=None):
        """
        Save the ingestion result to files.

        Args:
            output_dir (str): The output directory to save the result files.
        """
        result_file = os.path.join(output_dir, "ingestion_result.json")
        with open(result_file, "w") as f:
            f.write(json.dumps(self.ingestion_result, indent=4))
