import React, { useState } from 'react';
function Fruits() {
    const [fruits, setFruits] = useState(["Apple", "Banana", "Mango"]);
    function addFruit(e) {
        e.preventDefault();
        const newFruit = e.target.newFruits.value; //submit from er name = newFruits er fruit eita
        setFruits([...fruits, newFruit]);
    }

    function deleteFruit(fruitName) {
        const newFruits = fruits.filter(fruit => fruit !== fruitName);
        setFruits(newFruits);
    }

    return (
        <div>
            <h2>Fruits Component</h2>
            {fruits.map((fruit) => (
                <div>{fruit}<button onClick={()=>deleteFruit(fruit)}>Delete</button></div>  //eikhan e arrow function use kora hoise jate click er somoy fruit er value pass kora jai. arrow sara direct function call dilei fruit er array load howar somoy e function call hoye jabe.
            ))}
            <form onSubmit={addFruit}>
                <input type="text" placeholder="Enter fruit name" id="fruitInput" name="newFruits" />
                <button type='submit'>Add Fruit</button> 
            </form>
        </div>
    );
}   
export default Fruits;