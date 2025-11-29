import React, { useState } from 'react';
import { useParams,useSearchParams } from 'react-router-dom';

function SingleUser() {
    const {id} = useParams();
    const [users, setUsers] = useState([]);
    const [searchParams] = useSearchParams();
    const searchWithQuery = searchParams.get("s");
    console.log("searchWithQuery:", searchWithQuery);
    async function fetchUsers() {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const data = await res.json();
    console.log("users data:", data);
    setUsers(data);
  }
    return (
        <div>
            Single User Page
            <button onClick={async () => await fetchUsers()}>Get user by Id</button>
            {users.name} - {users.email}
        </div>
    )
}
export default SingleUser;