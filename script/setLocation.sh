#!/bin/bash

#replaces location of code in crontab.txt clears crontab, and sets crontab to crontab.(bash,tcsh)
crontab -r

#(1) edit this line!: code directory 
export ceres=~/Code/ceres
#(2) edit this line!: code directory ~/a/b --> s/\$ceres/~\/a\/b/g
# the s/\$ceres/ and /g must be there
# see how all the / slashes in the address now have to be \/, that's it!
perl -pi -e 's/\$ceres/~\/Code\/ceres/g' crontab.tcsh
perl -pi -e 's/\$ceres/~\/Code\/ceres/g' crontab.bash
#(3) edit this line: ~/local/lib/python2.6/site-packages/
export PYP=~/local/lib/python2.6/site-packages/
#(4) edit this line!: ~/local/lib/python2.6/site-packages
perl -pi -e 's/\$PYP/~\/local\/lib\/python2.6\/site-packages/g' crontab.tcsh
perl -pi -e 's/\$PYP/~\/local\/lib\/python2.6\/site-packages/g' crontab.bash

if [[ $SHELL == *"bash"* ]]
then
  echo "bash";
  echo "export PYTHONPATH=$PYP" >> ~/.bashrc
  echo "export PYTHONPATH=$PYP" >> ~/.bash_profile
  source ~/.bashrc
  crontab $ceres/script/crontab.bash;
fi
if [[ $SHELL == *"tcsh"* ]]
then
  echo "tcsh";
  echo "setenv PYTHONPATH \"$PYP\"" >> ~/.cshrc
  tcsh -c 'source ~/.cshrc'
  crontab $ceres/script/crontab.tcsh;
fi
