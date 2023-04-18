function createEmployee() {

    if(localStorage.getItem('employees') == null){
        localStorage.setItem('employees', '{}');
    }

    let employees = JSON.parse(localStorage.getItem('employees'));

    const employee = {
        id: document.getElementById("id").value,
        empName: document.getElementById("name").value,
        email: document.getElementById("email").value,
        address: document.getElementById("address").value,
        phone: document.getElementById("number").value,
        gender: document.querySelector('input[name = "gender"]:checked') ? document.querySelector('input[name = "gender"]:checked').value : null,
        maritalStat: document.getElementById("status").options[document.getElementById("status").selectedIndex].value,
        availablePTO: document.getElementById("vacation").value,
        approvedPTO: 0,
        salary: document.getElementById("salary").value,
        DOB: document.getElementById("dob").value
    };

    if(validateData(employee)){
        employees[employee.id] = employee;
        localStorage.setItem('employees', JSON.stringify(employees));
        alert("Employee added successfully");
        console.log(localStorage);
        window.location.href = 'index.html';
    }
}

function validateData(employee) {

    if(employee.empName == "" || employee.empName == undefined || employee.empName == null){
        alert("Please enter a valid name...");
        return false;
    }
    if(employee.id == "" || employee.id == undefined || employee.id == null){
        alert("Please enter a valid ID...");
        return false;
    }

    if(JSON.parse(localStorage.getItem('employees'))[employee.id] != null){
        alert("ID is already in use");
        return false;
    }

    if(employee.email == "" || employee.email == undefined || employee.email == null){
        alert("Please enter a valid E-Mail...");
        return false;
    }
    if(employee.address == "" || employee.address == undefined || employee.address == null){
        alert("Please enter a valid address...");
        return false;
    }
    if(employee.phone == "" || employee.phone == undefined || employee.phone == null){
        alert("Please enter a valid mobile number...");
        return false;
    }
    if(employee.gender == "" || employee.gender == undefined || employee.gender == null){
        alert("Please choose a gender...");
        return false;
    }
    if(employee.martialStat == "undefined"){
        alert("Please choose a martial status...");
        return false;
    }
    if(employee.availablePTO == "" || employee.availablePTO == undefined || employee.availablePTO == null){
        alert("Please enter number of available vacation days...");
        return false;
    }

    if(employee.DOB == "" || employee.DOB == undefined || employee.DOB == null){
        alert("Please enter a valid date of birth...");
        return false;
    }

    let date  = new Date();
    let dob = new Date(document.getElementById("dob").valueAsDate);

    if(((date - dob) / (1000 * 60 * 60 * 24 * 365)) < 16){
        alert("Invalid date...");
        return false;
    }

    if(employee.salary == "" || employee.salary == undefined || employee.salary == null){
        alert("Please enter starting salary...");
        return false;
    }

    return true;
}

const submitBtn = document.querySelector('#submit');

submitBtn.addEventListener('click', createEmployee);