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
Go to the store and buy some more, 99 bottles of beer on the wall...`)

// a fancier way, but I think the version above is easier to read and more performant.

// let bottles
// let bottlesLeft

// for (let i = 99; i > 0; i--) {
// 	if (i === 1) {
// 		bottles = 'bottle'
// 		bottlesLeft = 'No bottles of beer on the wall!'
// 	} else {
// 		bottles = 'bottles'
// 		bottlesLeft = `${i - 1} ${bottles} of beer on the wall!`
// 	}
// 	console.log(`${i} ${bottles} of beer on the wall,`)
// 	console.log(`${i} ${bottles} of beer,`)
// 	console.log('Take one down, pass it around,')
// 	console.log(bottlesLeft)
// }
