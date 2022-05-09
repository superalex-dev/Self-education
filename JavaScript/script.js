let firstname = "Alexander";
let age = 15;
let city = "Sofia";

console.log("Hello,", firstname + "you are", age, "years old" + "you are from", city)

document.getElementById("p1").innerHTML = "Hello " + firstname;
document.getElementById("p2").innerHTML = "You are " + age + "years old";
document.getElementById("p3").innerHTML = "and you are from " + city;
