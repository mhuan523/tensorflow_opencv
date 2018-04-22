# basic function for tensorflow
import tensorflow as tf

constant = tf.constant(10, dtype=tf.int32)
variable = tf.Variable(15, name='var')
print(constant)
print(variable)

'''
session = tf.Session()
print(session.run(constant))
initializer = tf.global_variables_initializer()
session.run(initializer)
print(session.run(variable))
'''

session = tf.Session()
initializer = tf.global_variables_initializer()

with session:
    session.run(initializer)
    print(session.run(constant))
    print(session.run(variable))



#basic numeric operations

cons1 = tf.constant(2)
cons2 = tf.constant(5)
consAdd = tf.add(cons1, cons2)
consSub = tf.subtract(cons1, cons2)
consMul = tf.multiply(cons1, cons2)
consDiv = tf.divide(cons1, cons2)

with tf.Session() as session:
    print(session.run(cons1))
    print(session.run(cons2))
    print(session.run(consAdd))
    print(session.run(consSub))
    print(session.run(consMul))
    print(session.run(consDiv))

var1 = tf.Variable(5)
var2 = tf.Variable(7)

varAdd = tf.add(var1, var2)
varSub = tf.subtract(var1, var2)
assign = tf.assign(var2, varAdd)
varMul = tf.multiply(var1, var2)
varDiv = tf.divide(var1, var2)
variables_initializer = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(variables_initializer)
    print(session.run(var1))
    print(session.run(var2))
    print(session.run(varAdd))
    print(session.run(varSub))
    print(session.run(varMul))
    print(session.run(varDiv))
    print('session.run(assign):',session.run(assign))
    print('assign.eval():', assign.eval())
    print('tf.get_default_session.run(assign):', tf.get_default_session().run(assign))









