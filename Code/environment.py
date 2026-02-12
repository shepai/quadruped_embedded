# load in the model and terrain
import mujoco
from mujoco import viewer
import time
import numpy as np

class environment:
    def __init__(self, path="/its/home/drs25/Documents/GitHub/"):
        self.m = mujoco.MjModel.from_xml_path(path + "/quadruped_embedded/Model/quadruped_presstip.xml")
        self.data = mujoco.MjData(self.m)
    def step(self, target_angles):
        kp = 20
        kd = 2

        for i in range(12):
            q = self.data.qpos[i]
            qd = self.data.qvel[i]

            torque = kp*(target_angles[i] - q) - kd*qd
            self.data.ctrl[i] = torque

        mujoco.mj_step(self.m, self.data)
    def observe(self): #gather observations
        pass 

if __name__=="__main__":
    env=environment()
    with viewer.launch(env.m, env.data) as v:
        while v.is_running():
            env.step([0 for i in range(12)])