<style>

      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        font-family: Arial, sans-serif;
        background-color: gainsboro;
      }

      form {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #fff;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        width: 30%;
        height: 60%;
      }

      img {
          width: 45%;
          height: 45%;
          margin-top: 30px;
          margin-bottom: 20px;
          border-radius: 50px ;
      }

    
      button {
        padding: 10px 20px;
        background-color: #0077b5;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-bottom: 30px;
        width: 40%;
      }

      button:hover {
        background-color: #0056b3;
      }

</style>

<html>
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
    
  
  <body>
    <form>

    <img src="logo2.png" alt=" Image" />
      <br />

    <button id="myButton">Login</button>
    <script src="script.js"></script>
   <!-- Importing the function from another file -->
      <script>
 // const handleClick = require('./otherFile.js');

// Get the button element
//const button = document.getElementById('myButton');

// Attach click event listener
//button.addEventListener('click', handleClick);
 

//////////

// Importing the function from another file
// const handleLogin = require('./Login.php');

// Get the button element
// const button = document.getElementById('myButton');

// Attach click event listener
//button.addEventListener('click', handleLogin);


      <p> Don't have an account?</p>
      <button type="button" onclick="location.href='signup.php';">Sign Up</button>
      
    </form>
  </body>
</html>


