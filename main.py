# Function to detect urgency-related words and phrases in email text
def detect_urgency(text):
    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "suspended",
        "verify now",
        "within 24 hours"
    ]
    text = text.lower()
    detected_words = []

    for word in urgency_words:
        if word in text:
            detected_words.append(word)
    
    return detected_words

def detect_credentials(text):
    credentials_words = [
        "password",
        "credit card",
        "pin",
        "login credentials",
        "verify your account",
        "update payment"
    ]
    text = text.lower()
    detected_words = []

    for word in credentials_words:
        if word in text:
            detected_words.append(word)
    return detected_words

def calculate_risk_score(urgency_results, credentials_results):
    urgency_findings = len(urgency_results)
    credentials_findings = len(credentials_results)
    
    risk_score = (urgency_findings * 10) + (credentials_findings * 20)
    
    if risk_score > 100:
        risk_score = 100

    return risk_score

def classify_risk(risk_score):
        if risk_score  < 30:
            return "LOW"
        elif risk_score < 60:
            return "MEDIUM"
        else:
            return "HIGH"

def check_sender(sender):
    parts = sender.split("@")
    
    if len(parts) != 2:
        return False

    username = parts[0]
    domain = parts[1]

    if username == "":
        return False
    
    if domain == "":
        return False
    
    if "." not in domain:
        return False
    
    domain_parts = domain.split(".")
    if domain_parts[0] == "" or domain_parts[-1] == "":
        return False

    return True

    
def main():
    print("PhishGuard")
    print("Phishing Email Detection System\n")

    sender = input("Sender: ")
    subject = input("Subject: ")
    body = input("Email body: ")
    
    email_text = subject + " " + body

    urgency_results = detect_urgency(email_text)
    credentials_results = detect_credentials(email_text)

    result = calculate_risk_score(urgency_results,credentials_results)

    risk_level = classify_risk(result)

    sender_valid = check_sender(sender)

    print("\n=== Email Received ===")
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")


    print("\n=== PhishGuard Analysis ===")
    print(f"Sender format valid: {sender_valid}")
    print(f"Urgency indicators: {urgency_results}")
    print(f"Credentials indicators: {credentials_results}")
    print(f"Risk Score: {result}")
    print(f"Risk Level: {risk_level}")

   



if __name__ == "__main__":
    main()


