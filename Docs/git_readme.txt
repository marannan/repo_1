sudo apt-get install git
create a new repo in github
create a new directory in your system
git init
git add * 
git commit -a -m "comment"
git remote add <repo_name> <git_url> repo_name is your github repo name and usl is the github url for your repo
git push -f(force) -u(first time only) repo_name <dest_branch> mostly master

Reverting commits
git reset --hard HEAD to reset the HEAD to latest commit
git rebase -i HEAR~no will list the last no commits, remove the commits if needed save
git push repo_name master --force to sync the local and remote git repository since we've rebased the local
