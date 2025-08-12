# Advanced JavaScript

## Template Literals

JavaScript **template literals** (also called **template strings**) are a syntax for creating strings that offer more flexibility than regular single (`'`) or double (`"`) quotes. They're enclosed by **backticks** (`` ` ``) and allow for:

### 1. String Interpolation

You can embed variables or expressions directly inside the string using `${...}`.

```javascript
const name = "Alice";
console.log(`Hello, ${name}!`);  // Output: Hello, Alice!
```

### 2. Multi-line Strings

Template literals preserve line breaks automatically.

```javascript
const poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;
console.log(poem);
```

### 3. Expression Evaluation

You can insert any valid JavaScript expression.

```javascript
const a = 5;
const b = 10;
console.log(`The sum is ${a + b}`);  // Output: The sum is 15
```

---

## Spread and Rest Operator (...)

The `...` (three dots) in JavaScript is used in two powerful and related ways:

### 1. Spread Operator

*Expands* elements of an array or object.

#### a. Copying Arrays

```javascript
const arr = [1, 2, 3];
const copy = [...arr]; // [1, 2, 3]
```

#### b. Combining Arrays

```javascript
const a = [1, 2];
const b = [3, 4];
const combined = [...a, ...b]; // [1, 2, 3, 4]
```

#### c. Passing Arguments to Functions

```javascript
const nums = [1, 2, 3];
Math.max(...nums); // Equivalent to Math.max(1, 2, 3)
```

#### d. Copying/Updating Objects

```javascript
const obj = { a: 1, b: 2 };
const newObj = { ...obj, c: 3 }; // { a: 1, b: 2, c: 3 }
```

### 2. Rest Operator

*Collects* multiple elements into an array. Opposite of spread.

#### a. Function Parameters

```javascript
function sum(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}
sum(1, 2, 3); // 6
```

#### b. Destructuring Arrays

```javascript
const [first, ...rest] = [10, 20, 30, 40];
// first = 10, rest = [20, 30, 40]
```

#### c. Destructuring Objects

```javascript
const { a, ...others } = { a: 1, b: 2, c: 3 };
// a = 1, others = { b: 2, c: 3 }
```

---

## Callback Functions

A **callback function** is a **function passed as an argument to another function**, and it's **executed later**.

```javascript
function sayGoodbye() {
  console.log("Goodbye!");
}

function greet(name, callback) {
  console.log("Hello, " + name);
  callback();
}

greet("Alice", sayGoodbye);
// Output:
// Hello, Alice
// Goodbye!
```

Here, `sayGoodbye` is passed to `greet` as a **callback**, and it's executed after the greeting.

---

## Promises

In JavaScript, a **Promise** is a way to handle **asynchronous operations** like fetching data from a server, reading a file, or waiting for a timer.

```javascript
const promise = new Promise((resolve, reject) => {
  // async operation here
});
```

### States of a Promise

1. **Pending** – Initial state, not fulfilled or rejected.
2. **Fulfilled** – The operation completed successfully (`resolve` was called).
3. **Rejected** – The operation failed (`reject` was called).

```javascript
const promise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Operation succeeded!");
  } else {
    reject("Operation failed.");
  }
});
```

### Using `.then()` and `.catch()`

```javascript
promise
  .then(result => {
    console.log(result); // "Operation succeeded!"
  })
  .catch(error => {
    console.error(error); // "Operation failed." (if rejected)
  });
```

#### Real-world Example

```javascript
function getGitHubUser(username) {
  return new Promise((resolve, reject) => {
    fetch(`https://api.github.com/users/${username}`)
      .then(response => {
        if (!response.ok) {
          reject(`GitHub API error: ${response.status}`);
        }
        return response.json();
      })
      .then(data => resolve(data))
      .catch(error => reject(`Network error: ${error.message}`));
  });
}

getGitHubUser("octocat")
  .then(user => {
    console.log("GitHub User Data:", user);
  })
  .catch(err => {
    console.error("Error:", err);
  })
  .finally(() => console.log("Finally: Clean up etc."));
```
