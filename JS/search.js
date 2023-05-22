async function searchData() {
    const searchInput = document.getElementById('search-input')
    const searchResults = document.getElementById('search-insert')

    const searchTerm = searchInput.nodeValue.toLowerCase()
    if (searchTerm === '') {
        searchResults.innerHTML = ''
        return
    }
    await fetch(`/search-employee?searchTerm=${encodeURIComponent(searchTerm)}`)
    .then(response => response.json())
    .then(data => {
        searchResults.innerHTML = ''

        data.forEach(employee => {
            const newRow = document.createElement("tr")
            newRow.innerHTML = `
            <td><button type="button" class="emp-btn" onclick="window.location.href = 'employeeData.html?id=${employee.id}'">${employee.name}</button></td>
            <td>
              <button class="update-employee-btn" type="button" onclick="window.location.href='update.html?id=${employee.id}';">Update</button>
              <button class="vacation-employee-btn" type="button" onclick="window.location.href='vacation.html?id=${employee.id}';">Vacation</button>
            </td>
            `
            searchResults.appendChild(newRow)
        })
    })
    .catch(error => {
        console.log("Error", error)
    })
    
}