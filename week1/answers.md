1. Define the following (one sentence each):

Node
A node is an independent program in ROS 2 that performs computations and communicates with other nodes.
Topic
A topic is a named channel used by nodes to send or receive messages asynchronously.
Package
A package is a folder that contains ROS 2 code, configuration, and resources for one project or functionality.
Workspace
A workspace is a directory where multiple ROS 2 packages are developed, built, and managed together.


2. Explain why sourcing is required. What happens if you do not source a workspace?

Sourcing sets up the ROS 2 environment so the system can find your packages, executables, and dependencies. If you do not source a workspace, ROS 2 commands will not recognize your custom packages.

3. What is the purpose of colcon build? What folders does it generate?

colcon build compiles all the packages in your workspace, resolves dependencies, and prepares them for use. It generates three main folders:

* build/  contains temporary build files
* install/  contains the final executables, libraries, and setup files
* log/  contains logs of the build and any errors

4. In your own words, explain what the entry_points console script does in setup.py.

The entry_points allows you to create a command-line shortcut for running your Python node. For example:

```python
entry_points={
    'console_scripts': [
        'simple_node = my_first_pkg.simple_node:main',
    ],
}
```

This means that when you type

```bash
ros2 run my_first_pkg simple_node
```

ROS 2 will automatically run the main() function in the file simple_node.py inside your package. 

5. Diagram showing one publisher and one subscriber connected by a topic:

ASCII version:


[Publisher Node] ---> (Topic) ---> [Subscriber Node]


Explanation: The publisher sends messages to the topic, and the subscriber receives messages from the same topic.


