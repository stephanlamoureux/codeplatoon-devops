// exports.factorial = function(num) {
// };

function factorial(num){
	// base case
	if (num < 0) {
		return undefined
	} else if (num == 0) {
		return 1
		// recursive case
	} else {
			return num * factorial(num - 1)
	}
}

// tests
console.log(factorial(8))  // 40320
console.log(factorial(18))  // 6402373705728000
console.log(BigInt(factorial(45)))  // 119622220865480194561963161495657715064383733760000000000
console.log(factorial(0))  // 1
console.log(factorial(1)) // 1
console.log(factorial(-20)) // undefined