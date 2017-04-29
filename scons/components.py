#!/usr/bin/env python

"""Components module for SCons"""


def _component(env, name, objects):
    """Define a component
    
    :param env:     the SCons environment to add the component to      
    :param name:    the name of the component
    :param objects: the objects of which the component consists
    """

    if name in env['COMPONENTS']:
        raise ValueError('Component {} already exists'.format(name))
    env['COMPONENTS'][name] = objects


def _get_components(env, *args):
    """Get the objects of the given component(s)
    
    :param env:     the SCons environment
    :param args:    the names of the components
    """

    objects = []
    for name in args:
        objects.append(env['COMPONENTS'][name])

    return objects


def install(env):
    """Install the components module on the given SCons environment
    
    :param env: the SCons environment to install on
    """

    env['COMPONENTS'] = {}
    env.AddMethod(_component, 'Component')
    env.AddMethod(_get_components, 'GetComponents')
