import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "#STUDY!!!",
            message = "TIME IS UP NOW LETS STUDY ",
            app_icon=r"C:\Users\ashis\OneDrive - Personal\OneDrive\Documents\python notification project\Icons8-Windows-8-Printing-Books.ico",
            timeout=15
        )
        time.sleep(1)
