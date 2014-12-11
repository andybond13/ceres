#minute hour day month day-of-week command-line-to-execute
#set to run weekly at midnight on Sunday
0 0 * * 0 rm $ceres/*/*output* 
0 0 * * 0 (cd $ceres/commerce && export PYTHONPATH=$PYP && python commerce.py)
0 0 * * 0 (cd $ceres/nhb && export PYTHONPATH=$PYP && python nhb.py)
0 0 * * 0 (cd $ceres/zauba && export PYTHONPATH=$PYP && python zauba.py)
