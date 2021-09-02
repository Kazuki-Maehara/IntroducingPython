import os
import stat

os.chmod('oops.txt', 0o400)
os.chmod('oops.txt', stat.S_IRUSR)
