import streamlit as st
from dotenv import load_dotenv
import os

import smtplib
from email.message import EmailMessage
import ssl

# Load variables from .env file
load_dotenv()

decoder = os.getenv("key")
msg =  os.getenv("msg")
PASS_KEY = os.getenv("PASS_KEY")


def send_emails():
    password = PASS_KEY
    email_name = 'yourEmail@gmail.com'
    fromaddr = email_name
    context = ssl.create_default_context() # add security


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as s:
            # send your self an email
            s.login(fromaddr, password)
            toaddr = 'yourEmail@gmail.com'
            em = EmailMessage()
            em['From'] = fromaddr
            em['To'] = toaddr
            em['Subject'] = 'MSG decoded'
            em.set_content('SOMEONE CRACKED THE CODE')
            s.sendmail(fromaddr, 'yourEmail@gmail.com', em.as_string())
                
            s.quit()


st.set_page_config(page_title='NVM',
                            layout="centered",)

# your cypher for example in hex:
st.code("""74 68 69 73 20 69 73 20 61 20 63 79 70 68 65 72 20 69 6E 20 68 65 78""", language='python')

user = st.text_input('')

if st.button("Decode :)"):
    if user.lower() == decoder:
        st.markdown(msg)
        send_emails()
    else:
        st.error('wrong..')
