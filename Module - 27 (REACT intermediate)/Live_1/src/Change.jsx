import { useState } from 'react';
function Change() {
    //using useState hook
    let [x, setX] = useState(0);
    function handleChange() {
        setX(x + 1);
        console.log(x);
    }
    function handleChange2() {
        setX(x - 1);
        console.log(x);
    }
    return (
        <div>
            <h2>Change Component</h2>
            <p>{x}</p>
            <button onClick={handleChange}>Increment</button>
            <button onClick={handleChange2}>Decrement</button>
        </div>
    );
}

export default Change;