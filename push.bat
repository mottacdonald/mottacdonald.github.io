@echo off

set /p commitmsg=Enter commit message: 

git add .
git commit -m "%commitmsg%"
git push

pause