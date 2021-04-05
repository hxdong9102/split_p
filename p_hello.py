###

print("Hello, I'm a python file in parent_tree repository")

from child_tree.sub_demo import child_demo

test = child_demo.Demo()
test.info()
test.date()

print("Congratulations!")
