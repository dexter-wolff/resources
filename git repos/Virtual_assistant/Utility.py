from Credentials import UserInfo
import smtplib
from gtts import gTTS
import time
import os
import requests
from bs4 import BeautifulSoup

class Input():
    def speak(text):
        tts = gTTS(text)
        filename = "sample.mp3"
        path = "Virtual_assistant\sample.mp3"
        tts.save(filename)
        os.system(filename)

    def listen():
        pass
class Email():

    EmailAddress = UserInfo.credentials["EmailAddress"]

    def send_email(self, to, content):
        EmailAddress = UserInfo.EmailAddress
        EmailPassword = UserInfo.EmailPassword
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        print("verifying")
        server.login( EmailAddress, EmailPassword)
        ReceiverAddrress = input("Who to send: ")
        server.sendmail(ReceiverAddrress, to, content)
        print("Done!")
        server.close()
class WebScraping():
    def WebScraper(url):
        r = requests.get(url)
        htmlContent = r.content

        soup = BeautifulSoup(htmlContent, 'html.parser') # parse the HTML
        
        paras = soup.find_all('p')


        print(paras)

        anchors = soup.find_all('a')
        all_links = set()

        print(all_links)

        for link in anchors:
            if(link.get('href') != '#'): 
                linkText = "https://codewithharry.com" +link.get('href')
                all_links.add(link)

        



