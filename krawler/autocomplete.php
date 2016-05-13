<?php
require_once('conn.php');

$search_term = $_GET['term'];
$query = "SELECT value FROM dictionary WHERE value LIKE '$search_term%';";
$result = $conn->query($query);
$output = array();

while ($row = $result->fetch_assoc()) {
	$rowvalue['value'] = $row['value'];
	array_push($output, $rowvalue);

	if (count($output) > 7) {
		break;
	}
}

print json_encode($output);
