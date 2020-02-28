import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.util import degrees, Angel, Pose

def main():
    args = anki_vector.util.parse_command_args()

    
    with anki_vector.Robot(args.serial) as robot:

    	#drive off charger
    	robot.behavior.drive_off_charger()

    	robot.world.connect_cube()

    	#pick up cube object
    	if robot.world.connected_light_cube:
    		robot.behavior.pickup_object(robot.world.connected_light_cube)

    	#get current position of robot
    	current_robot_pose = robot.pose.position
    	print(current_robot_pose)

    	#got to desired position with cube
        pose = Pose(x=10, y=10, z=0, angle_z=Angle(degrees=0))
        robot.behavior.go_to_pose(pose)
        print(robot.pose.position)

        #drop off the cube object
        time.sleep(3.0)
        pose_future.cancel()
        robot.behavior.place_object_on_ground_here()

       


if __name__ == "__main__":
    main()
