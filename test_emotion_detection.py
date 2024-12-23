import unittest
from EmotionDetection.emotion_detection import emotion_detector, predict_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Define the test cases - statement and emotion
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        # Go through each test case
        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement, expected_emotion=expected_emotion):
                detected_response = emotion_detector(statement)
                predicted_emotion = predict_emotion(detected_response)
                self.assertEqual(predicted_emotion["dominant_emotion"], expected_emotion)

if __name__ == "__main__":
    unittest.main()