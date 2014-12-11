#minute hour day month day-of-week command-line-to-execute
#set to run weekly at midnight on Sunday
0 0 * * 0 rm $ceres/*/*output* 
0 0 * * 0 (cd $ceres/commerce && setenv PYTHONPATH "$PYP" && python commerce.py)
0 0 * * 0 (cd $ceres/nhb && setenv PYTHONPATH "$PYP" && python nhb.py)
0 0 * * 0 (cd $ceres/zauba && setenv PYTHONPATH "$PYP" && python zauba.py)
