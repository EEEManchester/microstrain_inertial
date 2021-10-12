#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Imu

def imuDataCallback(imu):
    #rospy.loginfo("IMU Sequence: ", imu.header.seq);
    #rospy.loginfo("IMU Stamp (sec): ", imu.header.stamp);
    rospy.loginfo("Linear Acceleration:     [%f, %f, %f]", imu.linear_acceleration.x, imu.linear_acceleration.y, imu.linear_acceleration.z);
    rospy.loginfo("Angular Velocity:        [%f, %f, %f]", imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z);
    rospy.loginfo("Quaternion Orientation:  [%f, %f, %f, %f]", imu.orientation.x, imu.orientation.y, imu.orientation.z, imu.orientation.w);
   # add code here to handle incoming IMU data
    
def listener():

    rospy.init_node('listener', anonymous=True)

    # get the device name parameter
    deviceName = 'gx5'
    nameParam = rospy.get_name() + '/device'

    if rospy.has_param(nameParam):
        deviceName = rospy.get_param(nameParam)

        # clear parameter for future use
        rospy.delete_param(nameParam)

    # subscribe to the imu/data topic
    #Parameters:
    #   topic - namespace (defined in launch file) and topic name
    #   message type - type of message expected
    #   callback - callback function to handle this data
    rospy.Subscriber(("/" + deviceName + "/imu/data"), Imu, imuDataCallback)
    rospy.loginfo(("listening to /" + deviceName + "/imu/data"))

    # start listening for data
    rospy.spin()

if __name__ == '__main__':
    listener()
