from typing import Optional
from googlesearch import search

class LearnBot:
    """
    LearnBot is a class that provides methods to google and save the question and answer as attributes of the instance.
    It also provides a method to get the training data for a given question.
    """

    def __init__(self):
        """
        Initialize LearnBot
        """
        self.question: Optional[str] = None
        self.answer: Optional[str] = None

    def query_api(self, question: str) -> str:
        """
        Query google with the given question.

        Args:
            question (str): The question to be queried.

        Returns:
            The response from the API.
        """
        try:
            result = search(question, num_results=1, lang='ru')
            return next(result, None)
        except Exception as e:
            print('Error occurred:', e)

    def save_question_and_answer(self, question: str, answer: str) -> None:
        """
        Save the question and answer as attributes of the LearnBot instance.

        Args:
            question (str): The question.
            answer (str): The answer.
        """
        self.question = question
        self.answer = answer

    def get_train_data(self, question: str) -> str:
        """
        Get the training data for the given question.

        Args:
            question (str): The question to get training data for.

        Returns:
            The answer to the question, or raises a ValueError if no answer is found.
        """
        response = self.query_api(question)
        first_result = self.parse_response(response)
        self.save_question_and_answer(question, first_result)
        if first_result:
            return first_result
        else:
            raise ValueError('Ответ не найден')

    def parse_response(self, response: str) -> str:
        """
        Parse the response from the API to extract the required information.

        Args:
            response (str): The response from the API.

        Returns:
            The required information from the API response.
        """
        # code to parse the response goes here