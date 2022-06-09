# cloning to a local repo

CD to your home directory and issue `git clone https://github.com/umrosbrian/debian_home_dir`.  You'll need to then move all of the contents of the `debian_home_dir` directory into the home directory.

# working in a local repo

Every home directory that this repo will be cloned to is going to contain different items.  Rather than adding all files and directories to the .gitignore file for all untracked files and directories of all the systems it's very helpful to have a .git/info/exclude file on each system that the repo is cloned to.  The bash command `cd ; find . -maxdepth 1 ! -name \.bashrc  ! -name \.vimrc ! -name \.tmux\.conf ! -name \.functions ! -name README\.md | sed '/^\.$/d;s/^\.\///' > .git/info/exclude` will populate the file with everything in the home directory apart from the files that are tracked in this repo.
