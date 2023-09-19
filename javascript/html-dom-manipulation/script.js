// function used by the event handlers to change image src
function changeImage(imageId, newImageSrc) {
	const image = document.getElementById(imageId)

	if (image) {
		image.src = newImageSrc
		console.log(`${imageId} was clicked!`)
	}
}

// Attach click event handlers to each button
function attachClickHandler(btnId, imgId, imgSrc) {
	const button = document.getElementById(btnId)
	button.addEventListener('click', function () {
		changeImage(imgId, imgSrc)
		button.textContent = 'Thanks!'
		button.disabled = true
	})
}

attachClickHandler('btn1', 'dog1', './images/dog1_after.webp')
attachClickHandler('btn2', 'dog2', './images/dog2_after.webp')
attachClickHandler('btn3', 'dog3', './images/dog3_after.webp')

// document.getElementById('btn1').addEventListener('click', function () {
// 	const button = document.getElementById('btn1')
// 	changeImage('dog1', './images/dog1_after.webp')
// 	button.textContent = 'Thanks!'
// 	button.disabled = true
// })

// document.getElementById('btn2').addEventListener('click', function () {
// 	changeImage('dog2', './images/dog2_after.webp')
// 	const button = document.getElementById('btn2')
// 	button.textContent = 'Thanks!'
// 	button.disabled = true
// })

// document.getElementById('btn3').addEventListener('click', function () {
// 	changeImage('dog3', './images/dog3_after.webp')
// 	const button = document.getElementById('btn3')
// 	button.textContent = 'Thanks!'
// 	button.disabled = true
// })

// Log alt text of each image
const images = document.querySelectorAll('img')
images.forEach((image, index) => {
	const altText = image.getAttribute('alt')
	console.log(`Image ${index + 1} Alt Text: ${altText}`)
})

// replaces images with their alt text
function replaceImages() {
	let images = document.body.getElementsByTagName('img')
	for (let i = images.length - 1; i >= 0; i--) {
		let image = images[i]
		if (image.alt) {
			let text = document.createTextNode(image.alt)
			image.parentNode.replaceChild(text, image)
		}
	}
	// Hide buttons and footer
	document.getElementById('footer').style.display = 'none'
	const buttons = document.querySelectorAll('button')
	buttons.forEach(button => {
		button.style.display = 'none'
	})
}
