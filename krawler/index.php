<!DOCTYPE html>
<?php
require_once('conn.php');

if (!empty($_GET['search_term'])) {
	$search_term = $_GET['search_term'];

	// The actual search operation.
	$cmdstr = "python /opt/lampp/htdocs/web/python/searcher.py ".$search_term;

	$command = escapeshellcmd($cmdstr);
	$result = shell_exec($command);
	$output = json_decode($result, true);

	if (!empty($output['didyoumean'])) {
		$didyoumean = $output['didyoumean'];
	} else {
		// Check if this value has been searched before.
		$checkQuery = "SELECT * FROM trending WHERE word='$search_term';";
		$checkResult = $conn->query($checkQuery);

		if (!empty($checkResult) && $checkResult->num_rows > 0) {	// Means that this word has been searched before.
			$row = $checkResult->fetch_assoc();
			$freq = $row['freq'];
			$freq++;
			$updateQuery = "UPDATE trending SET freq=$freq WHERE word='$search_term';";
			$conn->query($updateQuery);
		} elseif (!empty($output['results'])) {							// If word has not been searched before.
			$insertQuery = "INSERT INTO trending(freq, word) VALUES(1, '$search_term');";
			$conn->query($insertQuery);
		}
	}

	//var_dump($output);
}

?>
<html>
<head>
	<title>Krawler</title>
	<link rel="icon" type="image/png" href="img/krawler.png">

	<link rel="stylesheet" type="text/css" href="css/custom.css">
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/redmond/jquery-ui.css">

	<style type="text/css">
		@font-face {
    		font-family: Komoda;
    		src: url("fonts/Komoda.otf");
		}
	</style>
</head>
<body>
<?php
require_once('sidebar.php');

if (empty($_GET['search_term'])) {
	require_once('nosearch.php');
} else {
	require_once('search.php');
}
?>
	</div>
</div>
</div>
</div>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>
<script type="text/javascript">
	$(function() {
		$("#search_term").autocomplete({
			source: "autocomplete.php",
			minLength: 3
		});
	});

	$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();      
    });

    function hamburger_cross() {

      if (isClosed == true) {          
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {   
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });  
});
</script>
</body>
</html>