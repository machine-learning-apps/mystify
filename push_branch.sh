#!/bin/sh

# Clone it locally (git clone git@github.com:aronchick/mystify.git)
# Add upstream repo (git remote add upstream git@github.com:machine-learning-apps/mystify.git)
# Create a feature/topic branch (`git checkout -b awesome_feature)
# Code fix/feature
# don’t forget to add tests/specs and make sure they pass
# Commit code on feature/topic branch (git add . && git commit -m “awesome”)
# Checkout master (git checkout master)
<<<<<<< HEAD
git checkout master

# Pull latest from upstream (git pull upstream master)
git pull upstream master
=======
git checkout main

# Pull latest from upstream (git pull upstream master)
git pull upstream main
>>>>>>> 6303ef9525c9718f80f88c66350806a426d80ada

# Checkout feature/topic branch (git checkout awesome_feature)
git checkout wb

# Rebase your changes onto the latest changes in master (git rebase master)
<<<<<<< HEAD
git rebase master
=======
git rebase main
>>>>>>> 6303ef9525c9718f80f88c66350806a426d80ada

# Push your fix/feature branch to your fork (git push origin awesome_feature)
git push origin wb

# On Github website