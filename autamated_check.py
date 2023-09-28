import time
import pywhatkit as p
def get_valid_phone_number():
    while True:
        phone_number = input("Enter phone number with country code (e.g., +1234567890): ")
        if phone_number.startswith('+'):
            return phone_number
        else:
            print("Please enter a valid phone number with a country code.")
def send_whatsapp_message(phone_number, message):
    try:
        p.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            wait_time=15,
            tab_close=True,
            close_time=5
        )
        print(f"Message to {phone_number} sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")
if __name__ == "__main__":
    phone_number = get_valid_phone_number()
    while True:
        send_whatsapp_message(phone_number, "how is going on")

        time.sleep(30)
