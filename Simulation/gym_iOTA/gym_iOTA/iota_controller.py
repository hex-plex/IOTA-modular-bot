import pybullet as p
import numpy as np
import cv2

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-10)

class iOTA:
    body_id = None
    __phyCli = None
    joints_info=[]
    def __init__(self,body_id,physicsClient,is_created=True,basePosition=None,baseOrientationInEuler=None):
        self.body_id = body_id
        self.__phyCli = physicsClient
        if not is_created:
            if basePosition is None:
                raise Exception("The basePosition is mandatory if is_created is False")
            if baseOrientationInEuler is None:
                raise Exception("The baseOrientationInEuler is mandatory if is_created is False")
            if len(baseOrientationInEuler)==3:
                baseOrientationInEuler = p.getQuaternionFromEuler(baseOrientationInEuler)
            iota=p.loadURDF('iota.urdf',basePosition,baseOrientationInEuler)
    def control_angle(self):
        pass

    def control_form(self):
        pass

    def __del__(self):
        self.__break_all()
        p.removeBody(self.body_id,physicsClientId=self.__phyCli)

    def __repr__(self):
        return "<IOTA-"+str(self.body_id)+">"

    def get_state(self):
        return p.getLinkState(self.body_id,
                              linkIndex=0,
                              computeLinkVelocity=1,
                              computeForwardKinematics=1,
                              physicsClientId=self.__phyCli) ## Give out only relavant data
    def make_joint(self, other_body_id):
        pass

    def break_joint(self, other_body_id):
        pass
    
    def __break_all(self):
        while len(joints_info)!=0:
            self.break_joint(joints_info[0])
            joints_info.pop(0)
            
    def get_joints_info(self):
        pass

    


iotas=[]
for i in range(n):
    iota=p.loadURDF('iota.urdf',[i,0,0],p.getQuaternionFromEuler([0,0,0]))
    iotas.append(iOTA(iota,physicsClient))

