
function is_ok(num){
    var sum = 0;
    var text = num.toString();
    for(let j = 0; j < text.length; j++){
        sum += parseInt(text[j], 10);
        if (num % parseInt(text[j], 10) != 0){
            return false;
        }
    }
    if (num % sum != 0){
        return false;
    }
    return true;
}

for (var i = 1; i < 100000; i++){
    if (is_ok(i)){
        console.log(i);
    }
}