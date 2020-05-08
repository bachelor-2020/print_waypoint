#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import rospy
from mavros_msgs.msg import WaypointReached


class Print_waypoint:
    def __init__(self):
        rospy.init_node("waypoint_reached")

        sub_gps = rospy.Subscriber(
            "mavros/mission/reached", WaypointReached, self.print_wp, queue_size=1
        )  # Fra Ardupilot

        # sub_gps = rospy.Subscriber(
        #     "mission/reached", WaypointReached, self.print_wp, queue_size=1
        # )  # Fake Waypoint

        self.rate = rospy.Rate(2)

    def print_wp(self, msg):
        print("\nVeipunkt nådd:".decode("utf-8"))
        print("\tTidsstempel:")
        print("\t\tsekunder:", msg.header.stamp.secs)
        print("\t\tnanosekunder:", msg.header.stamp.nsecs)
        print("\n\tVeipunkt #:", msg.wp_seq)


if __name__ == "__main__":
    try:
        p = Print_waypoint()
        while not rospy.is_shutdown():
            p.rate.sleep()

    except rospy.ROSInterruptException:
        pass
