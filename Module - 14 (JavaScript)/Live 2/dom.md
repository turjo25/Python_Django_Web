# Some Js Basics
- add script before the ending of body tag
- alert tag: website kholar sthe e akta pop up dibe. jotokhn na pop up message jabe totokhn code execute hbe na
- to link js file to html: 
```
<script src="script.js">
</script>
```
# DOM
- Document Object Model
- html er shb code js er moddhe document er under e object hishebe thake
- ei object gulo ke print koranor jonne amra use kori:
```
console.dir(document);
```
- evabe amra html er code js e print korte pari object hishebe
```
console.dir(document.head);
console.dir(document.body);
```
- egula tkhn e lage jkhn amra html page er upor kono buttom click ba ei related kono kaj korte chai
- this is called dynamic manipulation

# DOM Manipulation
- selecting with id:
```
let heading = document.getElementById("heading");
console.dir(heading);
```
- selecting with class:
```
let headings = document.getElementsByClassName("heading");
console.dir(headings);
```
- eita akta html collection return korbe. eita array er moto behave kore. index 0 theke shuru hoy array er moto e access kora jay index diye.
- selecting with tag name: (shb tag er nam diye select korte parbo)
```
let paras = document.getElementsByTagName("p");
console.dir(paras);
```

## Query Selector
- ei selector e id,class,tag any of one pass korte parbo.
- selector niye bujhe nibe konta ki
- example: amar jde shb paragraph er first paragraph ta lage tahole:
```
let firstElements = document.querySelector("p");
console.dir(firstElements);
```
- example: amar jde shb paragraph tag lage tahole:
```
let allElements = document.querySelectorAll("p");
console.dir(allElements);
```
- eita akta node list return korbe
- class jde dite chai tahole `(.)`diye shuru korte hbe:
```
let classes = document.querySelectorAll(".heading");
console.dir(classes);
```
- id jde dite chai tahole `(#)` diye shuru korte hbe:
```
let ides = document.querySelectorAll("#heading");
console.dir(ides);
```

## Properties
`tagName:` returns tag for element nodes
```
<- firstElements.tagName
-> 'P'
```
`innerText:` returns the text content of the element and all its children. mane kono node er child node thakle tar o shb innerText ashbe
```
let div = document.querySelector("div").innerText;
console.dir(div)
```
`innerHTML:` jde text er sthe amra tag gulo o dekhte chai tahole innerHTML use korbo
```
let innerhtml = document.querySelector("div").innerHTML;
console.dir(innerhtml)
```
> Difference between `innerHTML` and `innerText`:<br>
`innerHTML:` Text with HTML tags<br>
`innterText:` Only Raw Text

`innerContent:` innerText er moto e kaj kore kintu eita hidden element er text o show korate pare

> We can change in js of our html properties value by selecting that tag or text:<br>
`document.querySelector("div").innerText = "chages"`
<br>

> How to change any property:
<br>
`First: access the element` <br>
`Second: select property` <br>
`then change what should be`


# Some Important notes

`Document: children property->`  The read-only children property returns a live HTMLCollection which contains all of the child elements of the document upon which it was called.
```
<- document.querySelector("body").children
-> HTMLCollection(7) [h1.heading, h2.heading, h4.heading, p, p, button#btn, script, btn: button#btn]
```
- `firstChild:` The read-only firstChild property of the Node interface returns the node's first child in the tree, or null if the node has no children.
- `lastChild:` The read-only lastChild property of the Node interface returns the last child of the node, or null if there are no child nodes.
- Any property: if we select any node the,
firstChild -> text
then comes -> comments
lastChild -> elements (ei elemnts ei amra shb kaj kori) > they are all siblings in relation

## Attributes
`getAttribute(attr):` to get attribute value
```
let div = document.querySelector("div")
console.log(div)
let classes = div.getAttribute("class");
console.log(classes)
```
`setAttribute(attr,value):` to set the attribute value
```
let para = document.querySelector("p");
console.log(para);
console.log(para.setAttribute("class","newpara"));
```

## Style
- we can add style by selecting perticular node
```
let heading = document.querySelectorAll(".heading");
console.log(heading);
heading[0].style.backgroundColor = "red";
heading[0].style.color = "green";
```
## Insert Elements
- First we need to create element
```
let el = document.createElement("button");
el.innerText = "Click Me";
```
- Then we need to select where we want to append that item and then add it
```
let div = document.querySelector("div");
div.append(el);-> add the end of the node(inside)
div.prepend(el);-> add the start of the node(inside)
div.before(el);-> add before the node(outside)
div.after(el);-> add after the node(outside)
```
- we can also delete any element
```
document.querySelector("p").remove();
```
>`classList:` we can add new class within a class. classlist only adds new class not overwrite the previous like `setAttribute`.
```
let para = document.querySelector("p");
para.classList.add("newContent");
para.classList.remove("newContent");
```

# Event Handling in JS
## Inline event handling
- kono button ba kono keypress kore jde code e kono change ante chai tahole ei event handle kore kora jay
- There are a lot of events
- let's start:
>`onclick=""` -> eita button er moddhe akta attribute ja click korle ki change hobe ta define kore,
```
<button onclick="console.log('button clicked')">Click Me!</button>
```
>`ondblclick=""` -> eita button er moddhe akta attribute jake 2 bar click korle ki change hobe ta define kore.
```
<button ondblclick="console.log('button clicked 2x')">Click Me 2 times!</button>
```
>`onmouseover=""` -> eita button er moddhe akta attribute jar upor hover korle ki change hobe ta define kore.
```
<div onmouseover = "console.log('insdie div')">
        this is a div
    </div>
```
## In Js-file event handling
- we can handle event like this:<br>
node.event = () => {
    //anything to do
}
<br>
Example:<br>

```
let btn1 = document.querySelector(".btn1");
btn1.onclick = () =>{
    console.log("button is clicked")
}
```
> JS file e event handling priority > Inline event handling priority<br>

> ekta event akbar e handle korbo. multiple time likhle shbar sesh e jake likha hbe shudhu shey e kaj korbe. mane override hobe.

> this arrow function has its own object. if we add `(e)` this will be a object of that arrow function. this e has many properties
```
btn1.onclick = (evt) =>{
    console.log(evt.type)
    console.log("button is clicked")
}
```

## More Advance way of handling events(addEventListener)
- node.addEventListener(event,function to be executed);
- node.removeEventListener(event,function to be executed);
```
const handler = () =>{
    console.log("button clicked")
}
let btn1 = document.querySelector(".btn1");
btn1.addEventListener("click",handler);
```
