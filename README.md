# 📱 WhatsApp Bulk Message Automation

A Python-based tool to send **personalized or bulk WhatsApp messages** via WhatsApp Web.  
Reads contact information from an Excel sheet and message text from a file, then automates the sending process using `pyautogui` and `keyboard`.

---

## ✨ Features
- 🚀 Send messages to multiple contacts in one go.
- 📂 Read contacts from an Excel file (`Name` and `Contact` columns).
- 📝 Read the message from a text file.
- 🌐 Automatically opens WhatsApp Web for each contact.
- 🛠 Works with both personalized and fixed messages.

---

## 📂 Project Structure
```
├── whatsapp_automate.py       # Main automation script
├── whatsapp_contacts.xlsx     # Excel file with contacts
├── whatsapp_message.txt       # Message template
├── test.py                    # Testing script (optional)
```

---

## 📋 Requirements
Install the dependencies:
```bash
pip install pandas pyautogui keyboard
```

---

## ⚙️ Usage

### 1️⃣ Prepare Contacts
In `whatsapp_contacts.xlsx` create a sheet with columns:
- **Name** → Recipient name
- **Contact** → WhatsApp number (with country code, no '+' sign)

Example:
| Name      | Contact      |
|-----------|--------------|
| John Doe  | 923001234567 |
| Jane Doe  | 441234567890 |

---

### 2️⃣ Write Your Message
In `whatsapp_message.txt`, write the message you want to send.

---

### 3️⃣ Run the Script
```bash
python whatsapp_automate.py
```

---

### 4️⃣ Automation
- WhatsApp Web will open in your browser.
- The script will send messages automatically to each contact.

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Use responsibly and ensure compliance with WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/).

---
