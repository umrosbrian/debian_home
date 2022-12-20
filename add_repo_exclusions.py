"""Add content that don't want in a repo to .git/info/exclude."""

import os


files_to_keep = ['.bashrc', '.vimrc', '.tmux.conf', '.functions', 'README.md', '.ideavimrc', 'add_repo_exclusions.sh',\
                'add_repo_exclusions.py', '.pi_functions']
with open(os.path.join('.git','info','exclude'), 'w') as f:
    for item in os.listdir(os.curdir):
        if item not in files_to_keep:
            f.write(f"{item}\n")