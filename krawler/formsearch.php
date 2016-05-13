<div class="col-md-8" style="text-align: left;">
<div style="font-family:Komoda; font-size:70px;">Kra<img src="img/krawler.png" style="display: inline-block; width: 70px;">ler<sub style="font-size: 35px">form</sub></div>
	<form method="GET" action="formbase.php">
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
	echo "<tr><td><h3>No results found! Did you mean: <b><a href=\"formbase.php?search_term=".$output['didyoumean']."\">".$output['didyoumean']."</a>?</b></h3></tr></td>";
} else {
	foreach ($output['results'] as $result) {
		$title = $result['title'];
		$docurl = $result['doc_url'];
		$pdfurl = $result['pdf_url'];

		if (empty($pdfurl)) {
			echo "<tr><td><h4>$title</h4><p>Doc: <a href=\"$docurl\">$docurl</a></p><p>PDF not available!</p></td></tr>";
		} else {
			echo "<tr><td><h4>$title</h4><p>Doc: <a href=\"$docurl\">$docurl</a></p><p>PDF: <a href=\"$pdfurl\">$pdfurl</a></p></td></tr>";
		}
	}
}
?>
		</tbody>
	</table>
</div>
<?php
require_once('trending.php');
?>