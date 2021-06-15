/***Commented code***/
/*
eating(dudley).
*/
eating(harry).

happy(aunt_petunia) :- happy(dudley).
happy(uncle_vernon) :- happy(dudley), unhappy(harry).
happy(dudley) :- kicking(dudley,harry).
happy(dudley) :- eating(dudley).
/*The following added line is a rule for making harry unhappy*/
unhappy(harry) :- kicking(dudley,harry). 

/***Commented code***/
/* 
kicking(dudley,ron).
unhappy(ron).
*/

kicking(dudley,ron).
/***Commented code***/
/*
unhappy(harry).
*/