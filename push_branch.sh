#!/bin/sh

# Clone it locally (git clone git@github.com:aronchick/mystify.git)
# Add upstream repo (git remote add upstream git@github.com:machine-learning-apps/mystify.git)
# Create a feature/topic branch (`git checkout -b awesome_feature)
# Code fix/feature
# don’t forget to add tests/specs and make sure they pass
# Commit code on feature/topic branch (git add . && git commit -m “awesome”)
# Checkout master (git checkout master)
git checkout master

# Pull latest from upstream (git pull upstream master)
git pull upstream master

# Checkout feature/topic branch (git checkout awesome_feature)
git checkout wb

# Rebase your changes onto the latest changes in master (git rebase master)
git rebase master

# Push your fix/feature branch to your fork (git push origin awesome_feature)
git push origin wb

# On Github website