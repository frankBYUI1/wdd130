// trying our console
/* comments for a whole paragraph */
console.log('hi');


console.log(typeof 42);
console.log(typeof "abc");
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof { a: 1 });
console.log(typeof [1, 2, 3]);
console.log(typeof function hello() {});

let adult = true;
let myName = 'Bob';
let age = 24;

if (adult) {
    myName = 'Julie';
    age = 49;
};

console.log(myName);
console.log(age);
console.log(adult);

let variable = 4;

console.log(variable); 

if (adult) {
    myVarable = 6;
    console.log(myVarable);
  };

  let names = ["Bob", "Sue", "Jorge", "Svetlana"];

  console.log(names[2]);

  names[2] = "George";

  console.log(names);
  
  names.push('Grace');

  console.log(names);

  names.pop();
  
  console.log(names); 

let myString = "This is my String!";
console.log(myString.length); // 18

const hello = "Hello";
const world = "World";
const complexString = `${hello} ${world}`; // Backtick is the one before the number "1" on my keyboard


console.log(complexString);

// const myArray = ["one", "two", "three"];
// const htmlString = `
{/* <ol>
  <li>${myarray[0]}</li>
  <li>${myarray[1]}</li>
  <li>${myarray[2]}</li>
</ol>`; */}

// document.querySelector('div').innerHTML = htmlString;

const PI = 3.14;
let radius = 3;
let area = 0;
area = radius * radius * PI;
radius = 4;
area = radius * radius * PI;

