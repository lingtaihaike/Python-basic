import os
import re

route_n_result = os.popen("route -n").read()
gateway = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',route_n_result)[1]
print('网关为:' + gateway)