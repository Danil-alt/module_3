def send_email(message, recipient, sender="university.help@gmail.com"):

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    elif "@" not in recipient or not (recipient.endswith('.com') or recipient.endswith('.net') or recipient.endswith('.ru')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это должно быть сделано еще вчера', "university.help@gmail.com")
send_email("Памагите", "qwert@fnfn")
send_email("Памагите", "qwert@.com")
send_email("Памагите", "university.help@gmail.com", "qwert@.net")