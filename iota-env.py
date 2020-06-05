import gym
from gym import error , spaces, utils
from gym.utils import seeding
import pybullet as p

class sumofIotas(gym.Env):
    metadata = {'render.modes':['human']}

    def __init__(self):
        p.connect(p.GUI)
        p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.55,-0.35,0.2])
        ## These are to be redfined
        self.action_space = spaces.Box(np.array([-1]*4), np.array([1]*4))
        self.observation_space = spaces.Box(np.array([-1]*5), np.array([1]*5))
        
        
        
    def step(self,action):
        pass
    def reset(self):
        pass
    def render(self,mode='human'):
        pass
    def close(self):
        pass

    
