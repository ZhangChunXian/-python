from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What lanuage did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\n Thank you to everyone who participated in the survey!")
my_survey.show_results()

# Testing the AnonymousSurvey Class
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    # Tests for the class AnonymousSurvey
    def test_store_single_response(self):
        # Test that a single response is stored properly
        question = "What lanuage did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertEqual(['English'], my_survey.responses)

if __name__ == '__main__':
    unittest.main()