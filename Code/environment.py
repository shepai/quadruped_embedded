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
        for i in range(12):
            self.data.ctrl[i] = target_angles[i]
        #print(self.data.ctrl)
        mujoco.mj_step(self.m, self.data)

    def observe(self): #gather observations
        pass 

if __name__=="__main__":
    env=environment()
    print("nu:", env.m.nu)
    print("njnt:", env.m.njnt)
    print("actuator mapping:", env.m.actuator_trnid)
    with viewer.launch(env.m, env.data) as v:
        while v.is_running():
            env.step([np.random.random()*100 for _ in range(12)]) 