# adding SSH key to GitHub

Chances are, you're setting up a new machine.  See 
[make a SSH key on your machine](https://imgexch.com/web/computer/git.php#make-a-ssh-key-on-your-machine) and the 
following
[add the SSH key to your GitHub account](https://imgexch.com/web/computer/git.php#add-the-ssh-key-to-your-github-account).


# cloning to a local repo

CD to your home directory and issue `git clone https://github.com/umrosbrian/debian_home` or `git clone git@github.com:umrosbrian/debian_home.git` if you have a SSH public key on Github.  You'll need to then move all of the contents of the `debian_home` directory into the home directory.  You can do this by issuing the bash commands `find debian_home -mindepth 1 -maxdepth 1 -exec mv '{}' . \; ; rmdir debian_home`.  You'll probably want to issue `. ~/.bashrc`.

# working in a local repo

Every home directory that this repo will be cloned to is going to contain different items.  You probably don't want to see all of the contents when you issue something like `git status`.  Rather than adding all files and directories to the `.gitignore` file for all untracked files and directories of all the systems it's very helpful to have a `.git/info/exclude` file on each system that the repo is cloned to.  The bash script `add_repo_exlusions.sh`, which is included in the repo can be issued with `bash add_repo_exclusions.sh` to populate the file with everything in the home directory apart from the files that are tracked in this repo.  After issuing the script, you shouldn't see any `untracked` files when issuing `git status`.  If you happen to see an item pop up when issuing `git status` but don't want it tracked you can use `echo <item_you_don't_want_tracked >> .git/info/exclude` to add the item rather than reissuing the script.

