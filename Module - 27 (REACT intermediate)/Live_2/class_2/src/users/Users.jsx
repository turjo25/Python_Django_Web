import { use, useState } from "react";

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  async function fetchUsers() {
    setLoading(true);
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await res.json();
    console.log("users data:", data);
    setUsers(data);
    setLoading(false);
  }

  //using promise- (not recommended)
  //   function fetchUsersWithPromise() {
  //     setLoading(true);
  //     fetch("https://jsonplaceholder.typicode.com/users")
  //       .then((res) => res.json())
  //       .then((setUsers))
  //       .finally(() => setLoading(false));
  //   }

  return (
    <div>
      <h2>Users Page</h2>
      <button onClick={async () => await fetchUsers()}>Fetch Users</button>
      {loading && <p>Loading...</p>}
      {users.map((user) => (
        <div key={user.id}>
          {user.name} - {user.email}
        </div>
      ))}
    </div>
  );
}

export default Users;
