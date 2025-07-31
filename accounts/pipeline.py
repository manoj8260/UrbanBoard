from accounts.emails import send_activation_email

def send_google_email(strategy, details,user = None , is_new = False,*args,**kwargs):
    print(user)
    if user and is_new and user.email  :
        # print("Welcome email being sent to:", user.email)
        # print("Strategy request data:", strategy.request_data())
        # print("User details from Google:", details)
        atenticate_type = 'google' 
        return  send_activation_email(user,atenticate_type=atenticate_type)

        
    
