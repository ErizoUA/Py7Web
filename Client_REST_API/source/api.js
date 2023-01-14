console.log('healthchecker')

const main = async () => {
  const response = await fetch('http://127.0.0.1:8000/api/notes', {
    method: 'GET',
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

main()
