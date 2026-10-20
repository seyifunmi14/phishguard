import unittest

from main import (
    check_sender, 
    calculate_risk_score,
    classify_risk,
    detect_urgency,
    detect_credentials
)

class TestSenderValidation(unittest.TestCase):
    def test_valid_sender(self):
        self.assertTrue(check_sender("security@gmail.com"))
        
    def test_invalid_sender(self):
        self.assertFalse(check_sender("securitygmail.com"))

class TestRiskScoring(unittest.TestCase):
    def test_no_indicators(self):
        score = calculate_risk_score([],[])
        self.assertEqual(score, 0)

    def test_urgency_only(self):
        urgency = ["urgent", "immediately"]
        score = calculate_risk_score(urgency, [])
        self.assertEqual(score,20)
    
    def test_credentials_only(self):
        credentials = ["password", "credit card"]
        score = calculate_risk_score([], credentials)
        self.assertEqual(score,40)

    def test_maximum_score(self):
        urgency = ["urgent", "immediately", "act now", "suspended"]
        credentials = ["password", "credit card", "pin", "login credentials"]
        score = calculate_risk_score(urgency, credentials)
        self.assertEqual(score, 100)

class TestRiskClassification(unittest.TestCase):
    def test_low_risk(self):
        result = classify_risk(10)
        self.assertEqual(result, "LOW")

    def test_medium_risk(self):
        result = classify_risk(40)
        self.assertEqual(result, "MEDIUM")
    
    def test_high_risk(self):
        result = classify_risk(80)
        self.assertEqual(result, "HIGH")

    def test_low_medium_boundary(self):
        self.assertEqual(classify_risk(29), "LOW")
        self.assertEqual(classify_risk(30), "MEDIUM")
    
    def test_medium_high_boundary(self):
        self.assertEqual(classify_risk(59), "MEDIUM")
        self.assertEqual(classify_risk(60), "HIGH")

class TestUrgencyDetection(unittest.TestCase):
    def test_urgent_email(self):
        text = "Please act now"
        result = detect_urgency(text)
        self.assertEqual(result, ["act now"])
    
    def test_no_urgency(self):
        text = "Hello, I hope you are having a good day."
        result = detect_urgency(text)
        self.assertEqual(result, [])
    
    def test_no_partial_word_match(self):
        text = "Please respond urgently."
        result = detect_urgency(text)
        self.assertEqual(result, [])

class TestCredentialDetection(unittest.TestCase):
    def test_password_detection(self):
        text = "Please enter your password"
        result = detect_credentials(text)
        self.assertEqual(result, ["password"])
    
    def test_no_credentials(self):
        text = "Hello, your package has arrived."
        result = detect_credentials(text)
        self.assertEqual(result, [])
    
    def test_uppercase_password(self):
        text = "Please enter your PASSWORD"
        result = detect_credentials(text)
        self.assertEqual(result, ["password"])
    
    def test_no_false_positive_for_pin(self):
        text = "I am going shopping tomorrow."
        result = detect_credentials(text)
        self.assertEqual(result,[])


