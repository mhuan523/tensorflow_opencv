# basic function for tensorflow
import tensorflow as tf

constant = tf.constant(10, dtype=tf.int32)
variable = tf.Variable(15, name='var')
print(constant)
print(variable)

session = tf.Session()
print(session.run(constant))
initializer = tf.global_variables_initializer()
session.run(initializer)
print(session.run(variable))