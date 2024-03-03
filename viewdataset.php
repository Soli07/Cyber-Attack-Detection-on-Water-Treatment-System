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
	$Timestamp [] = $row['Timestamp'];
	$rows[] = $row['MV201'];
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


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Display</title>
    <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
		.container {
			max-width: 800px;
			margin: 20px auto;
			padding: 20px;
			background-color: #fff;
			border-radius: 8px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			overflow-x: auto; /* Add this line */
		}
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        table th, table td {
            padding: 8px;
            border: 1px solid #ddd;
            text-align: left;
        }
        table th {
            background-color: #f2f2f2;
        }
        h2 {
            margin-top: 0;
        }
		    button {
            background-color: #0077b5;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
			button:hover {
            background-color: #005daa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sensor Data</h2>
        <table>
            <tr>
				<th>Timestamp</th>
                <th>FIT101</th>
                <th>LIT101</th>
                <th>MV101</th>
                <th>P101</th>
                <th>P102</th>
                <th>AIT201</th>
                <th>AIT202</th>
                <th>AIT203</th>
                <th>FIT201</th>
                <th>MV201</th>
                <th>P201</th>
                <th>P202</th>
                <th>P203</th>
                <th>P204</th>
                <th>P205</th>
                <th>P206</th>
                <th>DPIT301</th>
                <th>FIT301</th>
                <th>LIT301</th>
                <th>MV301</th>
                <th>MV302</th>
                <th>MV303</th>
                <th>MV304</th>
                <th>P301</th>
                <th>P302</th>
                <th>AIT401</th>
                <th>AIT402</th>
                <th>FIT401</th>
                <th>LIT401</th>
                <th>P401</th>
                <th>P402</th>
                <th>P403</th>
                <th>P404</th>
                <th>UV401</th>
                <th>AIT501</th>
                <th>AIT502</th>
                <th>AIT503</th>
                <th>AIT504</th>
                <th>FIT501</th>
                <th>FIT502</th>
                <th>FIT503</th>
                <th>FIT504</th>
                <th>P501</th>
                <th>P502</th>
                <th>PIT501</th>
                <th>PIT502</th>
                <th>PIT503</th>
                <th>FIT601</th>
                <th>P601</th>
                <th>P602</th>
                <th>P603</th>
            </tr>
            <?php
            // Loop through the fetched data and output rows
            for ($i = 0; $i < count($FIT101); $i++) {
                echo "<tr>";
				echo "<td>" . $Timestamp[$i] . "</td>";
                echo "<td>" . $FIT101[$i] . "</td>";
                echo "<td>" . $LIT101[$i] . "</td>";
                echo "<td>" . $MV101[$i] . "</td>";
                echo "<td>" . $P101[$i] . "</td>";
                echo "<td>" . $P102[$i] . "</td>";
                echo "<td>" . $AIT201[$i] . "</td>";
                echo "<td>" . $AIT202[$i] . "</td>";
                echo "<td>" . $AIT203[$i] . "</td>";
                echo "<td>" . $FIT201[$i] . "</td>";
                echo "<td>" . $MV201[$i] . "</td>";
                echo "<td>" . $P201[$i] . "</td>";
                echo "<td>" . $P202[$i] . "</td>";
                echo "<td>" . $P203[$i] . "</td>";
                echo "<td>" . $P204[$i] . "</td>";
                echo "<td>" . $P205[$i] . "</td>";
                echo "<td>" . $P206[$i] . "</td>";
                echo "<td>" . $DPIT301[$i] . "</td>";
                echo "<td>" . $FIT301[$i] . "</td>";
                echo "<td>" . $LIT301[$i] . "</td>";
                echo "<td>" . $MV301[$i] . "</td>";
                echo "<td>" . $MV302[$i] . "</td>";
                echo "<td>" . $MV303[$i] . "</td>";
                echo "<td>" . $MV304[$i] . "</td>";
                echo "<td>" . $P301[$i] . "</td>";
                echo "<td>" . $P302[$i] . "</td>";
                echo "<td>" . $AIT401[$i] . "</td>";
                echo "<td>" . $AIT402[$i] . "</td>";
                echo "<td>" . $FIT401[$i] . "</td>";
                echo "<td>" . $LIT401[$i] . "</td>";
                echo "<td>" . $P401[$i] . "</td>";
                echo "<td>" . $P402[$i] . "</td>";
                echo "<td>" . $P403[$i] . "</td>";
                echo "<td>" . $P404[$i] . "</td>";
                echo "<td>" . $UV401[$i] . "</td>";
                echo "<td>" . $AIT501[$i] . "</td>";
                echo "<td>" . $AIT502[$i] . "</td>";
                echo "<td>" . $AIT503[$i] . "</td>";
                echo "<td>" . $AIT504[$i] . "</td>";
                echo "<td>" . $FIT501[$i] . "</td>";
                echo "<td>" . $FIT502[$i] . "</td>";
                echo "<td>" . $FIT503[$i] . "</td>";
                echo "<td>" . $FIT504[$i] . "</td>";
                echo "<td>" . $P501[$i] . "</td>";
                echo "<td>" . $P502[$i] . "</td>";
                echo "<td>" . $PIT501[$i] . "</td>";
                echo "<td>" . $PIT502[$i] . "</td>";
                echo "<td>" . $PIT503[$i] . "</td>";
                echo "<td>" . $FIT601[$i] . "</td>";
                echo "<td>" . $P601[$i] . "</td>";
                echo "<td>" . $P602[$i] . "</td>";
                echo "<td>" . $P603[$i] . "</td>";
                echo "</tr>";
            }
            ?>
        </table>
		
		<a href="simulation.php"><button>Simulate</button></a>

    </div>
</body>
</html>