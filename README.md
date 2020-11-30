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

