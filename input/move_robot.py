#!/usr/bin/env python
#Version: 07/06/2016

#every 100 counts is around 1/2 meters!!!
#momentum does play a huge factor, so ymmv!

#threading = one thread will change the variables, the other will

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import String

def move(linear, angular, move_type):
  pub = rospy.Publisher('/pioneer/cmd_vel', Twist, queue_size=10)
  string_pub = rospy.Publisher('chatter', String, queue_size=10)
  rospy.init_node('move_robot', anonymous=True)
  rate = rospy.Rate(100) # 10hz
  angular *= 0.01745
  count = 0
  vel = Twist(Vector3(linear,0,0),Vector3(0,0,angular))
  rospy.loginfo(vel)
  pub.publish(vel)
      #rate.sleep()
      #count += 1


#lin = 0
#ang = 0
#move_type = "stop"

if __name__ == '__main__':
  try:
    move_robot(linear,angular)
  except rospy.ROSInterruptException:
      pass
