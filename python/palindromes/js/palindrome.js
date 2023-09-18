exports.palindrome = function(word) {
	// Make sure it's a string and all letters are lowercase.
	const stringify = String(word).toLowerCase()
	// Remove special characters and whitespace
	const forward = stringify.replace(/[^a-zA-Z0-9]/g, '')
	// Reverse the string
	const backwards = forward.split("").reverse().join("")

	return true ? forward === backwards : false

}
