const searchInp = document.getElementById('search-input')
const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')

const tBody = document.querySelector('.table-body')
tableOutput.style.display = 'none'

searchInp.addEventListener('keyup', (e) => {

    const searchVal = e.target.value

    if (searchVal.trim().length > 0) {
        tBody.innerHTML = ''

        fetch("/search-employees", {
            body: JSON.stringify({ searchText: searchVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            appTable.style.display = 'none'
            tableOutput.style.display = 'block'

            if (data.length === 0) {
                tableOutput.style.display = 'none'
            } else {
                data.forEach(e => {
                    tBody.innerHTML += `
                    <tr>
                        <td><button type="button" class="emp-btn" onclick="window.location.href='/data/${e.id}';">${e.name}</button></td>
                        <td>
                            <button class="update-employee-btn" type="button" onclick="window.location.href='/updateData/${e.id}';">Update</button>
                            <button class="vacation-employee-btn" type="button" onclick="window.location.href='/vacation/${e.id}';">Vacation</button>
                        </td>
                    </tr>
                    `
                })
            }
        })

    } else {
        tableOutput.style.display = 'none'
        appTable.style.display = 'block'
    }
})