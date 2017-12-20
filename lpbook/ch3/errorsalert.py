# errorsalert.py
# Reference: w_pacb43.pdf, page 76


alert_system = 'console'    # Other value ca be 'email'
error_severity = 'critical' # Other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
    print(error_message)        #1
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)     #2
    elif error_severity == 'medium':
        send_email('support.1@example.com', error_message)  #3
    else:
        send_email('support.2@example.com', error_message)  #4
