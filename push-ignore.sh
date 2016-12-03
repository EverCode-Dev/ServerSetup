#!/bin/sh

cp -fv gitignore .gitignore
git add .gitignore
git commit -m 'Updated Git ignore file'
./push.sh
