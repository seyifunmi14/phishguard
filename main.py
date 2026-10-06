def main():
    print("PhishGuard")
    print("Phishing Email Detection System\n")

    sender = input("Sender: ")
    subject = input("Subject: ")
    body = input("Email body: ")

    print("\n=== Email Received ===")
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

if __name__ == "__main__":
    main()
    