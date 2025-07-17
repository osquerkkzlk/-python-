from controller import Move_forward,Turn_left,Stop
from State import control_state

if __name__ == '__main__':
    state=control_state()
    state("set_direction","forward")
    state("set_value",20)
    print(f"[STATE_CURRENT] {state()}")

    # 开始运行
    Move_forward(20,simulate=True)
    Turn_left(simulate=True)
    Stop()
