#!/usr/bin/python

import time

class Flyweight(type):
    def __init__(cls, name, bases, dct):
        cls.__instances = {}
        type.__init__(cls, name, bases, dct)

    def __call__(cls, key, *args, **kw):
        print "Fly", key

        instance = cls.__instances.get(key)
        if instance is None:
            instance = type.__call__(cls, key, *args, **kw)
            cls.__instances[key] = instance
        return instance

n = 0

class Astro:
    __metaclass__ = Flyweight

    def __init__(self, key):
        global n

        print "Astro:", key

        n += 1
        print "Creando la instancia '%s'..." % key
        time.sleep(2)
        print "'%s' creado" % key


a = Astro('luna')
b = Astro('luna')
b = Astro('luna')
assert a is b
c = Astro('sol')
print n
