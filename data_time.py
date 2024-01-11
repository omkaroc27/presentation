import datetime
import os
path = r"sample.txt"
# file modification timestamp of a file
m_time = os.path.getmtime(path)
dt_m = datetime.datetime.fromtimestamp(m_time)
print('Modified on:', dt_m)
# file creation timestamp in float
c_time = os.path.getctime(path)
# convert creation timestamp into DateTime object
dt_c = datetime.datetime.fromtimestamp(c_time)
print('Created on:', dt_c)
