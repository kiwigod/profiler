set -e

casperjs main.js &
PID=$!

echo "=====" >> /app/result.log

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    sleep 0.1
done
