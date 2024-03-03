<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "watertreatment";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$email = $_POST['email'];
$password = $_POST['password'];

// Check if email and password match
$sql = "SELECT * FROM users WHERE email = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    // Authentication successful
    $user = $result->fetch_assoc();
    if (password_verify($password, $user['password'])) {
        session_start();
        $_SESSION['user_id'] = $user['userid'];
        $_SESSION['first_name'] = $user['first_name'];
        $_SESSION['last_name'] = $user['last_name'];
        header('Location: home.html');
    } else {
        echo "Invalid email or password";
    }
} else {
    // Authentication failed
    echo "Invalid email or password";
}

$stmt->close();
$conn->close();
?>