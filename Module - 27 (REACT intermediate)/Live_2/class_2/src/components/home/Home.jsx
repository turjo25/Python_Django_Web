import { use, useState, useEffect } from "react";
function Home() {
  const [count, setCount] = useState(0);

  function increment() {
    setCount(count + 1);
  }
  //   useEffect(() => {
  //     console.log("Home component mounted");
  //     }, []);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  // useEffect(() => {
  //   return () => {
  //     console.log("Home component unmounted");
  //   };
  // });

//   useEffect(() => {
//     const t = setTimeout(search, 300);
//     return () => clearTimeout(t);
//   }, [query]);

  return (
    <div>
      Home Page
      <div>
        <button onClick={increment}>Count: {count}</button>
      </div>
    </div>
  );
}
export default Home;
