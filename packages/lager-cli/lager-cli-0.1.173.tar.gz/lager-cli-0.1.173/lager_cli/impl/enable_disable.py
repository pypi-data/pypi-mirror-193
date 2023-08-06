import os
import json
from lager.pcb.net import Net, NetType
from lager.pydexarm import Dexarm

def net_setup(*args, **kwargs):
    pass

def net_teardown(*args, **kwargs):
    pass

def disable_net(netname):
    target_net = Net(netname, type=NetType.Analog, setup_function=net_setup, teardown_function=net_teardown)
    with Dexarm(port="/dev/ttyACM1") as arm:
        (x, y, z, extrusion, theta_a, theta_b, theta_c) = arm.get_current_position()
        if z != 0.0:
            arm.move_to_blocking(x, y, 0.0, timeout=5.0)

def enable_net(netname):
    target_net = Net(netname, type=NetType.Analog, setup_function=net_setup, teardown_function=net_teardown)
    with Dexarm(port="/dev/ttyACM1") as arm:
        (x, y, z, extrusion, theta_a, theta_b, theta_c) = arm.get_current_position()
        if z != 0.0:
            arm.move_to_blocking(x, y, 0.0, timeout=5.0)

        (target_x, target_y, target_z) = target_net.location
        arm.move_to_blocking(target_x, target_y, 0.0, timeout=5.0)
        arm.move_to_blocking(target_x, target_y, target_z, timeout=5.0)

def start_capture(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.start_capture()

def stop_capture(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.stop_capture()    

def start_single(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.start_single_capture() 

def force_trigger(netname):
    target_net = Net(netname, type=None, setup_function=net_setup, teardown_function=net_teardown)
    target_net.force_trigger()     

def main():
    command = json.loads(os.environ['LAGER_COMMAND_DATA'])
    if command['action'] == 'disable_net':
        disable_net(**command['params'])
    elif command['action'] == 'enable_net':
        enable_net(**command['params'])  
    elif command['action'] == 'start_capture':
        start_capture(**command['params']) 
    elif command['action'] == 'stop_capture':
        stop_capture(**command['params']) 
    elif command['action'] == 'start_single':
        start_single(**command['params']) 
    elif command['action'] == 'force_trigger':
        force_trigger(**command['params'])                                            
    else:
        pass

if __name__ == '__main__':
    main()
