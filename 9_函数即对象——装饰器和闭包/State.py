
def control_state():
    '''
    控制基本状态
    '''
    speed =0
    direction ="stopped"

    def get_(command=None,value=None):
        nonlocal speed,direction
        match command:
            case "set_value":
                speed=value
            case "set_direction":
                direction=value
        return {"speed":speed,"direction":direction}
    return get_

