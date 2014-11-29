#/usr/bin/bash

#replaces location of code in crontab.txt clears crontab, and sets crontab to crontab.txt
crontab -r
export ceres=~/Code/ceres
perl -pi -e 's/\$ceres/~\/Code\/ceres/g' crontab.txt
crontab $ceres/script/crontab.txt
