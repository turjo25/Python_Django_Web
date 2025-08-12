//Topic 1
//spread
// const a =[1,2];
// const b =[3,4];
// const combined = [...a,...b];
// console.log(combined);

// const obj = {
//     a:1,
//     b:2
// }
// const newObj = {
//     ...obj,
//     c:3
// }
// console.log(newObj); //combined obj+newvalue
//rest
// function sum(...numbers){
//     return numbers.reduce((total,n) => total+n,0);
// }
// sum(1,2);
// sum(1,2,3,4,5); //multiple parameter handle korte parbe
//value list akare jabe and list er akta operation hocce reduce
// const [first,...rest] = [1,2,3,4,5];
//first = 1, rest = [2,3,4,5]
//same as objcet

//callback
// function sayGoodbye() {
//   console.log("Goodbye!");
// }
// function greet(name, callback) {
//   console.log("Hello, " + name);
//   callback();
// }
// greet("Alice", sayGoodbye);

//Promise
//line by line operation - synchonous operation
//parallely onkgula operation aksthe chalano - asynchronous operation
//kokhn lagbe -server theke data fetch, reading a file, waiting for a timer
//backend theke data antese pashapashi ui o load hocce
//1.pending: backend er response er jonne wait kortese
//2.Fulfilled: backend theke data successfully data ashce
//3.Rejected: jode kono karon e data ante na pare tahole rejected
//promise function e must 2 ta parameter thakbe. akta resolve and arekta reject
const promise1 = new Promise((resolve,reject) =>{
    const success = false;
    if(success){
        resolve("Operation successful")//callback function
    }else{
        reject("Operation failed")//callback function
    }
}); 
promise1
.then(result => {console.log(result)})//jode success hoy tahole eita call hobe
.catch(res => {
    console.log(res);
})//jode error hoy tahole eita call hobe

//real example
let promise2 = new Promise((resolve,reject)=>{
    fetch(`https://api.github.com/users/otocat`)//promise er akta function ja data fetch kore
    .then((response)=> resolve(response.json()))//fetch success hole eita
    .catch((error)=> reject(`Network error: ${error.message}`));//unsuccess hole eita
})
promise2
.then((user)=>{
    console.log("github user data:",user);//success hole user info dekhabe
})
.catch((err)=>{
    console.log("Error:",err);//unsuccess hole error msg dekhabe
})