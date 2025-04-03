#! /usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    template_param_arg = DeclareLaunchArgument('template_param_arg', default_value='')
    
    TemplateNode_node = Node(
            package='template_package',
            executable='TemplateNode',
            namespace="/",
            name='TemplateNode',
            parameters=[
                {'template_param': LaunchConfiguration("template_param_arg")}
            ],
        )
    
    
    
    return LaunchDescription([
        template_param_arg,
        TemplateNode_node,
    ])