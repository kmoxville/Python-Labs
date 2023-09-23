#!/bin/bash
git checkout -b dev
git commit -a -m 'Commit changes to branch'
git push
git checkout -b prd
git merge dev

