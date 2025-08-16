let todos = []
const todoList = document.getElementById("todoList");
const taskCount = document.getElementById("taskCount");
const input = document.getElementById("todoInput");


//show in list function
function showTodoList() {
    taskCount.innerHTML = todos.length + " tasks";
    todoList.innerHTML = "";
    for (todoItem of todos) {
        const item = `
    <li class="todo-item ${todoItem.completed ? 'completed' : ''}">
        <div class="todo-checkbox ${todoItem.completed ? 'checked' : ''}"></div>
        <span class="todo-text">${todoItem.todo}</span>
        <button class="delete-btn">x</button>
    </li>
    `
        todoList.innerHTML = item + todoList.innerHTML;
    }
}
showTodoList();

//get data from Form:
const form = document.getElementById("todoForm");
form.addEventListener("submit", (e) => {
    e.preventDefault(); // this function is called to prevent the refresh after clicking the submit button
    const val = input.value;

    //POST data
    const newData = {
        todo: val,
        completed:false,
        userId:5,
    }
    fetch("https://dummyjson.com/todos/add",{//data server e post korte hole method obossoye bole dite hobe
        method: "POST",
        headers:{
            "content-type":"application/json",//eita diye define kora je eita kon type er data hobe 
        },
        body: JSON.stringify(newData)//newData object ta ke string banaye body te rekhe then server e push
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            todos = data.todos;
            showTodoList();
        })

    todos.push(newData);
    showTodoList();
    input.value = "";
})


// data fetch
fetch("https://dummyjson.com/todos")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        todos = data.todos;
        showTodoList();
    })
    .catch(error=>{//error handle kora jay ei catch diye
        console.error(error);
        alert("Something is wrong!");
    })

