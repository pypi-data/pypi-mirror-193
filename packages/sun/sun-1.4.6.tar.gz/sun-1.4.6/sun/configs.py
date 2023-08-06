#!/usr/bin/python3
# -*- coding: utf-8 -*-

# configs.py is a part of sun.

# Copyright 2015-2023 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://gitlab.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os
import tomli

from sun.__metadata__ import data_configs, __all__


class Configs:

    config_file: str = f'{__all__}.toml'
    config_path: str = data_configs['sun_conf_path']

    # Default time configs.
    interval: int = 720
    standby: int = 3

    # Tool for managing the active processes
    process_tool: str = 'pgrep -l'

    # The default prefix to check for in the Log files.
    compare: str = "^\w[Mon|Tue|Wed|Thu|Fri|Sat|Sun]"

    # Default repository
    repositories: list = [
        {'NAME': 'Slackware',
         'HTTP_MIRROR': 'https://mirrors.slackware.com/slackware/slackware64-15.0/',
         'LOG_PATH': '/var/lib/slackpkg/', 'LOG_FILE': 'ChangeLog.txt',
         'PATTERN': 'Upgraded[.]|Rebuilt[.]|Added[.]|Removed[.]'}
    ]

    # Configuration file.
    toml_file_path: str = f'{config_path}{config_file}'

    try:  # Load configuration from /etc/sun/sun.toml file.
        if os.path.isfile(toml_file_path):
            with open(toml_file_path, 'rb') as conf:
                configs = tomli.load(conf)
        else:
            raise Exception(f"Error: Failed to find '{toml_file_path}' file.")

        interval: int = configs['time']['INTERVAL']
        standby: int = configs['time']['STANDBY']
        process_tool: str = configs['tools']['PROCESS']
        compare: str = configs['prefix']['COMPARE']
        repositories: list = configs['repository']
    except (tomli.TOMLDecodeError, KeyError) as error:
        print(f"Error: {error}: in the config file '{config_path}{config_file}'.")
