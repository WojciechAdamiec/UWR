var wizard = {
    gear: 'Magic staff',
    lifespan: 250,
    'spell': 'fireball'
}

var warrior = {
    gear: 'Steel Longsword',
    lifespan: 60,
    1:4,
    toString(){
        return 'Adam';
    }
}

var sword = {
    length: 76,
    damage: 30,
    toString() {
        return 'gear';
    }
}

// 1
console.log(wizard.gear);
console.log(wizard['gear']);
console.log(warrior[sword]); // (X_1)
console.log(warrior[1]);

// 2
sword[1] = 1;
sword[warrior] = '???';
sword[sword] = '!!!';
console.log(sword);
// output: {1: 1, length: 76, damage: 30, toString: ƒ, [object Object]: '???'}

/*
1.
Notacja z kropką: nazwa zmiennej nie moze zaczynac sie od cyfry, nie moze zawierac spacji.
Dodatkowo przy pomocy notacji [] można zrobić to co jest w linijce (X_1).

2.
Dla liczby n zapisze nową właściwość n.
Dla obiektu - zamieni ten obiekt na stringa (toString()) i wykona się jak dla stringa.
Programista może zmienić metodę toString(), żeby działać na odpowiednim kluczu

3.
Napis - zwraca undefined
Obiekt - zwraca undefined
Dopisze to jako właściwość dla tego klucza
Można - odpowiednio skracamy lub zwiększamy (elemntami typu undefined) tablice.
*/

var names = ['Bob', 'Adam', 'Tom', 'Richard'];
console.log(names['Tom']); // undefined
console.log(names[warrior]); // undefined
names['Bob'] = 42;
console.log(names); // [ 'Bob', 'Adam', 'Tom', 'Richard', Bob: 42 ]

var numbers = [1, 2, 3, 4, 5];
numbers.length = 3;
console.log(numbers); // [1, 2, 3]
numbers.length = 7;
console.log(numbers); // [1, 2, 3, undefined, ...]