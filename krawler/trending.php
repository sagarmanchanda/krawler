<div class="col-md-3 col-md-offset-1">
			<br><br><br><br><br>
			<h2 style="text-align: center; color:red; font-family: Komoda; font-size: 70px">Hot Searches</h2><br>
			<ul class="list-group">
<?php
$cacheQuery = "SELECT * FROM trending ORDER BY freq DESC LIMIT 5;";
$cacheResult = $conn->query($cacheQuery);

if (!empty($cacheResult)) {
	while($row = $cacheResult->fetch_assoc()) {
		echo "<li style=\"font-size: 20px\" class=\"list-group-item\"><span style=\"color: orange;\" class=\"glyphicon glyphicon-fire\"></span>  <a href=\"index.php?search_term=".$row['word']."\">".$row['word']."</a></li>";
	}
}
?>
</ul>
		</div>