import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {

  const [ user, setUser ] = useState('')
  const [errors, setErrors] = useState([]);
  
  const username = 'lightyagami'
  const password = 'password'

  // const API_URL = "https://shoutout-deploy.onrender.com/";
  const API_URL = 'http://127.0.0.1:5000'

  useEffect(() => {
    fetch('https://shoutout-deploy.onrender.com/checksession', {
      // fetch(`http://localhost:5000/checksession`, {
        credentials: 'include'
      })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json()
    })
    .then(data => {
        if (data.session === null) {
            console.log('No active session');
        } else {
            setUser(data);
        }
    })
    .catch(error => console.log('Fetch error:', error));
  }, [])

  const handleLogin = () => {
    fetch('https://shoutout-deploy.onrender.com/login', {
      // fetch(`http://localhost:5000/login`, {
      method: 'POST',
      credentials: 'include',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    }).then((r) => {
        if (r.ok) {
            r.json().then((user) => {
                setUser(user)
            });
        } else {
            // Check if response has content before parsing
            if (r.headers.get('content-length') > 0) {
                r.json().then((err) => {
                    console.log(err);
                    setErrors([err.error]);
                });
            } else {
                // Handle cases where there's no response body
                console.error("No response body");
                setErrors(["An unexpected error occurred"]);
            }
    }}).catch((error) => {
        console.error("Fetch error:", error);
        setErrors(["Network error"]);
    });
  }

  const handleLogout = () => {
    fetch(`https://shoutout-deploy.onrender.com/logout`, {
    // fetch(`http://localhost:5000/logout`, {
      method: "DELETE",
      credentials: 'include'
    })
    .then(() => {
      setUser(null)
    })
  }

  // const handleCheckSession = () => {
  //   fetch('/checksession', {
  //     method: 'GET',
  //     credentials: 'include',
  //   })
  //   .then(response => {
  //       if (!response.ok) {
  //           throw new Error('Network response was not ok');
  //       }
  //       return response.json()
  //   })
  //   .then(data => {
  //       if (data.session === null) {
  //           console.log('No active session');
  //       } else {
  //           console.log(data)
  //           setUser(data);
  //       }
  //   })
  //   .catch(error => console.log('Fetch error:', error));
  // }

  return (
    <div>
      <h1>Test</h1>
      {!user ? 
        <button onClick={handleLogin}>Login</button>
        :
        <button onClick={handleLogout}>Logout</button>
      }
      {!user ?
        <p>Please login</p>
        :
        <p>Welcome {user.first_name}</p>
      }
      {/* <button onClick={handleCheckSession}>CheckSession</button> */}

    </div>
  )
}

export default App;
