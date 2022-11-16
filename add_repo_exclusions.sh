#!/bin/bash
IFS=$'\n'

cd
find . -maxdepth 1 ! -name \.bashrc ! -name \.vimrc ! -name \.tmux\.conf ! -name \.functions ! -name README\.md ! -name \.ideavimrc ! -name add_repo_exclusions\.sh | sed '/^\.$/d;s/^\.\///' > .git/info/exclude
echo "git status:"
git status
