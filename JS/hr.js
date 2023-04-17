
function insertEmployees() {
    console.log(1000);
    const employees = JSON.parse(localStorage.getItem("employees"));
    
    const table = document.querySelector(".search-insert")

    Object.keys(employees).forEach(id => {
        const newRow = `
            <tr>
                <td><button type="button" class="emp-btn" onclick="window.location.href = 'employeeData.html'">${employees[id].empName}</button></td>
                <td>
                    <button class="update-employee-btn" type="button" onclick="window.location.href='update.html?id=${id}';">Update</button>
                    <button class="vacation-employee-btn" type="button" onclick="window.location.href='vacation.html?id=${id}';">Vacation</button>
                </td>
            </tr>
        `;
        table.innerHTML += newRow;
    })
}

// insertEmployees();