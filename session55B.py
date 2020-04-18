import tensorflow as tf
# from tensorflow.python import pywrap_tensorflow_internal

print(tf.version)

sess = tf.Session()

hello = tf.constant("Hello")
print(sess.run(hello))

a = tf.constant(20)
b = tf.constant(22)

print('a + b = {0}'.format(sess.run(a+b)))