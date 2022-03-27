console.log((![] + [])[+[]]
        + (![] + [])[+!+[]]
        + ([![]] + [][[]])[+!+[] + [+[]]]
        + (![] + [])[!+[] + !+[]]);

/*
Dzielimy całe wyrażenie na cztery grupy i analizujemy każdą z nich osobno:
1. ![] + [] to 'false', +[] to 0, [0] to pierwszy indeks, więc mamy 'f'
2. ![] + [] to 'false', +[] to 0, !+[] to true, +!+[] to zmiana true na 1, [1] to drugi indeks, więc mamy 'a'
3. [![]] + [][[]] daje nam [false] + 'undefined co daje 'falseundefined'. [+!+[] + [+[]]] to '10', dziesiąty indeks to 'i'
4. ![] + [] to 'false'; !+[] + !+[]] to 2, trzeci indeks to 'l'
dostajemy więc 'fail'
*/
