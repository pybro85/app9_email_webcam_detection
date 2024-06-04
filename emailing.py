import smtplib
from PIL import Image
from io import BytesIO
from email.message import EmailMessage


PASSWORD = "uwhrgphvoolotwkm"
SENDER = "kartalcarriers@gmail.com"
RECEIVER = "kartalcarriers@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New object showed up!"
    email_message.set_content("Hey, we've just detected a new object entering the area")
    
    with open(image_path, "rb") as file:
        content = file.read()
        image_data = BytesIO(content)
        image = Image.open(image_data)
        image_format = image.format
        # print("Image format:", image_format)
        
    email_message.add_attachment(content, maintype="image", subtype=image_format)
    
    gmail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # gmail.ehlo()
    # gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")
    
if __name__ == "__main__":
    send_email(image_path = "images/19.png")