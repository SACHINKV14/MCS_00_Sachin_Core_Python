# importing the module
import pywhatkit


try:
    pywhatkit.sendwhatmsg("+917760504584","Hello from GeeksforGeeks",10, 35)
    print("Successfully Sent!")

except:

    # printing the error message
    print("Network Error Occured")
