<!-- <html>
<body onload="runAnimations()">
	
	<div class="countup">{{ message }}</div>

	<script src="static/myScripts.js"></script>
</body>
</html> -->
<html>

	<head>
		<meta charset="utf-8">
			<head><meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Sigma Auto Estimator</title>
		<link rel= "stylesheet" type= "text/css" href= '/static/resultsStyle.css'>
		<script src="https://kit.fontawesome.com/df9ac4551a.js" crossorigin="anonymous"></script>
	</head>

	<body onload="runAnimations()">
		
		<div class="main-nav">
			<a href="/"><img class="logo" src="static/images/sigmaLogoLong.png"></a>
			
			<li><a href=""> RELIABILITY </a></li>
			<li><a href=""> CONTACT </a></li>
			<li><a href=""> ABOUT US </a></li>
			<li><a href=""> OUR MODEL </a></li>
		</div>

		<div class = "valLabel"> TRUE VALUE </div>
		
		<div class = "resultsSection">
			<div class = "resultsBlock">
				<div class="dollarSign">$</div>
				<div class="countup">{{ message }}</div>
			</div>
		</div>

		<div class = "aboutSection">
			<h1 class="aboutTit">About Us</h1>
			<div class="intro">
				&emsp;The purpose of the project is to build a machine learning model that can accurately estimate the prices of used cars. It is hypothesized that a six layered Artificial Neural Network (ANN) run under 1000 epochs will be significantly more accurate at predicting used car prices. <br><br>&emsp;A variety of factors such as miles driven, year, make, model, and components contribute to a car's price. Multiple machine learning (ML) algorithms could be employed to determine a vehicle’s market value. ML is branch of artificial intelligence in which data and algorithms are used to simulate human learning (Radiša et al., 2015). ML has become the forefront of scientific inquiry for the last decade due to its variety of applications from predicting building energy consumption (Radiša et al., 2015) to aiding in chronic disease diagnosis (Battineni et al., 2020). Researchers must apply different models to find which work best to tackle today's challenges (Diller et al., 2019). ML algorithms can assist retail traders gain an accurate estimate of their car's value, allowing for greater transparency in automotive trading. </div>
			<a class = "fileDownload" href="/static/projectSummary.pptx" download="project">
				<img width = "20%" src="/static/images/fileFolder.svg">
				<div class="figDesc">Download the Project Description Above</div>
			</a>
			
		</div>

		<div class = "bottomReference">
			<h3 class = "aboutUs">CREATED BY SATYA SHAH<br>THE SCIENCE AND MATH ACADEMY<br><br>FEBRUARY 27, 2022</h3>
			<!-- <h3 class = "minorLinks"><a href="/">OUR MODEL</a><br>RELIABILITY<br>ABOUT US<br>CONTACT US</h3> -->
			<h3 class = "thanks">MENTORED BY JARICK CAMMARATO<br><br>SPECIAL THANKS TO YVONNE GABRIEL</h3>
		</div>
			
		<script src="static/myScripts.js"></script>
	</body>

</html>

