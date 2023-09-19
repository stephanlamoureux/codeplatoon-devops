const displayNorrisJoke = document.querySelector('#norris-joke')
const loading = document.querySelector('#loading')

// grab a random joke from the chuck norris api and display it in a <p> tag.
async function fetchNorrisJoke() {
	try {
		loading.classList.remove('hidden')
		const results = await fetch(`https://api.chucknorris.io/jokes/random`)

		if (!results.ok) {
			displayNorrisJoke.textContent = 'Your Chuck Norris joke is missing!'
			throw new Error('Request failed.')
		}

		const data = await results.json()
		loading.classList.add('hidden')
		displayNorrisJoke.textContent = data.value
	} catch (error) {
		displayNorrisJoke.textContent = 'There was an error with your Chuck Norris joke!'
		console.error(error)
	}
}

const displayDadJoke = document.querySelector('#dad-joke')
const dadLoading = document.querySelector('#dad-loading')

async function fetchDadJoke() {
	try {
		dadLoading.classList.remove('hidden')
		const results = await fetch('http://icanhazdadjoke.com', {
			headers: {
				Accept: 'application/json',
			},
		})

		if (!results.ok) {
			displayDadJoke.textContent = 'Your dad joke is missing!'
			throw new Error('Request failed.')
		}

		const data = await results.json()
		dadLoading.classList.add('hidden')
		displayDadJoke.textContent = data.joke
	} catch (error) {
		displayDadJoke.textContent = 'There was an error with your dad joke!'
		console.log(error)
	}
}
