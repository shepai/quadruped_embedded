# load in the model and terrain
import mujoco
from mujoco import viewer
import time
import numpy as np

m = mujoco.MjModel.from_xml_path("/its/home/drs25/Documents/GitHub/quadruped_embedded/Model/quadruped_presstip.xml")
data = mujoco.MjData(m)

with viewer.launch(m, data) as v:
    while v.is_running():
        mujoco.mj_step(m, data)
