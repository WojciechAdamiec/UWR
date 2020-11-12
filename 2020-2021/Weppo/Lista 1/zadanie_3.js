
function is_prime(num){
    for(var j = 2; j <= num/2; j++){
        if (num % j == 0){
            return false;
        }
    }
    return true;
}

for (var i = 2; i < 100000; i++){
    if (is_prime(i)){
        console.log(i);
    }
}