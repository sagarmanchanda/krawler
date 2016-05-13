<div class="col-md-8" style="text-align: left;">
<div style="font-family:Komoda; font-size:70px;">Kra<img src="img/krawler.png" style="display: inline-block; width: 70px;">ler<sub style="font-size: 35px">Image</sub></div>
	<form method="GET" action="imagebase.php">
	<br>
	<div class="row">
		<div class="col-md-8">
			<input class="form-control" type="text" id="search_term" name="search_term" placeholder="Search">
		</div>
		<div class="col-md-4">
			<input value="Search" type="submit" class="button_example"></input>
		</div>
	</div>
	</form><br>

	<table class="table table-hover">
		<thead></thead>
		<tbody>
<?php
if (empty($output['didyoumean']) && empty($output['images'])) {
	echo "<tr><td><h3>No results found!</h3></tr></td>";
} elseif (!empty($output['didyoumean'])) {
	echo "<tr><td><h3>No results found! Did you mean: <b><a href=\"imagebase.php?search_term=".$output['didyoumean']."\">".$output['didyoumean']."</a>?</b></h3></tr></td>";
} else {
	foreach ($output['images'] as $result) {
		$title = $result['title'];
		$imageurl = $result['image-url'];
		$pageurl = $result['page-url'];

		echo "<tr><td><a href=\"$imageurl\"><img src=\"$imageurl\" onError=\"this.src='img/default.png';\" style=\"height:150px; max-width: 300px;\"></a></td><td><h4>$title</h4><p><a href=\"$imageurl\">Visit Image</a></p><p><a href=\"$pageurl\">Visit Page</a></p></td></tr>";
	}
}
?>
		</tbody>
	</table>
</div>
<?php
require_once('trending.php');
?>