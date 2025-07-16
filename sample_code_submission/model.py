# ------------------------------
# Dummy Model Submission
# This is a dummy model for the participants to understand the structure of the code i.e.
# - required functions in the Model class
# - inputs and outputs of the functions
# ------------------------------

import numpy as np


class Model:
    """
    This is a model class to be submitted by the participants in their submission.

    This class should consists of the following functions
    1) init:
        takes no arguments

    2) fit:
        takes 1 argument: train_data. It can be used for intiializing variables, classifier etc.
        can be used to train a classifier
    3) predict:
        takes 1 argument: test_data
        can be used to get predictions of the test set.
        returns a dictionary

    Note:   Add more methods if needed e.g. save model, load pre-trained model etc.
            It is the participant's responsibility to make sure that the submission 
            class is named "Model" and that its constructor arguments remains the same.
            The ingestion program initializes the Model class and calls fit and predict methods

            When you add another file with the submission model e.g. a trained model to be loaded and used,
            load it in the following way:

            # get to the model directory (your submission directory)
            model_dir = os.path.dirname(os.path.abspath(__file__))

            your trained model file is now in model_dir, you can load it from here
    """

    def __init__(self):
        """
        Model class constructor

        Params:
            None

        Returns:
            None

        """
        pass

    def fit(self, train_data=None):
        """
        Params:
            train_data:
                A dictionary with data, labels

        Functionality:
            This function can be used to train a model. You can ignore this function if you already have a pre-trained model.

        Returns:
            None
        """

        # To access train data and labels use the following line of code
        # data = train_data["data"]
        # labels = train_data["labels"]
        pass

    def predict(self, test_data=None):
        """
        Params:
            test_data (dict): A dictionary containing the test data

        Functionality:
            this function can be used for predictions using the test sets

        Returns:
            a tupple of lists: (means list, errorbars list) 
            size of each list = (test_samples, 2) 

        """

        # To access test data use the following line of code
        # data = test_data["data"]

        num_test_data = 100
        means = np.random.uniform(low=0.0, high=10.0, size=(num_test_data, 2))
        errorbars = np.random.uniform(low=0.1, high=1.0, size=(num_test_data, 2))

        return (means, errorbars)
