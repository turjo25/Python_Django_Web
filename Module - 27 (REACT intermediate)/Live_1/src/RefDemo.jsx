import { useRef } from "react";    

function RefDemo() {
    const text = useRef(null);

    function handleClick() {
        // text.current.innerText = "Text changed using useRef!";
        text.current.innerHTML = "<b>Text changed using useRef!</b>";
        text.current.style.color = "red";
    }
    return (
        <div>
            <h2>Ref Demo Component</h2>
            <p ref={text}>Text to be changed</p>
            <button onClick={handleClick}>Change Text</button>
        </div>
    );
}
export default RefDemo;