function createFs(n) {
    var fs = [];
    for (var i = 0; i < n; i++) {
        fs[i] =
            function () {
                return i;
            };
    };
    return fs;
}

var myfs = createFs(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());

function createFs_let(n) {
    var fs = [];
    for (let i = 0; i < n; i++) {
        fs[i] =
            function () {
                return i;
            };
    };
    return fs;
}

var myfs = createFs_let(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());

// Explanation: var works in a scope of a function, let works in a scope of a code block

function createFs_Babel(n) {
    var fs = [];

    for (var i = 0; i < n; i++) {
        (function (i){
            fs[i] = function () {
            return i;
            }
        }(i))
    }
    return fs;
}

var myfs = createFs_Babel(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());

function createFs_Babel_let(n) {
    var fs = [];

    for (let i = 0; i < n; i++) {
        (function (i){
            fs[i] = function () {
            return i;
            }
        }(i))
    }
    return fs;
}

var myfs = createFs_Babel_let(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());

// It still works!