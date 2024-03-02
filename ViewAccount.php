<?php

// Connect to your database
$servername = "localhost"; 
$username = "root"; 
$password = ""; 
$dbname = "Person"; 

$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve user data from the database
$sql = "SELECT fullname, email, password, mobile_number FROM Person WHERE id = 1"; // Assuming user_id 1 for demonstration
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $fullName = $row["fullname"];
    $email = $row["email"];
    $password = $row["password"];
    $mobileNumber = $row["mobilenumber"];
} else {
    echo "0 results";
}

$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile Form</title>
</head>
<body>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
<body>
    <header>
        <h1>Aqua Shield</h1>
    </header>
    <nav>
        <a href="index.html">Home</a>
        <a href="UploadDataset.html">Upload Dataset</a>
        <a href="ViewDataset">View Dataset</a>
        <a href="account.html">Account</a>
        <a href="Contact Us.html">Contact Us</a>
        <a href="help.html">Help</a>
    </nav>


    <script>
        function toggleReadOnly() {
            var inputs = document.getElementsByTagName('input');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].type !== 'submit') {
                    inputs[i].readOnly = !inputs[i].readOnly;
                }
            }
        }
    </script>





<main>
    <div class="content">
    <h2>User Profile</h2>
    
    <form action="update_profile.php" method="post">
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" value="<?php echo $fullName; ?>" required><br><br>

        <label for="email">Email</label>
        <input type="email" id="email" name="email" value="<?php echo $email; ?>" required><br><br>

        <label for="password">Password</label>
        <input type="text" id="password" name="password" value="<?php echo $password; ?>" required><br><br>

        <label for="mobileNumber">Mobile Number</label>
        <input type="text" id="mobileNumber" name="mobileNumber" value="<?php echo $mobileNumber; ?>" required><br><br>

        <!-- Toggle edit button 
        <input type="button" value="Edit" onclick="toggleReadOnly()">
--->
        <input type="submit" value="Update Profile">
    </form>
    </div>
</main>

    <footer>
        <p>&copy; 2023 Aqua Shield. All rights reserved.</p>
    </footer>
</body>
</html>

<style>

body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e6f5ff;
          
        }
        header {
            background-color: #0077b5;
            color: #ffffff;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 36px;
        }
        nav {
            background-color: #ffffff;
            border-bottom: 1px solid #dddddd;
            padding: 10px;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
        nav a {
            color: #0077b5;
            text-decoration: none;
            font-size: 20px;
        }
        nav a:hover {
            text-decoration: underline;
        }

        .content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 70%;

        }
        .content h2 {
            font-size: 36px;
            margin-bottom: 20px;
        }
        .content p {
            font-size: 20px;
            margin-bottom: 20px;
        
        }
        footer {
            background-color: #0077b5;
            color: #ffffff;
            padding: 20px;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        footer p {
            margin: 0;
            font-size: 16px;
        }

        main {
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }


    input[type="submit"]  {
        background-color: #0077b5;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        margin-bottom: 50px;
        margin-top: 30px;
        width: 20%;
        margin-right: 80px;

    }

    input[type="submit"] {
        opacity: 0.8;
    }

    .button {
        background-color: #0077b5;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        margin-bottom: 50px;
        margin-top: 30px;
        width: 20%;
        margin-right: 80px;
    }


</style>
