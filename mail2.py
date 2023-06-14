import tkinter as tk
from tkinter import *
from email.message import EmailMessage
import smtplib
from PIL import ImageTk, Image

import speak

# Set up text-to-speech engine
root =tk.Tk()


# Create a window for logging in to the email account
def login_window(root):
    # Create a window
    window = tk.Toplevel(root)
    window.title("LOGIN")   
         # Get screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
        
        # Set window size and position
    window_width = 1166
    window_height = 718
    x_pos = int((screen_width - window_width) / 2)
    y_pos = int((screen_height - window_height) / 2)
    window.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
    window.resizable(0, 0)


    bg_frame = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/background1.png")
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    lgn_frame = Frame(window, bg='#040405', width=950, height=600)
    lgn_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    txt = "WELCOME"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
    heading.place(x=80, y=30, width=300, height=30)

  
    side_image = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/vector.png")
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    sign_in_image = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/hyy.png")
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)
    
    sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)

    username_label = Label(lgn_frame, text="E-mail", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    username_label.place(x=550, y=300)

    username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
    username_entry.place(x=580, y=335, width=270)

    username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=550, y=359)

    # ===== Username icon =========
    username_icon = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/username_icon.png")
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
    username_icon_label.image = photo
    username_icon_label.place(x=550, y=332)


    password_label = Label(lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    password_label.place(x=550, y=380)
    password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
    password_entry.place(x=580, y=416, width=244)

    password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=550, y=440)
    # ======== Password icon ================
    password_icon = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/password_icon.png")
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
    password_icon_label.image = photo
    password_icon_label.place(x=550, y=414)
    window.mainloop()
    # Create a function to log in to the email account
    def login():
        global email_address, password, server
        email_address = username_entry.get()
        password = password_entry.get()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.connect("smtp.gmail.com",587)
            server.starttls()
            server.login(email_address, password)
            speak.Speak('Login successful')
            window.destroy()
            check_credentials(root)
        except smtplib.SMTPAuthenticationError:
            speak.Speak('Invalid login or password')
       


    # Create a button to log in to the email account
    lgn_button = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/btn1.png")
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
    lgn_button_label.image = photo
    lgn_button_label.place(x=550, y=450)
    login = Button(lgn_button_label, text='LOGIN', command=login,font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
    login.place(x=20, y=10)

    
    # Run the window
    window.mainloop()

# Check if the login credentials are valid
def check_credentials(root):
    # Create a window
    window = tk.Toplevel(root)
    window.title("CHECK")
   

      # Get screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
        
        # Set window size and position
    window_width = 1166
    window_height = 718
    x_pos = int((screen_width - window_width) / 2)
    y_pos = int((screen_height - window_height) / 2)
    window.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
    window.resizable(0, 0)

    bg_frame = Image.open(r"C:\Users/asus/Desktop/Workspace/Jarvis-master/images/background1.png")
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    lgn_frame = Frame(window, bg='#040405', width=950, height=600)
    lgn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    
    txt = "CHECK"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
    heading.place(x=80, y=30, width=300, height=30)

    sign_in_label = Label(lgn_frame, text="Do you want to send an email?", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(relx=0.5, rely=0.3, anchor='center')

    confirm_button_yes = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/btn1.png")
    photo = ImageTk.PhotoImage(confirm_button_yes)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
    lgn_button_label.image = photo
    lgn_button_label.place(relx=0.5, rely=0.6, anchor='center')
    login = Button(lgn_button_label, text="Yes",command=lambda: send_email_window(root),font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
    login.place(relx=0.5, rely=0.5, anchor='center')
    confirm_button_no = Image.open(r"C:/Users/asus/Desktop/Workspace/Jarvis-master/images/btn1.png")
    photo = ImageTk.PhotoImage(confirm_button_no)
    confirm_button_label = Label(lgn_frame, image=photo, bg='#040405')
    confirm_button_label.image = photo
    confirm_button_label.place(relx=0.5, rely=0.7, anchor='center')
    logiin = Button( confirm_button_label, text="No",command=window.destroy,font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
    logiin.place(relx=0.5, rely=0.5, anchor='center')

     

    
    # Run the window
    window.wait_window()
    #window.destroy()

# Create a window for sending an email
def send_email_window(root):
       # Create a window
    window = tk.Toplevel(root)
    window.title("SEND EMAIL")
    window.geometry("500x500")
    window.configure(bg="white")

    # Create labels for recipient, subject, and message fields
    to_label = tk.Label(window, text='To',font=("Arial", 20), bg="white", fg="black")
    subject_label = tk.Label(window, text='Subject',font=("Arial", 20), bg="white", fg="black")
    message_label = tk.Label(window, text='Message',font=("Arial", 20), bg="white", fg="black")

    # Create entry fields for recipient, subject, and message
    to_entry = tk.Entry(window,font=("Arial", 16), width=30)
    subject_entry = tk.Entry(window,font=("Arial", 16), width=30)
    message_entry = tk.Entry(window,font=("Arial", 16), width=30)

    # Create a function to send the email
    def send_email():
        to = to_entry.get()
        subject = subject_entry.get()
        message = message_entry.get()
        email = EmailMessage()
        email['To'] = to
        email['Subject'] = subject
        email['From'] = email_address
        email.set_content(message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect("smtp.gmail.com",587)
        server.starttls()
        server.login(email_address, password)
        server.send_message(email)
        speak.Speak('Email sent successfully')
        # engine.runAndWait()
        window.destroy()

    # Create a button to send the email
    send_button = tk.Button(window, text='Send', command=send_email, font=("Arial", 16), bg="blue", fg="white")

    # Pack the labels, entry fields, and send button into the window
    to_label.pack(pady=10)
    to_entry.pack(pady=10)
    subject_label.pack(pady=10)
    subject_entry.pack(pady=10)
    message_label.pack(pady=10)
    message_entry.pack(pady=10)
    send_button.pack()
    frame = tk.Frame(window, bg="white", bd=5)
    frame.place(relx=0.0, rely=0.2, relwidth=0.4, relheight=0.2, anchor="n")
    window.mainloop()
login_window(root)



# #################################################################
# import tkinter as tk
# from email.message import EmailMessage
# import smtplib

# import speak

# # Set up text-to-speech engine
# root =tk.Tk()


# # Create a window for logging in to the email account
# def login_window(root):
#     # Create a window
#     window = tk.Toplevel(root)
#     window.title("LOGIN")
#     window.geometry("500x300")
#     window.configure(bg="white")


#     # Create labels for email and password fields
#     email_label = tk.Label(window, text='Email address',font=("Arial", 20), bg="white", fg="black")
#     password_label = tk.Label(window, text='Password',font=("Arial", 20), bg="white", fg="black")

#     # Create entry fields for email and password
#     email_entry = tk.Entry(window,font=("Arial", 16), width=30)
#     password_entry = tk.Entry(window, show='*',font=("Arial", 16), width=30)

#     # Create a function to log in to the email account
#     def login():
#         global email_address, password, server
#         email_address = email_entry.get()
#         password = password_entry.get()
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.connect("smtp.gmail.com",587)
#             server.starttls()
#             server.login(email_address, password)
#             speak.Speak('Login successful')
#             window.destroy()
#             check_credentials(root)
#         except smtplib.SMTPAuthenticationError:
#             speak.Speak('Invalid login or password')
       


#     # Create a button to log in to the email account
#     login_button = tk.Button(window, text='Log in', command=login, font=("Arial", 16), bg="blue", fg="white")

#     # Pack the labels, entry fields, and login button into the window
#     email_label.pack(pady=10)
#     email_entry.pack(pady=10)
#     password_label.pack(pady=10)
#     password_entry.pack(pady=10)
#     login_button.pack(pady=20)

#     frame = tk.Frame(window, bg="white", bd=5)
#     frame.place(relx=0.0, rely=0.3, relwidth=0.4, relheight=0.2, anchor="n")
    
#     # Run the window
#     window.mainloop()

# # Check if the login credentials are valid
# def check_credentials(root):
#     # Create a window
#     window = tk.Toplevel(root)
#     window.title("CHECK")
#     window.geometry("0x0")
#     window.configure(bg="white")
#     # Create a label to display the status of the login attempt
#     #status_label = tk.Label()

#     # Check if the login credentials are valid
#     server.quit()
#     confirm_window = tk.Toplevel(root)
#     confirm_label = tk.Label(confirm_window, text="Do you want to send an email?",font=("Arial", 20), bg="white", fg="black")
#     confirm_button_yes = tk.Button(confirm_window, text="Yes", command=lambda: send_email_window(root), font=("Arial", 16), bg="blue", fg="white")
#     confirm_button_no = tk.Button(confirm_window, text="No", command=confirm_window.destroy, font=("Arial", 16), bg="blue", fg="white")
#     confirm_label.pack(pady=10)
#     confirm_button_yes.pack(pady=10)
#     confirm_button_no.pack(pady=10)
     
#     frame = tk.Frame(window, bg="white", bd=5)
#     frame.place(relx=0.0, rely=0.0, relwidth=0.4, relheight=0.2, anchor="n")
    
#     # Run the window
#     window.wait_window()
#     #window.destroy()

# # Create a window for sending an email
# def send_email_window(root):
#     # Create a window
#     window = tk.Toplevel(root)
#     window.title("SEND EMAIL")
#     window.geometry("500x500")
#     window.configure(bg="white")

#     # Create labels for recipient, subject, and message fields
#     to_label = tk.Label(window, text='To',font=("Arial", 20), bg="white", fg="black")
#     subject_label = tk.Label(window, text='Subject',font=("Arial", 20), bg="white", fg="black")
#     message_label = tk.Label(window, text='Message',font=("Arial", 20), bg="white", fg="black")

#     # Create entry fields for recipient, subject, and message
#     to_entry = tk.Entry(window,font=("Arial", 16), width=30)
#     subject_entry = tk.Entry(window,font=("Arial", 16), width=30)
#     message_entry = tk.Entry(window,font=("Arial", 16), width=30)

#     # Create a function to send the email
#     def send_email():
#         to = to_entry.get()
#         subject = subject_entry.get()
#         message = message_entry.get()
#         email = EmailMessage()
#         email['To'] = to
#         email['Subject'] = subject
#         email['From'] = email_address
#         email.set_content(message)
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.connect("smtp.gmail.com",587)
#         server.starttls()
#         server.login(email_address, password)
#         server.send_message(email)
#         speak.Speak('Email sent successfully')
#         # engine.runAndWait()
#         window.destroy()

#     # Create a button to send the email
#     send_button = tk.Button(window, text='Send', command=send_email, font=("Arial", 16), bg="blue", fg="white")

#     # Pack the labels, entry fields, and send button into the window
#     to_label.pack(pady=10)
#     to_entry.pack(pady=10)
#     subject_label.pack(pady=10)
#     subject_entry.pack(pady=10)
#     message_label.pack(pady=10)
#     message_entry.pack(pady=10)
#     send_button.pack()
#     frame = tk.Frame(window, bg="white", bd=5)
#     frame.place(relx=0.0, rely=0.2, relwidth=0.4, relheight=0.2, anchor="n")
#     window.mainloop()
#login_window(root)