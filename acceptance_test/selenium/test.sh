set -e

node main.js &
PID=$!

echo "====="

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    # ps -aux
    # ps -p $PID -o rss=
    sleep 0.250
done
