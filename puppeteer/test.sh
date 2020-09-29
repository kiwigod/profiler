set -e

node main.js &
PID=$!

echo "====="

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    sleep 0.1
done
