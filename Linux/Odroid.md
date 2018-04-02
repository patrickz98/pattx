#### Lights

How to shut up the alive led.
echo none > /sys/class/leds/led1/trigger

How to make it stop blinking:
echo default-on > /sys/class/leds/led1/trigger

How to make it show the eMMC activity:
echo mmc1 > /sys/class/leds/led1/trigger

How to make it show the SD activity:
echo mmc0 > /sys/class/leds/led1/trigger

How to make it blink as you want to:
echo timer > /sys/class/leds/led1/trigger

echo 1000 > /sys/class/leds/led1/delay_on
echo 1000 > /sys/class/leds/led1/delay_off
