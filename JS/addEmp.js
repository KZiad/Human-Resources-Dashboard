function validateData() {

}

function createEmployee() {
    
    const employee = {
        id: document.getElementById("id").value,
        empName: document.getElementById("name").value,
        email: document.getElementById("email").value,
        address: document.getElementById("address").value,
        phone: document.getElementById("number").value,
        gender: document.getElementsByName("gender").value,
        martialStat: document.getElementById("status").value,
        availablePTO,
        approvedPTO,
        salary: document.getElementById("salary"),
        DOB: document.getElementById("dob")
    };

    alert("Employee added successfully");
}

window.addEventListener("submit", createEmployee);