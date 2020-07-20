import gym
from gym import error , spaces, utils
from gym.utils import seeding
import pybullet as p
from iota_controller import iOTA
class sumofIotas(gym.Env):
    metadata = {'render.modes':['human']}

    def __init__(self,no_of_modules=5):
        p.connect(p.GUI)
        p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.55,-0.35,0.2])
        ## These are to be redfined
        self.nom = no_of_modules
        self.action_space = spaces.Box(low=np.array([0]*self.nom+[-1]*self.nom), high=np.array([1]*self.nom+[1]*self.nom))
        self.observation_space = spaces.Box()
        
        
        
    def step(self,action):
        pass
    def reset(self):
        pass
    def render(self,mode='human'):
        pass
    def close(self):
        pass

    
