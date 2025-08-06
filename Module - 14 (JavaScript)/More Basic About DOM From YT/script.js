// let heading = document.getElementById("heading");
// console.dir(heading);

// let headings = document.getElementsByClassName("heading");
// console.dir(headings);

// let paras = document.getElementsByTagName("p");
// console.dir(paras);

// let firstElements = document.querySelector("p");
// console.dir(firstElements);

// let allElements = document.querySelectorAll("p");
// console.dir(allElements);

// let classes = document.querySelectorAll(".heading");
// console.dir(classes);

// let ides = document.querySelectorAll("#btn");
// console.dir(ides);

// console.dir(document.body.lastChild)

// let div = document.querySelector("div").innerText;
// console.dir(div)

// let innerhtml = document.querySelector("div").innerHTML;
// console.dir(innerhtml)


// Some Basic Problem Solving
// let h1 = document.querySelector("h1");
// console.dir(h1.innerText);
// h1.innerText = h1.innerText + " By Mee";

// let classes = document.querySelectorAll(".box");
// console.dir(classes);
// // classes[0].innerText = "Modified";
// // classes[1].innerText = "Modified";
// // classes[2].innerText = "Modified";
// let i = 1;
// for(mod of classes){
//    mod.innerText = `modified ${i}`;
//     i++;
// }

//Attribute 
// let div = document.querySelector("div")
// console.log(div)
// let classes = div.getAttribute("class");
// console.log(classes)

// let para = document.querySelector("p");
// console.log(para);
// console.log(para.setAttribute("class","newpara"));

//Style
// let heading = document.querySelectorAll(".heading");
// console.log(heading);
// heading[0].style.backgroundColor = "red";
// heading[0].style.color = "green";
// heading[0].innerText = "Bangladesh";

// Insert Elements 
// let el = document.createElement("button");
// el.innerText = "Click Me";
// console.dir(el);

// let div = document.querySelector("div");
// // div.append(el);
// // div.prepend(el);
// // div.before(el);
// div.after(el);

//remove element
// document.querySelector("p").remove();

//practice
// let btn = document.createElement("button");
// btn.innerText = "click me";
// btn.style.backgroundColor = "red";
// btn.style.color = "white";
// document.querySelector("body").prepend(btn);

//practice2
// let para = document.querySelector("p");
// para.classList.add("newContent");

//Event Handling
// let btn1 = document.querySelector(".btn1");
// btn1.onclick = () =>{
//     console.log("button is clicked")
// }

//object
// let btn1 = document.querySelector(".btn1");
// btn1.onclick = (evt) =>{
//     console.log(evt.type)
//     console.log("button is clicked")
// }

//addEventListener:
// const handler = () =>{
//     console.log("button clicked")
// }
// let btn1 = document.querySelector(".btn1");
// btn1.addEventListener("click",handler);

// practice(Dark and light mode toggle)
let btn1 = document.querySelector(".btn1");
let body = document.querySelector("body");
const dark = () =>{
    body.style.backgroundColor = "black";
    btn1.style.backgroundColor = "white";
    btn1.style.color = "black";
}
const light = () =>{
    body.style.backgroundColor = "white";
    btn1.style.backgroundColor = "black";
    btn1.style.color = "white";
}
let currMode = "light";
btn1.addEventListener("click",() =>{
    if(currMode === "light"){
        currMode = "dark";
        dark();
    }else{
        currMode = "light";
        light();
    }
    console.log(currMode);
});



