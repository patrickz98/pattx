#!/bin/sh

ISPUSER=root
ISPWORKDIR=/home/odroid/Core
ISPWORKPUB=$ISPWORKDIR/pattx
ISPTASKCLIENT=initscript.php
PHPBIN=`which php`

### BEGIN INIT INFO
# Provides:          ispwork
# Required-Start:    $network $local_fs $remote_fs
# Required-Stop:     $network $local_fs $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start ISPWork daemons (taskclient.php)
### END INIT INFO


# Defaults
RUN_MODE="daemons"

LOGDIR=~/log
PIDDIR=~/run
TCLDPID=$PIDDIR/$ISPTASKCLIENT.pid

# clear conflicting settings from the environment
unset TMPDIR

# See if the daemons are there
test -f $ISPWORKPUB/$ISPTASKCLIENT  || exit 0

. /lib/lsb/init-functions

case "$1" in
	start)
		log_daemon_msg "Starting Noip daemons"
		
		install -o $ISPUSER -m 755 -d $LOGDIR
		install -o $ISPUSER -m 755 -d $PIDDIR

		log_progress_msg "$ISPTASKCLIENT"
		
		if ! start-stop-daemon --start -b -c $ISPUSER -d $ISPWORKPUB --make-pidfile -p $TCLDPID -x $PHPBIN -- $ISPTASKCLIENT; then
			log_end_msg 1
			exit 1
		fi

		log_end_msg 0
		;;
	stop)
		log_daemon_msg "Stopping Noip daemons"

		log_progress_msg "$ISPTASKCLIENT"
		
		start-stop-daemon --stop --quiet --pidfile $TCLDPID
		
		# Wait a little and remove stale PID file
		sleep 1
		if [ -f $TCLDPID ] && ! ps h `cat $TCLDPID` > /dev/null
		then
			# Stale PID file (nmbd was succesfully stopped),
			# remove it (should be removed by smbd itself IMHO.)
			rm -f $TCLDPID
		fi

		log_end_msg 0

		;;
	restart)
		$0 stop
		sleep 1
		$0 start
		;;
	*)
		echo "Usage: /etc/init.d/noip {start|stop|restart}"
		exit 1
		;;
esac

exit 0
