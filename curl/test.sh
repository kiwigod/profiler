set -e

php main.php &
PID=$!

echo "====="

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    sleep 0.1
done

# rss and vsz in kib

# /usr/bin/time php main.php
# container creation ts 
# stat /proc/1/cmdline
