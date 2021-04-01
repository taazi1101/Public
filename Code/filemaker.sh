x=1
while true
do
	x=$((1+x))
	echo $x
	echo "" > $1$x.tmp
done
