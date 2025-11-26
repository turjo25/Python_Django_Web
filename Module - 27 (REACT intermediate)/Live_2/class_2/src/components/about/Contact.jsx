import { useState } from "react";
function Contact() {
  const [error, setError] = useState("");
  const [password, setPassword] = useState("");

  function validatePassword(event) {
    event.preventDefault();
    if (event.target.password.value.length < 6) {
      setError("Password must be at least 6 characters long");
      return false;
    }
    return true;
  }
  function onFinish(event) {
    event.preventDefault();
    if (validatePassword(event)) {
      console.log("pass:", event.target.password.value);
      alert("Form submitted");
    } else {
      console.log("validation failed");
    }
  }
  return (
    <div>
      <form onSubmit={onFinish}>
        <input type="text" placeholder="Your name" />
        <br />

        {/* <input name="password" type="password" placeholder="password"/><br />
                {error && <span style={{ color: 'red' }}>{error}</span>}<br /> */}

        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          name="password"
          type="password"
          placeholder="password"
        />
        <br />
        {password.length > 0 && password.length < 6 && (
          <span style={{ color: "yellow" }}>Password is weak!</span>
        )}
        <br />

        <textarea placeholder="Your message"></textarea>
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default Contact;
