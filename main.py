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

def main():
    print("PhishGuard")
    print("Phishing Email Detection System\n")

    sender = input("Sender: ")
    subject = input("Subject: ")
    body = input("Email body: ")
    
    email_text = subject + " " + body

    urgency_results = detect_urgency(email_text)
    credentials_results = detect_credentials(email_text)

    print("\n=== Email Received ===")
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

    print("\n=== PhishGuard Analysis ===")
    print(f"Urgency indicators: {urgency_results}")
    print(f"Credentials indicators: {credentials_results}")

if __name__ == "__main__":
    main()


