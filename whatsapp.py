import pywhatkit
import pandas as pd
import logging
import sys

# Configure error logging
error_logging = logging.getLogger('error_logger')
error_logging.setLevel(logging.ERROR)
error_handler = logging.FileHandler('whatsapp_error.log')
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
error_logging.addHandler(error_handler)

# Configure success logging
success_logging = logging.getLogger('success_logger')
success_logging.setLevel(logging.INFO)
success_handler = logging.FileHandler('whatsapp_success.log')
success_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
success_logging.addHandler(success_handler)

# Redirect standard output and standard error to the log file
sys.stdout = open('whatsapp.log', 'a', buffering=1)  # Append mode with line buffering
sys.stderr = sys.stdout

file_path = "./numbers.xlsx"
df = pd.read_excel(file_path)

mode = "contact"

if mode == "contact":
    # Send a WhatsApp message to specific contacts
    for number,name in df[['number', 'name']].values:
        try:
            print(f"Sending a message to {name} ({number})")
            message = f'This is a message by {name}'
            
            pywhatkit.sendwhatmsg_instantly(number, message, wait_time=20, tab_close=True)
            print(f"Message sent successfully to {name} ({number})")
            success_logging.info(f"Message sent successfully to {name} ({number})")
        except Exception as e:
            error_message = f"Failed to send a message to {name} ({number}): {str(e)}"
            print(error_message)
            error_logging.error(error_message)

elif mode == "group":
    # Send a WhatsApp message to a specific group
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")
