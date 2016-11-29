#!/usr/bin/env python

import sys
import rospy
import actionlib
from pr2motion.srv import *
from pr2motion.msg import *


def init():
    client = actionlib.SimpleActionClient('/pr2motion/Init',pr2motion.msg.InitAction)
    client.wait_for_server()
    goal=pr2motion.msg.InitGoal()
    client.send_goal(goal)
    client.wait_for_result()
    print client.get_result()

def connect_port(local,remote):
    rospy.wait_for_service('/pr2motion/connect_port')
    try:
        connect_handle=rospy.ServiceProxy('/pr2motion/connect_port',pr2motion.srv.connect_port)
        request=pr2motion.srv.connect_portRequest()
        request.local=local
        request.remote=remote
        result=connect_handle(request)
        print result.genom_exdetail
        return result.genom_success
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__=="__main__":
    rospy.init_node('setup_pr2motion')
    init()
    connect_port("joint_state","joint_states")
    connect_port("head_controller_state","/head_traj_controller/state")
    connect_port("traj","/gtp/trajectory")

