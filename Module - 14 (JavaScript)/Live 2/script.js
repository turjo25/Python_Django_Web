//array and array functions
// const shoppingList = ["milk","bread","egg"];
// shoppingList.push("butter");
// shoppingList.pop();
// console.log(shoppingList);


//Map in Js
// -> akta akta item dhore niye ashe 
// const quantities = [2,3,4];
//and i want to double the amount
//first map function arekta function nibe. r oi fucntion ta hbe quantities double korar
// function dbl(item){
//     return item*2;
// }
//then the double function then pass in the map
// const doubleQantities = quantities.map(dbl);
//using arrow function
// const doubleQantities = quantities.map(item => item*2);
// console.log(doubleQantities);


//Object
//js object == python dictionary
// let student = {
//     name: "Turjo",
//     age:22,
//     nationality:"Bangladeshi",
//     city:"Fardipur"
// }
// console.log(student);
// console.log(student["name"]);
// //we can modify
// student.name = "Turjo Rahman";
// console.log(student.name);

//DOM
//browser html pore then shbkicu document object er moddhe rejhe dey
//eventlistener
// let hiDiv = document.querySelector("h1");
// hiDiv.addEventListener("mouseover",(e) => {
//     hiDiv.textContent = "Bye";
// });

// hiDiv.addEventListener("mouseleave",(e) => {
//     hiDiv.textContent = "HI";
// });


//setTimeout and seInterval
function nice(){
    console.log(new Date);
}
// console.log("Started...");
// setTimeout(nice,1000*2);
//bujhar khetre 1000 er sthe gun diye likha hoy cz 1s = 1000ms;
// setInterval(nice,1000*1);
// 1 sec por por time show korbe

//clearTimeout and clearInterval

// console.log("Started...");
// const tid = setTimeout(nice,1000*2);
// document.querySelector("button").addEventListener("click",(e)=>{
//     clearTimeout(tid);
// })//timeout cancel hoye jabe
 
console.log("Started...");
const tid = setInterval(nice,1000*1);
document.querySelector("button").addEventListener("click",(e)=>{
    clearInterval(tid);
})//interval cancel hoye jabe