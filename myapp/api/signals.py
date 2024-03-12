
def request_started_handler(sender, **kwargs):
    print('Hi from request_start_handler. Sender:', sender)

def request_finished_handler(sender, **kwargs):
    print('Hi from request_finished_handler.')    

