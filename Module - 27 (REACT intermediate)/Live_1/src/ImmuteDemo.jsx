import React, { useState } from 'react';
function ImmuteDemo() {
    const [user, setUser] = useState({
        name: 'Alice',
        address: {
            city: 'Wonderland',
            zip: '12345'
        }
    });
    function updateName() {
        const newUser = {
            ...user,
            name: 'Bob'
        };
        setUser(newUser);
        // Alternatively, using functional update
        // setUser(
        //     prev => ({
        //         ...prev,
        //         name: 'Bob'
        //     })
        // )
    }
    return (
        <div>
            <h2>Immute Demo Component</h2>
            <p>Name: {user.name}</p>
            <p>City: {user.address.city}</p>
            <p>Zip: {user.address.zip}</p>
            <button onClick={updateName} >Update Name</button>
        </div>
    );
}

export default ImmuteDemo;