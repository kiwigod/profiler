set -e

php artisan dusk:test2 &
PID=$!

echo "====="

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    sleep 0.1
done
