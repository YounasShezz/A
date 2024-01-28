import subprocess
import sys
cmd = subprocess
reload="systemctl reload apache2 {}".format

pr=reload(sys.argv[1])
print(pr, sys.argv[0])
    #cmd.run(["";"","",""])
