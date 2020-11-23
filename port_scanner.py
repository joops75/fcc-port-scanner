import socket
import re
from common_ports import ports_and_services as dict

def get_open_ports(target, port_range, verbose=False):  
  try:
    host_IPv4 = socket.gethostbyname(target)

  except:
    if re.search('^\d+\.\d+\.\d+\.\d+$', target):
      return 'Error: Invalid IP address'
    else:
      return 'Error: Invalid hostname'

  try:
    hostname = socket.gethostbyaddr(host_IPv4)[0]

  except:
    hostname = ''

  open_ports = []
  for port in range(port_range[0], port_range[1] + 1):
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.2)
      s.connect((host_IPv4, port))
      open_ports.append(port)

    except:
      pass

    s.close()

  if verbose:
    ans = []
    if hostname:
      ans.append('Open ports for ' + hostname + ' (' + host_IPv4 + ')')

    else:
      ans.append('Open ports for ' + host_IPv4)

    ans.append('PORT'.ljust(9) + 'SERVICE')

    for open_port in open_ports:
      try:
        port_desc = dict[open_port]

      except:
        port_desc = ''

      ans.append(str(open_port).ljust(9) + port_desc)

    ans = '\n'.join(ans)

  else:
    ans = open_ports

  return ans