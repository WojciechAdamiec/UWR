var test = 'test';
console.log(typeof test); //"string"
console.log(test instanceof String); //false
/*
a) typeof - typ argumentu, w postaci stringu

b) instanceof - czy dany argument jest utworzony okreslonym konstruktorem
*/
const number = new Number(77);
console.log(number instanceof Number); // true
var test2 = {jeden: 'jeden',
             dwa: 1
};
console.log(typeof test2); // object
function Sample(first, second, third) {
    this.first = first;
    this.second = second;
    this.third = third;
  }
const test3 = new Sample('first', 'second', 2020);

console.log(test3 instanceof Sample); // true
console.log(typeof test3); // object
console.log(test3 instanceof Object); // true
