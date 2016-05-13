<div class="col-md-8" style="text-align: left;">
<div style="font-family:Komoda; font-size:70px;">Kra<img src="img/krawler.png" style="display: inline-block; width: 70px;">ler<sub style="font-size: 35px">pdf</sub></div>
	<form method="GET" action="pdfbase.php">
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
if (empty($output['didyoumean']) && empty($output['results'])) {
	echo "<tr><td><h3>No results found!</h3></tr></td>";
} elseif (!empty($output['didyoumean'])) {
	echo "<tr><td><h3>No results found! Did you mean: <b><a href=\"pdfbase.php?search_term=".$output['didyoumean']."\">".$output['didyoumean']."</a>?</b></h3></tr></td>";
} else {
	foreach ($output['results'] as $result) {
		$title = $result['title'];
		$url = $result['url'];

		echo "<tr><td><h4>$title</h4><p><a href=\"$url\">$url</a></p></td></tr>";
	}
}
?>
		</tbody>
	</table>
</div>
<?php
require_once('trending.php');
?>