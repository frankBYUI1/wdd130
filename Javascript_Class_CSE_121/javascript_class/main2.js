// Comparisons

console.log(5 >= 5 && 6 == '6')

// Conditionals

let yourAge = 20;

console.log(yourAge >= 18);

if (yourAge >= 18) {
    console.log('You can vote');
} else {
    console.log('You cannot vote');
}

// Switch
let grade = "A";
let gpaPoints = 0;
switch (grade) {
  case "A":
    gpaPoints = 4;
    break;
  case "B":
    gpaPoints = 3;
    break;
  case "C":
    gpaPoints = 2;
    break;
  case "D":
    gpaPoints = 1;
    break;
  case "F":
    gpaPoints = 0;
    break;
  default:
    gpaPoints = null;
}

console.log(gpaPoints);

if (yourAge < 5){
    console.log('not in school or preschool');
} else if (yourAge <=18 ) {
    console.log('in secondary school');
} else {
    console.log('could be in college');
}

let num = Math.random();

if (num > .5) {
    console.log('heads')
} else {
    console.log('tails')
}

flip(5);

