## Getting Started
- [Official Getting Started](http://nvidia.com/jetsonnano-start)



## Tutorials

- [facial recog with jetson nano](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)


default networking - l4tbr0
ipv4 settings - manual
192.168.55.1 / 24
gateway 192.168.55.100


## Jetson clocks
It has moved and is now located in a ifferent folder
it is now located at ```/usr/bin/jetson_clocks``` so to execute

```
sudo ~/jetson_clocks.sh
sudo /usr/bin/jetson_clocks/jetson_clocks.shx
```

## get detailed instructions on a device

```
lsusb
```

Find how many USB devices are connected
```
$ find /dev/bus
```

use lsusb command with the -D parameter to display the detail of specific a device
```
$ lsusb -D /dev/bus/usb/003/002
```