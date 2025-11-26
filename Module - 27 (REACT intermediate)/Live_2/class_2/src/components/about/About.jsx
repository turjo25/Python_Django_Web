import { useState,useMemo } from "react";
import Contact from "./Contact"

function About() {
    const [arr, setArr] = useState([1,2,3,4,5]);
    const len = useMemo(() => arr.length, [arr]);
    return (
        <div>About Page
        <Contact />
        Length: {len}
        </div>

    )
}
export default About