function* fib_g() {
    var cache = [0, 1];
    while(true){
        yield cache[1];
        var new_fibb = cache[0] + cache[1]
        cache = [cache[1], new_fibb];
    }
}

function* take(it, top) {
    for (let i = 0; i < top; i++){
        yield it.next().value;
    }
}

for (let num of take(fib_g(), 10)) {
    console.log(num);
}