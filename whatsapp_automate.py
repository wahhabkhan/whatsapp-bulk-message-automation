# Import the 'time' module for adding delays in the script.
import time  
# Import the 'webbrowser' module as 'web' for opening web URLs.
import webbrowser as web  
# Import the 'quote' function from the 'urllib.parse' module for URL encoding.
from urllib.parse import quote
# Import the 'keyboard' module as 'k' for simulating keyboard inputs.
import keyboard as k 
# Import the 'pandas' library as 'pd' for data manipulation.
import pandas as pd
# Import the 'pyautogui' library for controlling the mouse and keyboard.
import pyautogui  

# Define a function named 'send_whatsapp' that takes Excel file, text file, and optional coordinates as parameters.
def send_whatsapp(data_file_excel, message_file_text, x_cord=533, y_cord=693):
   # Read an Excel file with contact information and set the data type of the 'Contact' column to 'str'.
   df = pd.read_excel(data_file_excel, dtype={"Contact": str})

   # Extract 'Name' and 'Contact' columns from the Excel data.
   name = df['Name'].values
   contact = df['Contact'].values
   # Store the message file path in the 'files' variable.
   files = message_file_text  

   # Open and read the message file.
   with open(files) as f:
       file_data = f.read()

   # Create a zipped iterable of 'Name' and 'Contact' pairs.
   zipped = zip(name, contact)

   # Initialize a message counter.
   counter = 0  

   # Loop through each pair of 'Name' and 'Contact'.
   for (a, b) in zipped:
       # Format the message with the 'Name'.
       msg = file_data.format(a)  

       # Open the WhatsApp web URL with the formatted message.
       web.open(f"https://web.whatsapp.com/send?phone={b}&text={quote(msg)}")

       # Wait for 15 seconds.
       time.sleep(15)  

       # Click at the specified coordinates on the screen using pyautogui.
       pyautogui.click(x_cord, y_cord)

       # Wait for 2 seconds.
       time.sleep(2)  

       # Simulate pressing the 'Enter' key.
       k.press_and_release('enter')  

       # Wait for 2 seconds.
       time.sleep(2)  

       # Simulate pressing the 'Enter' key again.
       k.press_and_release('enter')  

       # Wait for 2 seconds.
       time.sleep(2)  

       # Simulate pressing 'Ctrl+W' to close the tab.
       k.press_and_release('ctrl+w')  

       # Wait for 1 second.
       time.sleep(1)  

       # Increment the message counter.
       counter += 1  
       # Print a message indicating a message was sent.
       print(counter, "Message Sent..!!")  

   # Print "Done!" when all messages have been sent.
   print("Done!")  

# Define file paths for the Excel file and text message file.
excel_path = r"D:\Projects\drancy\whatsapp_contacts.xlsx"
text_path = r"D:\Projects\drancy\whatsapp_message.txt"

# Call the 'send_whatsapp' function with the specified file paths as arguments.
send_whatsapp(excel_path, text_path)
