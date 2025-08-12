WhatsApp Bulk Message Automation
A Python-based tool to send personalized or bulk WhatsApp messages via WhatsApp Web.
Reads contact information from an Excel sheet and message text from a file, then automates the sending process using pyautogui and keyboard.

✨ Features
Send messages to multiple contacts in one go.

Read contacts from an Excel file (Name and Contact columns).

Read the message from a text file.

Automatically opens WhatsApp Web for each contact.

Works with both personalized and fixed messages.

📂 Project Structure
bash
Copy
Edit

├── whatsapp_automate.py       # Main automation script
├── whatsapp_contacts.xlsx     # Excel file with contacts
├── whatsapp_message.txt       # Message template
├── test.py                    # Testing script (optional)

📋 Requirements
Install the dependencies:

bash
Copy
Edit
pip install pandas pyautogui keyboard

⚙️ Usage
Prepare contacts in whatsapp_contacts.xlsx with columns:

Name → Recipient name

Contact → WhatsApp number (with country code, no '+' sign)

Example:

Name	Contact
John Doe	923001234567
Jane Doe	441234567890

Write your message in whatsapp_message.txt.

Run the script:

bash
Copy
Edit
python whatsapp_automate.py
WhatsApp Web will open in your browser, and messages will be sent automatically.

⚠️ Disclaimer
This project is for educational purposes only.
Use responsibly and ensure compliance with WhatsApp's terms of service.
