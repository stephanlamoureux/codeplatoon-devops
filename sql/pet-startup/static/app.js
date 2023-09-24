const baseUrl = 'http://127.0.0.1:5000'

function getPets() {
	fetch(`${baseUrl}/pets`)
		.then(response => response.json())
		.then(data => {
			const petsList = document.getElementById('pets')
			petsList.innerHTML = ''

			data.forEach(pet => {
				const listItem = document.createElement('li')
				listItem.textContent = `Name: ${pet[3]}, Type: ${pet[2]}`
				petsList.appendChild(listItem)
			})
		})
}

function getOwners() {
	fetch(`${baseUrl}/owners`)
		.then(response => response.json())
		.then(data => {
			const ownersList = document.getElementById('owners')
			ownersList.innerHTML = ''

			data.forEach(owner => {
				const listItem = document.createElement('li')
				listItem.textContent = `Owner Name: ${owner[0]}`
				ownersList.appendChild(listItem)
			})
		})
}

// Add event listener to the button
const petBtn = document.getElementById('petBtn')
petBtn.addEventListener('click', getPets)

const ownerBtn = document.getElementById('ownerBtn')
ownerBtn.addEventListener('click', getOwners)
