function fib_i() {
    var cache = [0, 1]
    return {
        next: function () {
            var new_fibb = cache[0] + cache[1];
            cache = [cache[1], new_fibb];
            return {
                    value: cache[1],
                    done: false
            }
        }
    }
}

function* fib_g() {
    var cache = [0, 1];
    while(true){
        yield cache[1];
        var new_fibb = cache[0] + cache[1]
        cache = [cache[1], new_fibb];
    }
}

var _it = fib_i();
for (var _result; _result = _it.next(), !_result.done;) {
    if (_result.value > 100000){
        break;
    }
    console.log(_result.value);
}

var _it = fib_g();
for (var _result; _result = _it.next(), !_result.done;) {
    if (_result.value > 100000){
        break;
    }
    console.log(_result.value);
}

// We can iterate using var-of with our generator
for (var i of fib_g()) {
    if (i > 100000){
        break;
    }
    console.log(i);
}

// We can't iterate using var-of with our iterator
