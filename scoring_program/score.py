# ------------------------------------------
# Imports
# ------------------------------------------
import os
import json
import random
import logging
from datetime import datetime as dt
logger = logging.getLogger(__name__)


class Scoring:
    """
    This class is used to compute the scores for the competition.

    Atributes:
        * start_time (datetime): The start time of the scoring process.
        * end_time (datetime): The end time of the scoring process.
        * reference_data (dict): The reference data.
        * ingestion_result (dict): The ingestion result.
        * ingestion_duration (float): The ingestion duration.
        * scores_dict (dict): The scores dictionary.
    """

    def __init__(self, name=""):
        # Initialize class variables
        self.start_time = None
        self.end_time = None
        self.reference_data = None
        self.ingestion_result = None
        self.ingestion_duration = None
        self.scores_dict = {}

    def start_timer(self):
        self.start_time = dt.now()

    def stop_timer(self):
        self.end_time = dt.now()

    def get_duration(self):
        if self.start_time is None:
            logger.warning("Timer was never started. Returning None")
            return None

        if self.end_time is None:
            logger.warning("Timer was never stoped. Returning None")
            return None

        return self.end_time - self.start_time

    def load_reference_data(self, reference_dir):
        """
        Load the reference data.

        Args:
            reference_dir (str): The reference data directory name.
        """
        logger.info("Reading reference data")
        self.reference_data = None  # TODO: replace with the actual data loading logic

    def load_ingestion_duration(self, predictions_dir):
        """
        Load the ingestion duration.

        Args:
            predictions_dir (str): The predictions directory name.
        """
        logger.info("Reading ingestion duration")

        ingestion_duration_file = os.path.join(predictions_dir, "ingestion_duration.json")
        with open(ingestion_duration_file) as f:
            self.ingestion_duration = json.load(f)["ingestion_duration"]

    def load_ingestion_result(self, predictions_dir):
        """
        Load the ingestion result.

        Args:
            predictions_dir (str): The predictions directory name.
        """
        logger.info("Reading ingestion result")

        ingestion_result_file = os.path.join(predictions_dir, "ingestion_result.json")
        with open(ingestion_result_file) as f:
            self.ingestion_result = json.load(f)

    def compute_scores(self):
        """
        Compute the scores for the competition.

        """
        def _accuracy(predictions, ground_truth):
            correct = sum(p == g for p, g in zip(predictions, ground_truth))
            return correct / len(ground_truth)

        logger.info("Computing scores")
        predictions = self.ingestion_result["predictions"]
        ground_truth = random.choices([0, 1], k=10)  # TODO: replace by the actual ground_truth

        # TODO: replace by actual score
        score = _accuracy(predictions, ground_truth)

        print("------------------")
        print(f"Accuracy Score: {score}")
        print("------------------")

        self.scores_dict = {
            "score": score
        }

    def write_scores(self, output_dir):

        logger.info("Writing scores")
        score_file = os.path.join(output_dir, "scores.json")
        with open(score_file, "w") as f_score:
            f_score.write(json.dumps(self.scores_dict, indent=4))
