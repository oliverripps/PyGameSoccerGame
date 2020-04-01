CS241 Final Project

We should use the GitHub feature of Branching!!!!

Branching-If we have a working master branch(which is what the basic github push and pull runs on), it is most effective working as a group to not all
be committing to that and messing it up. Especially when we'll all be working on different things. Branching solves this.

Process of Branching
-run "git branch" to see all the branches in our project. The starred one is the branch you are currently on.
-when you create a branch you are copying all the code from master and then changing it without changing master. When you are done(when the new feature works in the code), you merge the branch back to master(using a pull request ideally--ill explain later).
-when you are on master, create a new branch using "git checkout -b [the name of the branch you want to create]". To move to a branch that is already created, use "git checkout [branch you want to go to]" and to create a new branch "git branch [name of branch you want to create]". The -b statement consolidates those two statements into one and makes it easier.
-when you finish up on your branch and want to merge the code back to master, the ideal way to do it is using pull requests. If you go to the github directory on the github website, you can click on branches, find your branch and create new pull request. This then notifies every member of the group to review the code(if they want) and then you can merge it to the master branch.
-the thing this prevents most is us all adding stuff to master and breaking it and then not understanding why its broken and spending a ton of time debugging. It will take a little longer at first but save us a lot of time down the road.
