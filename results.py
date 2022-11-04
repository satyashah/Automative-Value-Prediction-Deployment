import numpy as np

indexs = {
"year" : ['2016', '2017', '2018', '2019', '2020', '2021', '2010', '2011', '2012', '2013', '2014', '2015'] ,
"make" : ['porsche', 'fiat', 'smart', 'ram', 'buick', 'volkswagen', 'dodge', 'nissan', 'toyota', 'jaguar', 'kia', 'gmc', 'land rover', 'audi', 'ford', 'mazda', 'acura', 'volvo', 'mini', 'jeep', 'chrysler', 'chevrolet', 'hyundai', 'lincoln', 'mitsubishi', 'lexus', 'subaru', 'honda', 'bmw', 'scion', 'genesis', 'mercedes-benz', 'cadillac', 'infiniti'] ,
"model" : ['passat', 'accord crosstour', 'xc90', 'is 250', 'challenger', '650', 'murano', '500', 'xf', '911', 'impala limited', 'cx-3', 'a4', 'qx50', 'prius', 'avalanche 1500', 'is 300', 'prius v', '500l', 'xt4', 'rogue select', 'tsx', 'nv 200', 'mdx', 'acadia limited', 'rs5', 'glc63 amg coupe', 'rogue hybrid', 'tribeca', 'ecosport', 'is 350', 'fusion energi', 'is 200t', 'titan', 'continental', 'juke', 'forester', 'acadia', '320', 'g80', 'range rover velar', 'xts', 'cla45 amg', 'yaris', 'c-hr', 'hr-v', 'accent', 'charger', 'brz', 'mazda2', 's5', '230', 'c-max', 'fortwo', 'rc 300', 'fr-s', 's7', 'cls550', 'ilx', 'passport', 'insight', 's8', 'captiva sport', 'q60', 'outback', 'panamera', 'range rover', 'edge', 'ranger', '750', 'azera', 'tl', 'g70', 'yukon xl 1500', 'grand caravan', 'taurus', 'c43 amg', 'cx-9', 'sequoia', 'discovery sport', 'flex', '428', 'accord', 'santa fe', 'glb250', 'regal', '530', '500x', 'sl550', 'volt', 'sonic', 'boxster', 'renegade', 'qx80', 'prius c', 'malibu', 'm3', 'gle350', 'spark', 'envision', 's4', 'q50 hybrid', 'tucson', 'forte', 'gle43 amg', '330', 'focus', 'terrain', 'sportage', 'versa note', 'mkz hybrid', 'gx 460', 'supra', 's550', 'stinger', 'c400', '86', 'sonata hybrid', 'traverse', 'allroad', 'ioniq hybrid', 'gls63 amg', 'cts', 'e450', 'tts', 'ss', 'grand cherokee srt-8', '840', 'arteon', 'kicks', 'escalade', 'durango', 'expedition el', 'mx-5 miata', 'camaro', 'x3', 'crosstrek', 'golf', 'navigator l', 'lancer', 'mustang', 'telluride', 'f-pace', 'explorer sport trac', 'tahoe', 'sedona', '540', 'ct6', 'outlander', 'es 300h', 'transit connect', 'ls 500', 'venue', 'rs3', 'mkx', '718 cayman', 'cls400', 'corolla hatchback', 'tacoma', 'avalon hybrid', 'eclipse', 'genesis', 'xj', 'promaster city', 'nx 300h', '4runner', 'lc 500', 'santa fe xl', 'cla250', 'suburban 1500', 'qx56', '500c', '335', 'rav4', 'macan', 'ml400', 'santa fe sport', 'compass', 'nx 300', 'sts', 'fit', 'ascent', 'highlander hybrid', 'liberty', '528', 'c350', 'f150', 'yukon', 'cooper clubman', 'avenger', '1500', 'g37', 'rx 350', 'silverado 1500', 'q50', 'slc43 amg', 'corolla hybrid', 'c-max energi', 'trax', 'rx 450h', 'regal sportback', 'journey', 'optima', 'glc300', 'pacifica', 'kona', 'qx60', 'gla250', 'corvette', 'camry', 'mazda6', 'v60 cross country', 'colorado', 'cooper hardtop', 'mirage g4', 'sq5', 'odyssey', 'q3', 'm37', 'sierra 1500', 'rlx', 's450', '228', '124 spider', 'mks', '328', 'prius plug in hybrid', 'forte5', 'q7', '300', 'c63 amg', 'gl550', 'fusion hybrid', 'ridgeline', 'glc43 amg', 'cayman', 'xt6', 'altima', 'sienna', 'e300', 'trailblazer', 'jetta hybrid', 'blazer', 'equus', 'soul', 'aviator', 'gls550', 'a8', 'ux 250h', 'f-type', '430', 'mkz', 'civic', 'tc', 'gs 350', 'yaris ia', 'slk350', 's90', 'pathfinder', 'corolla im', 'gti', 'impala', 'navigator', 'e250', 'xd', 'regal tourx', 'lx 570', 'cruze limited', 'versa', 'es 350', 'verano', 'ml350', 'canyon', 'qx30', 'tundra', 'frontier', 'corolla', 'v60', 'escape hybrid', 'glc300 coupe', 'malibu hybrid', 'q8', 'niro', 'ex35', 'gladiator', 'fiesta', 'cx-5', 'beetle', 'x2', 'x6', 'eos', 'xb', 'c250', '535', 'lacrosse', 'silverado 1500 ld', 'sonata', 'patriot', 'lucerne', 'atlas cross sport', 'rav4 hybrid', 'm235', 'im', 'explorer', 'ia', 'rio5', '718 boxster', 's3', 'range rover evoque', 'rc 350', 'glk350', 'wrangler', 'ls 460', 'corsair', 'impreza', 'ats', 'rogue sport', '370z', 'cc', 'mirage', 'xv crosstrek', 'slk250', 'tiguan limited', 'dart', 'golf alltrack', 'jetta', 'srx', 'c450 amg', 'discovery', 'c300', 'm2', 'seltos', 'cruze', 'maxima', 'q5', 'xc40', '435', 'nx 200t', 'e400', '640', 'iq', 'e-pace', 'xterra', 'optima hybrid', 'jetta gli', 's60', '200', 'cherokee', 'camry hybrid', 'gl450', 'outlander sport', 'x5', 'x7', 'highlander', 'ct 200h', 'xt5', 'xe', 'sl450', 'sentra', 'mkc', 'expedition', 'tlx', 'equinox', 'qx70', 'rdx', 'a35 amg', 'e550', 'cls450', 'nautilus', 'eclipse cross', 'palisade', 'e43 amg', 'e350', 'veloster', 'grand cherokee', 'cr-v', 'armada', 'a6', 'cooper', 'a3', 'm8', 'cts-v', 'escape', 's560', 'mkt', '1500 classic', 'qx60 hybrid', 'ux 200', 'accord hybrid', 'sierra 1500 limited', 'a7', 'touareg', 'gls450', 's6', 'fj cruiser', 'wrx', 'rogue', 'm240', 'sorento', 'quest', 'xc60', 'gle53 amg', 'cascada', 'pilot', 'range rover sport', 'q70', 'encore gx', 'atlas', 'rc f', 'm4', 'elantra', 'a5', 'z4', 'encore', '340', 'cadenza', 'tt', 'tiguan', 'fusion', 'cooper countryman', 'avalon', 'm340', 'rio', '740', 'mazda3', 'malibu limited', 'gla45 amg', 'town and country', 'x1', 'gle43 amg coupe', 'gs 200t', 'g90', 'x4', 'a220', 'enclave', 'venza', 'g25', 'cayenne', 'legacy'] ,
"transmission" : ['manual 6 speed', 'manual 7 speed', 'manual 5 speed', 'automatic'] ,
"drive" : ['4wd', '2wd'] ,
"exteriorColor" : ['silver', 'burgundy', 'black', 'purple', 'green', 'orange', 'white', 'brown', 'red', 'maroon', 'blue', 'creme', 'gold', 'pearl', 'yellow', 'gray', 'copper', 'tan'] ,
"interiorColor" : ['burgundy', 'black', 'brown', 'orange', 'white', 'red', 'blue', 'taupe', 'champagne', 'cream', 'maroon', 'gray', 'tan']
}

components = ["miles","year","make","model","transmission","drive","exteriorColor","interiorColor","mileage","engineSize","engineCylinders"]

def encodeSingle(value, indexList):
	
  index = indexList.index(value)
  carArr = [0]*len(indexList)
  carArr[index] = 1
  return carArr


def get(dataDict):
	tfArray = []
	
	for component in components:
		if component in indexs.keys():
			# print(dataDict[component].lower(), indexs[component])
			sinArr = encodeSingle(dataDict[component].lower(), indexs[component])
		else:
			sinArr = [float(dataDict[component])]
		tfArray.append(sinArr)

	flatTest =  []
	[flatTest.extend(comp) for comp in tfArray]
			
	return flatTest
