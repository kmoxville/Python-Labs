#!/bin/bash
git checkout dev
git commit -a -m 'Commit changes to branch'
git push
git checkout prd
git merge dev

