import pygame
import sys
import rospy
from std_msgs.msg import String
pygame.init()

pygame.display.set_mode((1, 1), pygame.NOFRAME)

def num():
  pub = rospy.Publisher('chatter', String, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  while not rospy.is_shutdown():
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_1:
                  pub.publish("1")
              elif event.key == pygame.K_2:
                  pub.publish("2")
              elif event.key == pygame.K_3:
                  pub.publish("3")
              elif event.key == pygame.K_4:
                  pub.publish("4")
              elif event.key == pygame.K_5:
                  pub.publish("5")
              elif event.key == pygame.K_6:
                  pub.publish("6")
              elif event.key == pygame.K_7:
                  pub.publish("7")
              elif event.key == pygame.K_8:
                  pub.publish("8")
              elif event.key == pygame.K_9:
                  pub.publish("9")

if __name__ == '__main__':
    try:
        num()
    except rospy.ROSInterruptException:
        pass
