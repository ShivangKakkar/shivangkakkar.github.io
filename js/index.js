let btn = document.getElementsByClassName('close-btn')[0]
let menu = document.getElementsByClassName('menu')[0]

btn.addEventListener('click', () => {
  menu.classList.toggle('hide')
})
