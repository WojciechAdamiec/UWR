function fib(n){
    var cache = {0: 0, 1: 1};
    return function aux(n){
        if (cache[n] === undefined){
            cache[n] = aux(n - 1) + aux(n - 2);
        }
        return cache[n];
    }(n);
}

function slow_fib(n){
    if(n == 0) return 0;
    if(n == 1) return 1;
    return slow_fib(n - 1) + slow_fib(n - 2);
}


function count_time(n) {
    console.time("measure");
    console.log('Slow fib: ');
    slow_fib(n);
    console.timeEnd("measure");

    console.log('');
    console.time("measure");
    console.log('Mem fib: ');
    fib(n);
    console.timeEnd("measure");
}

count_time(42);