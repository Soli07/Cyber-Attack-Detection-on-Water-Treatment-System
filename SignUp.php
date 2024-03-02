<?php

// Database credentials
$servername = "localhost"; // Change this to your server name
$username = "root"; // Corrected the typo
$password = ""; // Change this to your database password
$dbname = "Person"; // Change this to your database name


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Define variables and initialize with empty values
$full_name = $email = $password = $mobile_number = "";
$full_name_err = $email_err = $password_err = $mobile_number_err = "";



// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
  // Validate Full Name
  if (empty(trim($_POST["full_name"]))) {
      $full_name_err = "Please enter your full name.";
  } else {
      $full_name = trim($_POST["full_name"]);
  }
  
  // Validate Email
  if (empty(trim($_POST["email"]))) {
      $email_err = "Please enter an email.";
  } else {
      // Check if email is valid
      if (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
          $email_err = "Invalid email format.";
      } else {
          $email = trim($_POST["email"]); 
      }
  }
  
  // Validate Password
  if (empty(trim($_POST["password"]))) {
      $password_err = "Please enter a password.";     
  } elseif (strlen(trim($_POST["password"])) < 6) {
      $password_err = "Password must have at least 6 characters.";
  } else {
      $password = trim($_POST["password"]);
  }

  // Validate Mobile Number
  if (empty(trim($_POST["mobile_number"]))) {
      $mobile_number_err = "Please enter your mobile number.";
  } else {
      // Check if mobile number is valid
      if (!preg_match("/^[0-9]{10}$/", $_POST["mobile_number"])) {
          $mobile_number_err = "Invalid mobile number format.";
      } else {
          $mobile_number = trim($_POST["mobile_number"]);
      }
  }
  
  // Check for input errors before inserting into database
  if (empty($full_name_err) && empty($email_err) && empty($password_err) && empty($mobile_number_err)) {
      // Here you would typically insert the user into your database
      // For demonstration purposes, let's just echo the inputs
      echo "Full Name: " . $full_name . "<br>";
      echo "Email: " . $email . "<br>";
      echo "Password: " . $password . "<br>";
      echo "Mobile Number: " . $mobile_number;
  }
}

?>


<html>

<body>

<h2>Modal Signup Form</h2>

<button onclick="document.getElementById('id01').style.display='block'" style="width:auto;">Sign Up</button>

<div id="id01" class="modal">
  <span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close">&times;</span>
  <form class="modal-content" action="/action_page.php" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
    <div class="container">
      <h1>Sign Up</h1>
      <p>Please fill in this form to create an account.</p>
      <hr>
      <label for="fullname"><b>Full Name</b></label>
      <input type="text" placeholder="Full Name" name="full_name" required value="<?php echo $full_name; ?>">
      <span><?php echo $full_name_err; ?></span>
      
      <label for="email"><b>Email</b></label>
      <input type="text" placeholder="Enter Email" name="email" required value="<?php echo $email; ?>">
      <span><?php echo $email_err; ?></span>


      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="password" required value="<?php echo $password; ?>">
      <span><?php echo $password_err; ?></span>
    

      <label for="mobileno"><b>Mobile Number</b></label>
      <input type="text" placeholder="Mobile Number" name="mobile_number" required value="<?php echo $mobile_number; ?>">
      <span><?php echo $mobile_number_err; ?></span>
 
      <label>
        <input type="checkbox" checked="checked" name="remember" style="margin-bottom:15px"> Remember me
      </label>

      <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

      <div class="clearfix">
        <button type="submit" class="signupbtn">Sign Up</button>
        <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
        
      </div>
    </div>
  </form>
</div>

<script>
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>

</body>
</html>


<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

/* Add a background color when the inputs get focus */
input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for all buttons */
button {
  background-color: #0077b5;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

button:hover {
  opacity:1;
}

/* Extra styles for the cancel button */
.cancelbtn {
  padding: 14px 20px;
  background-color: #f44336;
}

/* Float cancel and signup buttons and add an equal width */
.cancelbtn, .signupbtn {
  float: left;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #474e5d;
  padding-top: 50px;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 40%; /* Could be more or less, depending on screen size */
}

/* Style the horizontal ruler */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}
 
/* The Close Button (x) */
.close {
  position: absolute;
  right: 35px;
  top: 15px;
  font-size: 40px;
  font-weight: bold;
  color: #f1f1f1;
}

.close:hover,
.close:focus {
  color: #f44336;
  cursor: pointer;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn, .signupbtn {
     width: 100%;
  }
}
</style>
