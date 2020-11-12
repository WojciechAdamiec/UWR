function recur(n){
    if (n == 0){
        return 0;
    }
    if (n == 1){
        return 1;
    }
    return recur(n - 1) + recur(n - 2);
}

function iter(n){
    if (n == 0){
        return 0;
    }
    if (n == 1){
        return 1;
    }
    var first = 0;
    var second = 1;
    var aux = first + second;

    for (var j = 2; j < n; j++){
        first = second;
        second = aux;
        aux = first + second;
    }
    return aux;
}

for (var x = 10; x < 1000; x++){
    console.log("======================");
    console.log("Number: ", x);
    console.log("");
    console.time("Iter time");
    var a = iter(x);
    console.timeEnd("Iter time");
    console.time("Recur time");
    var b = recur(x);
    console.timeEnd("Recur time");
    console.log("");
}

/*
Wykonanie wersji w trybie 'iter' jest szybsze w Chrome o jakieś 10-20% niż w node.js;
Wykonanie wersji w trybie 'recur' jest zdecydowanie szybsze w node.js niż w Chrome;
Wykonanie wersji w trybie 'recur' jest żałośnie wolne w Firefox;
Wykonanie wersji w trybie 'iter' jest najwolniejsze w Firefox;
*/
