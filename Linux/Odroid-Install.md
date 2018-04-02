# Install new odroid img

Download at: https://odroid.in

	unxz ubuntu-16.04-mate-odroid-u2u3-20160920.img.xz
	sudo diskutil unmount /dev/disk2s1
	sudo dd if=ubuntu-16.04-mate-odroid-u2u3-20160920.img of=/dev/disk2 bs=100m
	sudo diskutil unmountDisk /dev/disk2


Ssh on Odroid:

	sudo apt-get update
	sudo apt-get install nano bash-completion
	sudo mv /etc/smsc95xx_mac_addr /etc/smsc95xx_mac_addr-old

	sudo nano /etc/hostname
	sudo nano /etc/hosts

Edit .bash_rc:

	export LANGUAGE=en_US.UTF-8
	export LANG=en_US.UTF-8
	export LC_ALL=en_US.UTF-8


Stuff:

	sudo locale-gen en_US.UTF-8
	sudo dpkg-reconfigure locales
	sudo apt-get install php7.0 php7.0-zip php7.0-xml php7.0-mysql php7.0-curl
	echo none > /sys/class/leds/led1/trigger
	lsb_release -a