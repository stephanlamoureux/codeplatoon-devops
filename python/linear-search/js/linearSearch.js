function linearSearch(key, arr) {
	for (let i = 0; i < arr.length; i++) {
		return arr[i] === key ? i : undefined
	}
}

function globalLinearSearch(key, arr) {
	let results = []
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === key) {
			results.push(i)
		}
	}

	if (results.length === 0) {
		return undefined
	} else {
		return results
	}
}

console.log(linearSearch(1, [1, 3, 5])) // 0
// global linear search tests
const bananas_list = ['b', 'a', 'n', 'a', 'n', 'a', 's']
console.log(globalLinearSearch('a', bananas_list)) // 1, 3, 5
console.log(globalLinearSearch(3, [1, 2, 3])) // 2
console.log(globalLinearSearch(4, [1, 2, 3])) // undefined
console.log(globalLinearSearch(13, [1, 2, 3])) // undefined

// exports.linearSearch = function (valueToFind, arrayToSearchThrough) {}
