const jokeElement = document.getElementById('joke')
const jokeButton = document.querySelector('button')

joke()

jokeButton.addEventListener('click', joke)

async function joke() {
  const config = {
    headers: {
      Accept: 'application/json',
    },
  }
  const res = await fetch('https://icanhazdadjoke.com', config)
  const data = await res.json()
  jokeElement.innerHTML = data.joke
}
