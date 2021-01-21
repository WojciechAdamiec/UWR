function forEach(a, f) {
    for (let i = 0; i < a.length; i++){
        f(a[i]);
    }
}

function map(a, f) {
    for (let i = 0; i < a.length; i++){
        a[i] = f(a[i]);
    }
    return a;
}

function filter(a, f) {
    var ans = []
    for (let i = 0; i < a.length; i++){
        if (f(a[i])){
            ans.push(a[i]);
        }
    }
    return ans;
}

var a = [1, 2, 3, 4];

forEach(a, _ => { console.log(_); });
// [1,2,3,4]

console.log('');
var f = filter(a, _ => _ < 3);
forEach(f, _ => { console.log(_); });
// [1,2]

console.log('');
var m = map(a, _ => _ * 2);
forEach(m, _ => { console.log(_); });
// [2,4,6,8]