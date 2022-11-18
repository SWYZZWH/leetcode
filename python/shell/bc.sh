v=$(echo "scale=3;10/3" | bc)
echo $v
v2=$(echo "scale=3;c(1.0)" | bc -l)
echo $v2