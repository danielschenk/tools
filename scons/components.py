#!/usr/bin/env python

# Copyright (C) 2017 Daniel Schenk <danielschenk@users.noreply.github.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
