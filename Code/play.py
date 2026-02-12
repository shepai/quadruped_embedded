import mujoco
from mujoco.viewer import launch

# Load the model
model = mujoco.MjModel.from_xml_path("/its/home/drs25/Documents/GitHub/quadruped_embedded/Model/quadruped_presstip.xml")
sim = mujoco.MjSim(model)

# Launch the built-in interactive viewer with sliders
launch(sim)
