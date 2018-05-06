#!/usr/bin/env python

# MIT License
#
# Copyright (C) 2017 Daniel Schenk <danielschenk@users.noreply.github.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Components module for SCons"""


def _component(env, name, objects):
    """Define a component
    
    :param env:     the SCons environment to add the component to      
    :param name:    the name of the component
    :param objects: the objects of which the component consists
    """

    variant_dir = env['COMPONENTS_VARIANT_DIR']

    if name in env['COMPONENTS'][variant_dir]:
        raise ValueError('Component {} already exists'.format(name))
    env['COMPONENTS'][variant_dir][name] = objects


def _get_components(env, *args):
    """Get the objects of the given component(s)
    
    :param env:     the SCons environment
    :param args:    the names of the components
    """

    variant_dir = env['COMPONENTS_VARIANT_DIR']
    objects = set()
    for name in args:
        [objects.add(obj) for obj in env['COMPONENTS'][variant_dir][name]]

    return list(objects)


def install(env):
    """Install the components module on the given SCons environment
    
    :param env: the SCons environment to install on
    """

    variant_dir = env.Dir('.').abspath
    env['COMPONENTS'] = {}
    env['COMPONENTS'][variant_dir] = {}
    env['COMPONENTS_VARIANT_DIR'] = variant_dir
    env.AddMethod(_component, 'Component')
    env.AddMethod(_get_components, 'GetComponents')
