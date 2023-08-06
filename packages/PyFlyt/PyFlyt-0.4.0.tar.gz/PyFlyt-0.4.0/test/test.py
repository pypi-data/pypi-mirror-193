import numpy as np

from PyFlyt.core import Aviary

# the starting position and orientations
start_pos = np.array([[0.0, 0.0, 5.0]])
start_orn = np.array([[1.571, 0.0, 0.0]])

# environment setup
env = Aviary(
    start_pos=start_pos,
    start_orn=start_orn,
    render=True,
    drone_type="rocket",
    drone_model="rocket",
    # use_camera=True,
)

# set to position control
env.set_mode(0)

env.drones[0].get_joint_info()

# simulate for 1000 steps (1000/120 ~= 8 seconds)
for i in range(10000):
    print("----------------------------------------------------")
    print(f"Fuel remaining: {env.drones[0].aux_state}")
    print(f"Throttle setting: {env.drones[0].boosters.throttle_setting}")
    print(f"Ignition state: {env.drones[0].boosters.ignition_state}")
    print(f"Fuel mass: {env.getDynamicsInfo(env.drones[0].Id, 0)[0]}")
    print(f"Fuel inertia: {env.getDynamicsInfo(env.drones[0].Id, 0)[2]}")

    # pitch, yaw, ignition, thrust_setting, booster_gimbal_1, booster_gimbal_2
    if i > 100 and i < 1000:
        env.drones[0].setpoint = np.array([-1.0, 0.0, 1.0, 1.0, 0.0, 0.0])
    else:
        env.drones[0].setpoint = np.array([0.0, 0.0, 0.0, 1.0, 0.0, 0.0])
    env.step()
