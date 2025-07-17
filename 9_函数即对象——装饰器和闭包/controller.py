from decorators import log_command,simulate,timer

@timer
@log_command
@simulate
def Turn_left():
    print(f"Turning left")

@log_command
@simulate
def Move_forward(units):
    print(f"🚕 is moving forward {units} uniuts")

@log_command
@simulate
def Stop():
    print(f"Stopping")