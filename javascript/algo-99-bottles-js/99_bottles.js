function bottleSong() {
  let bottlesLeft = 99

	while (bottlesLeft > 2) {
		console.log(
			`${bottlesLeft} bottles of beer on the wall, ${bottlesLeft} bottles of beer.`
		)
		bottlesLeft--
		console.log(
			`Take one down and pass it around, ${bottlesLeft} bottles of beer on the wall.`
		)
	}

	console.log(`${bottlesLeft} of beer on the wall, ${bottlesLeft} bottles of beer.
	Take one down and pass it around, 1 bottle of beer on the wall.
	1 bottle of beer on the wall, 1 bottle of beer.
	Take one down and pass it around, no more bottles of beer on the wall.
	No more bottles of beer on the wall, no more bottles of beer.
	Go to the store and buy some more, 99 bottles of beer on the wall.`)
}

bottleSong()
