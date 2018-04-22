# basic funtions of tensorflow matrix

import  tensorflow as tf

mat1 = tf.constant([[1, 2]])
mat2 = tf.constant([[3, 4]])
mat3 = tf.constant([[5],
                   [6]])

mat4 = tf.constant([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

with tf.Session() as session:
    print(session.run([mat1, mat2, mat3]))
    print(mat1.shape, mat2.shape, mat3.shape)  #dimensions
    print(session.run(mat4[0]))
    print(session.run(mat4[:, 1]))
    print(session.run(mat4[2, 2]))

mat5 = tf.matmul(mat1, mat3)
mat6 = tf.multiply(mat1, mat3)
with tf.Session() as session:
    print(session.run(mat5))
    print(session.run(mat6))

mat7 = tf.zeros([3, 4])
mat8 = tf.ones([5, 5])
mat9 = tf.fill([3, 3], 2)
mat10 = tf.linspace(0., 1. ,11)
mat11 = tf.random_uniform([3, 3], -1, 3)
with tf.Session() as session:
    print(session.run(mat7))
    print(session.run(mat8))
    print(session.run(mat9))
    print(session.run(mat10))
    print(session.run(mat11))