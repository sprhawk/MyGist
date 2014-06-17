git
===

### 在merge产生冲突时，得到原始的文件 ###
```shell
git checkout --ours -- path/to/file.txt
git checkout --theirs -- path/to/file.txt
git pull -Xtheirs
```

### 比较Xcode的Localizable.strings文件 ###
(from :http://www.entropy.ch/blog/Developer/2010/04/15/Git-diff-for-Localizable-strings-Files.html)

First, add this to the project’s .git/info/attributes file:
+
```
 *.strings diff=localizablestrings
```
(Unfortunately you do have to add it to every project, there doesn’t seem to be a global attributes configuration file)

Second, add this to your ~/.gitconfig file:
+
```
[diff "localizablestrings"]
   textconv = "iconv -f utf-16 -t utf-8"
```


### 创建一个全新的分支（与其他分支没有关联）###
```shell
git symbolic-ref HEAD refs/heads/newbranch 
rm .git/index 
git clean -fdx 
<do work> 
git add your files 
git commit -m 'Initial commit'
```
[http://book.git-scm.com/5_creating_new_empty_branches.html]

### git stash ###
```shell
$ git stash save "work in progress for foo feature"
$ git commit -a -m "blorpl: typofix"
$ git stash apply
$ git stash list
$ git stash apply stash@{1}
$ git stash clear
```

### 生成一个新的key ###
```shell
ssh-keygen -t rsa -C "..."
to ~/.ssh/github_id_rsa
ssh-add ~/.ssh/github_id_rsa
ssh -T git@github.com
```

### git revert ###
```shell
$ git revert HEAD
Finished one revert.
[master]: created 1e689e2: 
  "Revert "Updated to Rails 2.3.2 and edge hoptoad_notifier""
  
  $ git revert HEAD~3
```

### git submodule ###
```
$ git submodule add  (NOTE: Do not use local URLs here if you plan to publish your superproject!)
```

Pulling down the submodules is a two-step process. First run git submodule
init to add the submodule repository URLs to .git/config:
```
$ git submodule init
$ git submodule update
```

If you want to make a change within a submodule and you have a detached head, then you should create or checkout a branch, make your changes, publish the change within the submodule, and then update the superproject to reference the new commit:
```
$ git checkout master
```
or
```
$ git checkout -b fix-up
```


then
```
$ echo "adding a line again" >> a.txt
$ git commit -a -m "Updated the submodule from within the superproject."
$ git push
$ cd ..
$ git diff
diff --git a/a b/a
index d266b98..261dfac 160000
--- a/a
+++ b/a
@@ -1 +1 @@
-Subproject commit d266b9873ad50488163457f025db7cdd9683d88b
+Subproject commit 261dfac35cb99d380eb966e102c1197139f7fa24
$ git add a
$ git commit -m "Updated submodule a."
$ git push
```

### git push --tags ###

### remove a git submodule ###
1. Delete the relevant section from the .gitmodules file.
2. Delete the relevant section from .git/config.
3. Run git rm --cached path_to_submodule (no trailing slash).
4. Commit and delete the now untracked submodule files.



### 忽略文件的更改 ###
git update-index --assume-unchanged <filename>


### 开启色彩输出 ###
git config --global color.ui true

