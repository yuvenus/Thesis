#!/usr/bin/env python
#Version: 07/06/2016

import rospy
from std_msgs.msg import String

def change_face(emote):
  pub = rospy.Publisher('robot_face/speak', String, queue_size=10)
  rospy.init_node('change_face', anonymous=True)
  rate = rospy.Rate(10) # 10hz
  count = 0
  while not rospy.is_shutdown() and count != 1:
    if (emote == "help"):
      exp = "can you please help me?"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "happy" or emote == "Happy"):
      exp = ":) thank you!!"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "greet" or emote == "Greet"):
      exp = "hello! :)"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "sad" or emote == "Sad"):
      exp = "aww you didn't help me :("
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    #facial expressions
    elif (emote == "reg"):
      exp = "."
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "smile"):
      exp = ":)"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "frown"):
      exp = ":("
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "surprise"):
      exp = ":o"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    elif (emote == "disgust"):
      exp = ":&"
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()
    else:
      exp = emote
      rospy.loginfo(exp)
      pub.publish(exp)
      count += 1
      rate.sleep()


#emote = raw_input("What emote? ")

if __name__ == '__main__':
  try:
    change_face(emote)
  except rospy.ROSInterruptException:
      pass
