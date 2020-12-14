# macsec-gw
Packages for PQC macsec-gw

## linux command line for DPDK performance

```
grubby --info=ALL
...
grubby --update-kernel=/boot/vmlinuz-4.14.79-adva-23 --args="isolcpu=1-7 nohz_full=1-7 rcu_nocbs=1-7"
```
## CPU arch detection
```
gcc -march=native -Q --help=target | grep march
```
## Set MTU for protected port: 1426

MACsec in VXLAN overhead is 74 bytes, thus MTU for protected port should be 1426 bytes. Any oversized packets are discarded in macsc-gw application, as result iperf3 shows zero throghput.

## iperf3 fierwall on server side
```
firewall-cmd --add-port=5201/tcp
firewall-cmd --list-ports
```
## copy ssh public keys of the peers
ssh-copy-id might not work because of the external firewall rules.
Adding public keys manually and restart sshd works.

# FRA and BER configuration snippets
## FRA
```
[root@fra ~]# systemctl status xsec-dpdk
● xsec-dpdk.service - ADVA AT xsec DPDK drivers
   Loaded: loaded (/usr/lib/systemd/system/xsec-dpdk.service; enabled; vendor preset: disabled)
   Active: inactive (dead) since Mon 2020-12-07 22:05:44 UTC; 6 days ago
  Process: 611 ExecStartPost=/usr/local/sbin/dpdk-devbind --force --bind=igb_uio 0000:00:06.0 0000:00:07.0 (code=exited, status=0/SUCCESS)
  Process: 607 ExecStart=/usr/sbin/insmod /opt/adva/extra/dpdk/igb_uio.ko (code=exited, status=1/FAILURE)
  Process: 603 ExecStart=/usr/sbin/insmod /opt/adva/extra/dpdk/rte_kni.ko carrier=on kthread_mode=multiple (code=exited, status=1/FAILURE)
  Process: 597 ExecStart=/usr/sbin/modprobe vfio-pci (code=exited, status=0/SUCCESS)
  Process: 590 ExecStart=/usr/sbin/modprobe uio (code=exited, status=0/SUCCESS)
  Process: 578 ExecStartPre=/opt/adva/extra/set-huge-pages.sh (code=exited, status=0/SUCCESS)
 Main PID: 607 (code=exited, status=1/FAILURE)
 
 [root@fra ~]# systemctl status macsec-gw -l
● macsec-gw.service - ADVA AT MACsec GW
   Loaded: loaded (/usr/lib/systemd/system/macsec-gw.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2020-12-07 22:05:44 UTC; 6 days ago
 Main PID: 631 (macsec-gw)
   CGroup: /system.slice/macsec-gw.service
           └─631 /opt/adva/extra/macsec-gw -l 1,2 --vdev crypto_aesni_gcm,socket_id=0,max_nb_sessions=128 -- -p 0x1 -P -u 0x1 --config="(0,0,1),(0,0,2)" -a -f /opt/adva/extra/ep-vxlan.cfg

Dec 14 19:01:32 fra macsec-gw[631]: HS:  *Info: REKEY 9404-76e3, peer[0]
Dec 14 19:01:36 fra macsec-gw[631]: HS: [OK] Established, peer[0], hs_spi:3, old_spi:2, retr_cnt:1

[root@fra ~]# cat /opt/adva/extra/ep-vxlan.cfg
# Neibghor rules
neigh port 0 82:01:e3:e2:c4:ae
neigh port 1 02:01:d8:0d:41:65
#vxlan
vxlan vni 5005 s
[root@fra ~]# ifconfig vEth2 mtu 1426
[root@fra ~]# ifconfig vEth2 10.0.0.1/24
[root@fra ~]# ip route
default via 217.160.210.1 dev vEth0 proto dhcp metric 100
10.0.0.0/24 dev vEth2 proto kernel scope link src 10.0.0.1
217.160.210.1 dev vEth0 proto dhcp scope link metric 100
217.160.210.23 dev vEth0 proto kernel scope link src 217.160.210.23 metric 100
[root@fra ~]# ping 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=29.1 ms
c 217.160.210.23 dst 85.215.238.110

[root@fra ~]# ifconfig vEth2 mtu 1426
[root@fra ~]# ifconfig vEth2 10.0.0.1/24
[root@fra ~]# ip route
default via 217.160.210.1 dev vEth0 proto dhcp metric 100
10.0.0.0/24 dev vEth2 proto kernel scope link src 10.0.0.1
217.160.210.1 dev vEth0 proto dhcp scope link metric 100
217.160.210.23 dev vEth0 proto kernel scope link src 217.160.210.23 metric 100
[root@fra ~]# ping 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=29.1 ms
```
## BER

```
[root@ber ~]# systemctl status xsec-dpdk
● xsec-dpdk.service - ADVA AT xsec DPDK drivers
   Loaded: loaded (/usr/lib/systemd/system/xsec-dpdk.service; enabled; vendor preset: disabled)
   Active: inactive (dead) since Mon 2020-12-07 16:46:02 UTC; 1 weeks 0 days ago
  Process: 5296 ExecStartPost=/usr/local/sbin/dpdk-devbind --force --bind=igb_uio 0000:00:06.0 0000:00:07.0 (code=exited, status=0/SUCCESS)
  Process: 5290 ExecStart=/usr/sbin/insmod /opt/adva/extra/dpdk/igb_uio.ko (code=exited, status=1/FAILURE)
  Process: 5287 ExecStart=/usr/sbin/insmod /opt/adva/extra/dpdk/rte_kni.ko carrier=on kthread_mode=multiple (code=exited, status=1/FAILURE)
  Process: 5285 ExecStart=/usr/sbin/modprobe vfio-pci (code=exited, status=0/SUCCESS)
  Process: 5279 ExecStart=/usr/sbin/modprobe uio (code=exited, status=0/SUCCESS)
  Process: 5272 ExecStartPre=/bin/echo performance | /usr/bin/tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor (code=exited, status=0/SUCCESS)
  Process: 5260 ExecStartPre=/opt/adva/extra/set-huge-pages.sh (code=exited, status=0/SUCCESS)
 Main PID: 5290 (code=exited, status=1/FAILURE)
[root@ber ~]# systemctl status macsec-gw -l
● macsec-gw.service - ADVA AT MACsec GW
   Loaded: loaded (/usr/lib/systemd/system/macsec-gw.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2020-12-07 16:46:02 UTC; 1 weeks 0 days ago
 Main PID: 5309 (macsec-gw)
   CGroup: /system.slice/macsec-gw.service
           └─5309 /opt/adva/extra/macsec-gw -l 1,2 --vdev crypto_aesni_gcm,max_nb_sessions=128 -- -p 0x1 -P -u 0x1 --config="(0,0,1),(0,0,2)" -f /opt/adva/extra/ep-vxlan.cfg

Dec 14 19:06:27 ber macsec-gw[5309]: HS: [OK] Established, peer[0], hs_spi:0, old_spi:3, retr_cnt:0
Dec 14 19:07:21 ber macsec-gw[5309]: MACSEC: macsec_inbound_post() failed crypto op, status: 0x2, short_len: 32, session: 0x1002daf40
Dec 14 19:07:22 ber macsec-gw[5309]: HS:  *Info: REKEY 9412-3163, peer[0]
Dec 14 19:07:25 ber macsec-gw[5309]: HS: [OK] Established, peer[0], hs_spi:1, old_spi:0, retr_cnt:0
[root@ber ~]# cat /opt/adva/extra/ep-vxlan.cfg
# Neibghor rules
neigh port 0 82:01:7c:9a:15:99
neigh port 1 02:01:e1:71:e1:2b
#vxlan
vxlan vni 5005 src 85.215.238.110  dst 217.160.210.23
[root@ber ~]# ifconfig vEth2 mtu 1426
[root@ber ~]# ifconfig vEth2 10.0.0.2/24

```
