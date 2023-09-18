window.onload = () => {
  const baseUrl ="https://api.vatcomply.com/rates?base="

  const selector = document.querySelector("#selector")
  const container = document.querySelector("#container")

  const makeRequest = async (currency) => {
    const result = await fetch(baseUrl + currency)
    const resultJson = await result.json()
    const rates = resultJson.rates
    convertToHTML(rates)
  }

  const createElement = (elem) => {
    const div = document.createElement("div")
    div.innerText = elem
    div.className = "item"
    container.appendChild(div)
  }

  const convertToHTML = (rates) => {
    container.innerHTML = "";
    const ratesArray = Object.entries(rates)
    ratesArray.forEach( elem => createElement(elem))
  }


  selector.addEventListener("change" ,(e) => {
      makeRequest(e.target.value)
    })
}