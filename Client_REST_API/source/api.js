console.log('healthchecker')

const form = document.forms[0]

console.log(form)

addEventListener('submit', async (e) => {
  e.preventDefault()
  const response = await fetch('http://127.0.0.1:8000/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      username: form.username.value,
      password: form.password.value,
    }),
  })
  console.log(response.status)
  console.log(response)
  if (response.status === 200) {
    result = await response.json()
    localStorage.setItem('token', result.access_token)
    window.location = '/list.html'
  }
})

const main = async () => {
  token = localStorage.getItem('token')
  const response = await fetch('http://127.0.0.1:8000/api/notes', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
  console.log(response.status)
  if (response.status === 200) {
    console.log('Success!')
    data = await response.json()
    console.log(data)
    for (el of data) {
      elementHtml = document.createElement('li')
      elementHtml.className = 'list-group-item'
      elementHtml.textContent = `${el.id}: ${el.title} - ${el.description}. Status: ${el.done}. Date: ${el.created_at}`
      notes.appendChild(elementHtml)
    }
  }
}

if (!form) {
  main()
}
