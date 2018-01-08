#!/usr/bin/env python3

# Copyright (C) 2016 Vimal A.R <arvimal@yahoo.in>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import sys
import pathlib
import configparser
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

HOME = os.getenv('HOME')
DAISHO_HOME = HOME + "/.config/daisho/"
CONFIG = DAISHO_HOME + "daisho.conf"
TODO_LIST = DAISHO_HOME + "to-do.yaml"
HISTORY = DAISHO_HOME + "history.txt"


class Daisho(object):
    """Daisho's main class"""
    
    def __init__(self):
        # Check existence of CONFIG and TODO_LIST
        if all([pathlib.Path(CONFIG).exists(),
                pathlib.Path(TODO_LIST).exists()]):
            print("\nWelcome to Daisho")
            self.daisho_help()
            self.daisho_prompt()
        else:
            print("\nWelcome to Daisho.\n")
            print("Initial setup:")
            print("\tCreating Daisho's configurations")

            # Create HOME, CONFIG, TODO_LIST, and HISTORY
            pathlib.Path(DAISHO_HOME).mkdir()
            pathlib.Path(CONFIG).touch(exist_ok=True)
            pathlib.Path(TODO_LIST).touch(exist_ok=True)
            pathlib.Path(HISTORY).touch(exist_ok=True)
            # Write Daisho's configuration file
            conf_parser = configparser.ConfigParser()
            conf_parser.add_section("Global")
            conf_parser.set("Global", "DAISHO_HOME", DAISHO_HOME)
            conf_parser.set("Global", "CONFIG", CONFIG)
            conf_parser.set("Global", "TODO_LIST", TODO_LIST)
            conf_parser.set("Global", "HISTORY", HISTORY)
            with open(CONFIG, "w") as config_file:
                conf_parser.write(config_file)
            print("\tDone\n")
            self.daisho_help()
            self.daisho_prompt()

    def daisho_help(self):
        """
        Daisho's Usage
        """
        print("\nUsage:")
        print(" 1. add <to-do>          - Add a new to-do.")
        print(" 2. search <key-word>    - Search for a keyword.")
        print(" 3. list <day>           - List to-dos for the day.")
        print(" 4. help                 - Prints this help message. ")
        print(" 5. quit                 - Quits Daisho. \n")
        pass

    def daisho_prompt(self):
        """
        Daisho's prompt.
        Process user-input
        """
        cmd_list = ['add', 'list', 'search', 'help', 'quit']
        keyword_completer = WordCompleter(cmd_list)

        while True:
            daisho_prompt = prompt("daisho ->> ",
                                   history=FileHistory(HISTORY),
                                   auto_suggest=AutoSuggestFromHistory(),
                                   completer=keyword_completer)
            value = daisho_prompt.split(" ")
            # Split based on inputs
            if value[0] == 'add':
                self.add_tasks(value)
            elif value[0] == 'list':
                self.list_tasks(value)
            elif value[0] == 'search':
                self.search_tasks(value)
            elif value[0] == 'help':
                self.daisho_help()
            elif value[0] == 'quit':
               sys.exit("\nExiting Daisho.\n")
            else:
                self.daisho_help()

    def list_tasks(self):
        """Lists tasks.
        Takes arguments such as `today`, `tomorrow`, weekday etc..

        Not yet implemented, come again later!
        """

        pass

    def add_tasks(self, *args):
        # Add tasks as yaml
        pass

    def search_tasks(self):
        """Search tasks based on keywords"""
        print("Not yet implemented, come again later!")
        pass


if __name__ == "__main__":
    my_daisho = Daisho()
    my_daisho()
