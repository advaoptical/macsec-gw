#! /usr/bin/env python
# coding=utf-8
##############################################
# Copyright (c) 2020
# ADVA Optical Networking
##############################################
import base64
import json
import struct
import signal2
import socket
import sys
import commands
# import subprocess
import argparse
from socket import socket, AF_PACKET, SOCK_RAW
sys.path.append('/opt/adva/extra')
from macsec_gw_api import gw_api_msg
CMD_IFNAME = "vEth1"

def get_pid(proc_name):
    pid = -1
    # z = subprocess.check_output(['ps', '-aux', '|', 'grep', proc_name])
    z = commands.getstatusoutput('ps -aux | grep ' + proc_name)
    pids = z[1].split('\n')
    # sudo is 1st process, we need to communicate with its child
    s = 'sudo'
    for i in range(0, len(pids)):
        if s in pids[i]:
            pid = int(pids[i+1].split()[1])
            return pid

    for i in range(0, len(pids)):
        if 'grep' not in pids[i]:
            pid = int(pids[i].split()[1])
            return pid
        
    return pid

SIGRTMIN = 34
SIGRTMAX = 64


class XsecRekey256b:
    def __init__(self):
        # Look for the process
        self.pid = get_pid('macsec')
        self.key = ""

    def send_key_256b(self, base64_key):
        key_base64_bytes = base64_key.encode('ascii')
        key_bytes = struct.unpack('@32B', base64.b64decode(key_base64_bytes))
        self.key = key_bytes
        hex_dump('# Key in bytes:', key_bytes, len(key_bytes))
       # 32 bytes
        for i in range(8):
            d = bytes_to_int(key_bytes, i * 4)
            # print('%08x' % d)
            val = signal2.sigval_t(socket.htonl(d))
            # print('%8x' % val.sigval_ptr )
            err = signal2.sigqueue(self.pid, SIGRTMIN, val)
            if err:
                print('error %d' % err)
            #     sys.exit(err)
        return

    def read_key(self, fn):
        return


def bytes_to_int(arr, idx):
    res = 0
    for i in range(4):
        res |= ((arr[idx + i]) << 8*i)
    return res


def hex_dump(fmt, arr, len):
    s = fmt+'\n'
    for i in range(len):
        if i % 16 == 0:
            s += '%08x: ' % i
        s += '%02x ' % arr[i]
        # if (i+1) % 4 == 0:
        #     s += ' '
        if (i+1) % 16 == 0:
            s += '\n'
    print(s)

def api_send_keys(base64_key):
    key_base64_bytes = base64_key.encode('ascii')
    key_bytes = struct.unpack('@32B', base64.b64decode(key_base64_bytes))
    hex_dump('# Key in bytes:', key_bytes, len(key_bytes))
    keys = key_bytes + key_bytes
    s = socket(AF_PACKET, SOCK_RAW)
    s.bind((CMD_IFNAME, 0))
    api = gw_api_msg(CMD_IFNAME)
    # print keys
    peer_idx=0
    s.send(api.msg_rekey(peer_idx, keys))        


if __name__ == "__main__":
    
    key_obj = {"key_ID":"f600c46f-b561-4b2b-bb6a-525bac61d61f",
            "key":"G8f7NMcrNQREEzfldJMDGpuUdfJxnMJL71Y5wscwZA8="}
    test_base64_message = key_obj.get('key')

    parser = argparse.ArgumentParser()
    parser.add_argument("base64_key", nargs='*', default=test_base64_message, help="Base64 encoded 256bit key used for RX and TX for MACsec session")
    parser.add_argument('-f', '--file', help="file name containing QKD JSON")

    args = parser.parse_args()

    base64_key = args.base64_key
    
    if args.file:
      s = open(args.file, 'r').read()
      d = json.loads(s)
      base64_key = d[u'keys'][0]['key']
      print("Key ID: %s" % d[u'keys'][0]['key_ID'])

    print("Base64 encoded key: %s" % base64_key)

    api_send_keys(base64_key)

    # a = XsecRekey256b()
    # # RX key
    # a.send_key_256b(base64_key)
    # # TX Key
    # a.send_key_256b(base64_key)
