# JSON
- List + Dict -> combination
```json
{"hi": "hello"}
{"hi": 5}
{"hi":[1,2,3]}
{{"hi":"hello"},
{"bye":{}}
}
```

# API and Rest API
- Way or interface like a broker
- amar hoye kono akta kaj kore dibe
- Rest API: Rest er kicu rules follow kore API er kaj korle eita rest api
- Rest API json Fetch kore ane
> REST APIs typically use standard HTTP methods (verbs) to perform operations on resources:<br>
<b>GET: Retrieve a resource or a collection of resources.<br>
POST: Create a new resource.<br>
PUT: Update or replace an existing resource.<br>
DELETE: Remove a resource.<br></b>
Clients send requests to specific endpoints (URLs) on the server, and the server responds with a representation of the requested resource or an indication of the operation's success or failure, often in JSON format.
- Json er moddhe thake data
- then js DOM diye data shob change kore dey
- Advantage: html akbar e fetch korbo then baki shob data change kore dibo json diye
> Jshb jinish dynamic shei shb amra alada kore js file e giye handle korbo

# JS Fetch
- kono akta website theke kono info fetch kore niye ashte pari
- For better view the json:
[PostMan](https://www.postman.com/)
- for Dummy Json:
[Dummy JSON]((https://dummyjson.com/todos))
- Js er moddhe kono website er data anar jonne `fetch` tool use kori
- for getting the data:
```javascript
fetch("https://dummyjson.com/todos")
    .then(response => response.json())
    .then( data => {
        console.log(data);
        todos = data.todos;
        showTodoList();
    })
```
- for posting the data:
```javascript
fetch("https://dummyjson.com/todos/add",{//data server e post korte hole method obossoye bole dite hobe
        method: "POST",
        headers:{
            "content-type":"application/json",//eita diye define kora je eita kon type er data hobe 
        },
        body: JSON.stringify()//
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            todos = data.todos;
            showTodoList();
        })
```
- Dummy json theke kivabe data get,post,delete korbo shob bole dewa ache ei website e: [Dummy JSON](https://dummyjson.com/docs/todos)