#!/bin/bash
git checkout dev
git add --all
git commit -a -m 'Commit changes to branch'
git push
git checkout prd
git merge dev
git push

