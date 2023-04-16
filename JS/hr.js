function insertEmployees() {
    const employees = JSON.parse(localStorage.getItem("employees"));
    
    const table = document.getElementById("employee-table")

    employees.foreach(employee => {
        const row = table.insertRow()
        const name = row.insertCell()
        name.innerHTML = `<button type="button" class="emp-btn"
                        onclick="windows.location.href = 'employeeData.html'>
                        ${employee.name}</button>`
    })
}