<!DOCTYPE html>
<html>

	<head>
		<meta charset="utf-8">
			<head><meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Sigma Auto Estimator</title>
		<link rel= "stylesheet" type= "text/css" href= '/static/inputsStyle.css'>
		<script src="https://kit.fontawesome.com/df9ac4551a.js" crossorigin="anonymous"></script>
	</head>

	<body>
		
		<div class="main-nav">
			<a href="/"><img class="logo" src="static/images/sigmaLogoLong.png"></a>
			
			<li><a href=""> RELIABILITY </a></li>
			<li><a href=""> CONTACT </a></li>
			<li><a href=""> ABOUT US </a></li>
			<li><a href=""> OUR MODEL </a></li>
		</div>
		<form action="/results" method = "post">
		<div class = "inputsOne">
			<div class = "inputBlockLong">
				<div class = "box box-top"></div>
				<h3 class = "label label-top"> Find your car's <a>true</a> worth</h3>

				<div class = "inputBox inputBox-A">
					<input type="text"  class="input" id="make" name="make" placeholder="MAKE">
					<img class="icons" src = "static/images/magGlassBlue.svg"></img>
				</div>

				<div class = "inputBox inputBox-B">
					<input type="text" class="input" id="model" name="model" placeholder="MODEL">
					<img class="icons" src = "static/images/steeringWheelBlue.svg"></img>
				</div>
			</div>

			
			<div class = "inputBlockMain">
				<img class="bigIconA" src = "static/images/clockIcon.svg"></img>
				
				<div class = "inputBoxMain inputBox-C">
					<label class= "labelMain" for="year">Year</label>
					<input type="text" class="inputMain input-A" id="year" name="year" placeholder="i.e. 2014">
				</div>

				<div class = "inputBoxMain inputBox-D">
					<label class= "labelMain" for="miles">Miles</label>
					<input type="text"  class="inputMain input-B" id="miles" name="miles" placeholder="i.e. 12653">
				</div>

				<div class = "inputBoxMain inputBox-E">
					<label class= "labelMain" for="transmission">Transmission</label>
					<select  class="inputMain input-C"  id="transmission" name="transmission" placeholder="transmission">
						<option value="automatic">Automatic</option>
						<option value="manual7speed">Manual 7 Speed</option>
						<option value="manual6speed">Manual 6 Speed</option>
						<option value="manual5speed">Manual 5 Speed</option>
					</select>
				</div>
				
			</div>

			<div class = "infoBlock  iC">
				<img class = "infoImg" src = "static/images/windowIcon.svg"></img>
				<h2 class = "infoTitle"> Transparent </h2>
				<h3 class = "infoDesc"> We put our stats, our accuracy and method available for all </h3>
			</div>
		</div>

		<div class = "inputsTwo">
			<div class = "inputBlockLong-A">
				<div class = "box box-mid"></div>
				<h3 class = "label label-mid"> How about some <a>color</a>?</h3>

				<div class = "inputBox inputBox-F">
					<input type="text" class="input" id="exteriorColor" name="exteriorColor" placeholder="i.e. Black">
					<img class="icons" src = "static/images/paintRoller.svg"></img>
				</div>

				<div class = "inputBox inputBox-G">
					<input type="text"  class="input"  id="interiorColor" name="interiorColor" placeholder="i.e. Black">
					<img class="icons" src = "static/images/paintBucket.svg"></img>
				</div>
			</div>

			<div class = "inputBlockMain-A">
				<img class="bigIconA" src = "static/images/twoGears.svg"></img>
				
				<div class = "inputBoxMain inputBox-C">
					<label class= "labelMain" for="drive">Drive</label>
					<select class="inputMain input-A" id="drive" name="drive">
						<option value="4WD">4WD</option>
						<option value="2WD">2WD</option>
					</select>
				</div>

				<div class = "inputBoxMain inputBox-D">
					<label class= "labelMain" for="engineSize">Engine Size</label>
					<input type="text"  class="inputMain input-B" id="engineSize" name="engineSize" placeholder="i.e. 3.6">
				</div>

				<div class = "inputBoxMain inputBox-E">
					<label class= "labelMain" for="transmission">Transmission</label>
					<input  class="inputMain input-C"  id="engineCylinders" name="engineCylinders" placeholder="i.e. 6">
					</select>
				</div>
				
			</div>

			<div class = "infoBlock  iA">
				<img class = "infoImg" src = "static/images/gasCan.svg"></img>
				<h2 class = "infoTitle"> MPG </h2>
				<h3 class = "infoDesc"> How far can you go? Gas is not cheap! 
					<input type="text"  class="inputMain input-H" id="mileage" name="mileage" placeholder="i.e. 26">
				</h3>
			</div>
		</div>

		
		<div class = "inputsThree">
				<div class = "label labelBottom"> 
					Now For Your <a>Free</a> Estimate. 
				<input onclick="window.location.href='/results'" class="getEstBut" type='submit' value='Lets go!'>
				</div>
		</div>
		
		<div class = "bottomReference">
			<h3 class = "aboutUs">CREATED BY SATYA SHAH<br>THE SCIENCE AND MATH ACADEMY<br><br>FEBRUARY 27, 2022</h3>
			<h3 class = "minorLinks"><a href="/">OUR MODEL</a><br>RELIABILITY<br>ABOUT US<br>CONTACT US</h3>
			<h3 class = "thanks">MENTORED BY JARICK CAMMARATO<br><br>SPECIAL THANKS TO YVONNE GABRIEL</h3>
		</div>
			
		<script src="static/myScripts.js"></script>
	</body>

</html>

<!-- <form action="/results" method = "post">
	<label for="miles">Miles</label>
	<input type="text" id="miles" name="miles" placeholder="i.e. 87032" value="87032">

	
	<label for="make">Make</label>
	<input type="text" id="make" name="make" placeholder="i.e. Nissan" value="Nissan">

	<label for="model">Model</label>
	<input type="text" id="model" name="model" placeholder="i.e. Altima" value="Altima">

	<label for="year">Year</label>
	<input type="number" id="year" name="year" min="2010" max="2021" placeholder="i.e. 2014" value="2014">

	<label for="transmission">Transmission</label>
	<select id="transmission" name="transmission">
		<option value="automatic">Automatic</option>
		<option value="manual7speed">Manual 7 Speed</option>
		<option value="manual6speed">Manual 6 Speed</option>
		<option value="manual5speed">Manual 5 Speed</option>
	</select>
	
	<label for="drive">Drive</label>
	<select id="drive" name="drive">
		<option value="4WD">4WD</option>
		<option value="2WD">2WD</option>
	</select>

	<label for="exteriorColor">Exterior Color</label>
	<input type="text" id="exteriorColor" name="exteriorColor" placeholder="i.e. Black" value="Black">

	<label for="interiorColor">Interior Color</label>
	<input type="text" id="interiorColor" name="interiorColor" placeholder="i.e. Black" value="Black">

	<label for="mpgCity">MPG City</label>
	<input type="text" id="mpgCity" name="mpgCity" placeholder="i.e. 19" value="19">

	<label for="mpgHighway">MPG Highway</label>
	<input type="text" id="mpgHighway" name="mpgHighway" placeholder="i.e. 30" value="30">

	<label for="engineSize">Engine Size</label>
	<input type="text" id="engineSize" name="engineSize" placeholder="i.e. 3.6" value="3.6">

	<label for="engineCylinders">Engine Cylinders</label>
	<input type="text" id="engineCylinders" name="engineCylinders" placeholder="i.e. 6" value="6">

<input class="runBut" type='submit' value='Continue'> -->