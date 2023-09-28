import pywhatkit as p

def get_valid_phone_number():
    while True:
        phone_number = input("Enter phone number with country code (e.g., +1234567890): ")
        if phone_number.startswith('+'):
            return phone_number
        else:
            print("Please enter a valid phone number with a country code.")


def send_whatsapp_message(phone_number, message, time_hour, time_min):
    try:
        p.sendwhatmsg(phone_no=phone_number, message=message, time_hour=time_hour, time_min=time_min, wait_time=15)
        print(f"Message to {phone_number} scheduled for {time_hour}:{time_min} sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")


if __name__ == "__main__":
    phone_number = get_valid_phone_number()
    send_whatsapp_message(phone_number, "gecen xeyre, men getdim yatmagha", 1, 12)
    send_whatsapp_message(phone_number, "sabahin xeyir, necesen", 4, 33)
