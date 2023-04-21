import yagmail
import tkinter as tk
import tkinter.simpledialog
import random
import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
import datetime

global counter
global start
start =  datetime.datetime.now()
counter = 0
password = str(random.randint(100000, 999999))


# Define a function to get the recipient email address from the user
def get_recipient_email():
    recipient_email = tk.simpledialog.askstring("Recipient email", "Enter the recipient email address:")
    return recipient_email
# Get the recipient email address from the user
recipient_email = get_recipient_email()


# Send the email using yagmail
yag = yagmail.SMTP('senderemail96@gmail.com', 'gkeupnzsgtmarzpq')
contents = ['This is one OTP',
            str(password)]
flag = yag.send(recipient_email, 'subject', contents)


# Define the TKinter window
root = tk.Tk()
root.geometry("400x200")


# Open the image file and convert it to a TKinter image
image1 = Image.open("true.png")
tk_image1 = ImageTk.PhotoImage(image1)
image2 = Image.open("false.png")
tk_image2 = ImageTk.PhotoImage(image2)

# Define a function to check the entered OTP and display the appropriate screen
def check_password():
    # Get the entered OTP
    otp = otp_entry.get()
    

    # Check if the entered OTP matches the password
    print(password)
    if otp == password:
        # Create a label and display the image
        image_label = tk.Label(root, image=tk_image1)
        image_label.configure(image=tk_image1)
        image_label.image = tk_image1  # update reference to the new image
        image_label.place(x=145,y=70)
        
        root.after(3000, root.destroy)
    else:
        # Display an error message
        image_label = tk.Label(root, image=tk_image2)
        image_label.configure(image=tk_image2)
        image_label.image = tk_image2
        image_label.place(x=145,y=70)
        global counter
        counter += 1
        if counter == 3:
            root.after(1000, root.destroy)
        global start
        current =  datetime.datetime.now()
        elapsed_time = current - start
        if elapsed_time.total_seconds() >= 900:  # 15 minutes
            root.after(1000, root.destroy)
            
  
# Create a label and an entry for the OTP
otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()
otp_entry = tk.Entry(root)
otp_entry.pack()

# Create a button to check the OTP
check_button = tk.Button(root, text="Check OTP", command=check_password)
check_button.pack()

def main():
    # Start the tkinter event loop for the first window
    root.mainloop()

# Call the main function to run the program
if __name__ == '__main__':
    main()
    
