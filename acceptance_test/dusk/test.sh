set -e

php artisan dusk:test2 &
PID=$!

echo "====="

while ps -p $PID > /dev/null
do
    ps -e -o pcpu,rss,args
    # ps -aux
    # ps -p $PID -o rss=
    sleep 0.250
done
