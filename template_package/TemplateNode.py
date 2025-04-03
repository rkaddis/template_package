import rclpy
import rclpy.parameter
import rclpy.publisher
import rclpy.subscription

from std_msgs.msg import String


class TemplateNode(rclpy.Node):

    template_publisher = None
    template_param = None

    def __init__(self):
        # Initialize the node and set the node's ROS name.
        super().__init__(node_name="TemplateNode")

        # Declare a parameter and read in the value.
        self.declare_parameter(name="template_param", value="")
        self.template_param = self.get_parameter(name="template_param")

        # Create a publisher.
        self.template_publisher = self.create_publisher(String, "template_pub_topic", 1)

        # Create a subscriber. The callback function is called when data is received over the subscribed topic.
        self.create_subscription(String, "template_sub_topic", self.template_subscriber_callback, 1)


    # Subscriber callback. Called whenever data is received over the subscribed topic.
    def template_subscriber_callback(self, msg : String):
        pass


# This function called by ROS when the file is loaded.
def main(args=None):
    rclpy.init(args=args)
    node = TemplateNode() # create the node
    
    rclpy.spin(node) # spin the node until ROS is shut down
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        