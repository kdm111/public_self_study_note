class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       
   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       
   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # 로봇이 주어지고 어떤 방과 위치가 주어진다.
        # 방의 가로 세로와 위치의 좌표는 알지 못한다.
        