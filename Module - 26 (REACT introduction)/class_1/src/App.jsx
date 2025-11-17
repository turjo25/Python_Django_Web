import "./App.css";
import New from "./New";
function App() {
  const isUserLoggedIn = true;

  // ------if else evabe likha jabe------
  // if (isUserLoggedIn)
  //   return <New/>
  // else
  //   return <div>Hellow</div>

  return (
    <>
      <div>
        hello world
        <div>{isUserLoggedIn ? <New /> : <></>}</div>
      </div>
    </>
  );
}

export default App;
