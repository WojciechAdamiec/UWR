function sum() {
    var acc = 0;
    for (var i = 0; i < arguments.length; i++){
        acc += arguments[i];
    }
    return acc;
}

console.log(sum(1, 2, 3));
// 6
console.log(sum(1, 2, 3, 4, 5));
// 15
