import os

ip_or_host = input("Input ip or host to test:")

os.system('ping -c 6 {}'.format(ip_or_host))
