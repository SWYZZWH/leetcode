function f1() {
  echo "$#"
   for i in "$@"; do
     echo 1
   done

   for (( j=0; j < $#; j++ )) do
     echo 2
   done

   echo $1 $2 $3 $4
}



function my_echo() {
    echo 1
}

echo $(f1 "1" "2" "3" "4")
echo $(my_echo "")