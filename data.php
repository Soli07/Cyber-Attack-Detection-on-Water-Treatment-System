<?php
// Establish database connection (replace with your credentials)
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
// SQL query to fetch all columns from the table
$sql = "SELECT * FROM sensors_data";
$result = $conn->query($sql);

// Initialize the PHP array to store the values of all columns
$rows = [];
$Timestamp =[];
$FIT101 = [];
$LIT101 = [];
$MV101 = [];
$P101 = [];
$P102 = [];
$AIT201 = [];
$AIT202 = [];
$AIT203 = [];
$FIT201 = [];
$MV201 = [];
$P201 = [];
$P202 = [];
$P203 = [];
$P204 = [];
$P205 = [];
$P206 = [];
$DPIT301 = [];
$FIT301 = [];
$LIT301 = [];
$MV301 = [];
$MV302 = [];
$MV303 = [];
$MV304 = [];
$P301 = [];
$P302 = [];
$AIT401 = [];
$AIT402 = [];
$FIT401 = [];
$LIT401 = [];
$P401 = [];
$P402 = [];
$P403 = [];
$P404 = [];
$UV401 = [];
$AIT501 = [];
$AIT502 = [];
$AIT503 = [];
$AIT504 = [];
$FIT501 = [];
$FIT502 = [];
$FIT503 = [];
$FIT504 = [];
$P501 = [];
$P502 = [];
$PIT501 = [];
$PIT502 = [];
$PIT503 = [];
$FIT601 = [];
$P601 = [];
$P602 = [];
$P603 = [];
$Normal_Attack = [];

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
	$rows[] = $row['MV201'];
	$Timestamp[] = $row['Timestamp'];
    $FIT101[] = $row['FIT101'];
    $LIT101[] = $row['LIT101'];
    $MV101[] = $row['MV101'];
    $P101[] = $row['P101'];
    $P102[] = $row['P102'];
    $AIT201[] = $row['AIT201'];
    $AIT202[] = $row['AIT202'];
    $AIT203[] = $row['AIT203'];
    $FIT201[] = $row['FIT201'];
    $MV201[] = $row['MV201'];
    $P201[] = $row['P201'];
    $P202[] = $row['P202'];
    $P203[] = $row['P203'];
    $P204[] = $row['P204'];
    $P205[] = $row['P205'];
    $P206[] = $row['P206'];
    $DPIT301[] = $row['DPIT301'];
    $FIT301[] = $row['FIT301'];
    $LIT301[] = $row['LIT301'];
    $MV301[] = $row['MV301'];
    $MV302[] = $row['MV302'];
    $MV303[] = $row['MV303'];
    $MV304[] = $row['MV304'];
    $P301[] = $row['P301'];
    $P302[] = $row['P302'];
    $AIT401[] = $row['AIT401'];
    $AIT402[] = $row['AIT402'];
    $FIT401[] = $row['FIT401'];
    $LIT401[] = $row['LIT401'];
    $P401[] = $row['P401'];
    $P402[] = $row['P402'];
    $P403[] = $row['P403'];
    $P404[] = $row['P404'];
    $UV401[] = $row['UV401'];
    $AIT501[] = $row['AIT501'];
    $AIT502[] = $row['AIT502'];
    $AIT503[] = $row['AIT503'];
    $AIT504[] = $row['AIT504'];
    $FIT501[] = $row['FIT501'];
    $FIT502[] = $row['FIT502'];
    $FIT503[] = $row['FIT503'];
    $FIT504[] = $row['FIT504'];
    $P501[] = $row['P501'];
    $P502[] = $row['P502'];
    $PIT501[] = $row['PIT501'];
    $PIT502[] = $row['PIT502'];
    $PIT503[] = $row['PIT503'];
    $FIT601[] = $row['FIT601'];
    $P601[] = $row['P601'];
    $P602[] = $row['P602'];
    $P603[] = $row['P603'];
    $Normal_Attack[] = $row['Normal_Attack'];
    }
	
} else {
    echo "0 results"; // Initialize the PHP array with a default value if there are no rows
}

// Close the database connection
$conn->close();
?>