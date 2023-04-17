const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');
localStorage.setItem("vacId", id);
function validate(vac) {
  // Check if id is a number
  if (vac.id == "" || vac.id == undefined) {
    alert("Error: Please write a valid ID");
    return false;
  }

  //Checking if the id exists
  let employees = JSON.parse(localStorage.getItem("employees"));
  if (employees[vac.id] == null) {
    alert("Error: ID does not exist");
    return false;
  }

  // Checking if the name exists
  if (vac.name == "" || vac.name == undefined) {
    alert("Error: Please enter a name");
    return false;
  }

  // Checking if the dates are valid
  let today = new Date();
  let beginDate = vac.beginDate;
  let endDate = vac.endDate;
  if (beginDate < today) {
    alert("Error: Begin date must be in the future");
    return false;
  }
  if (endDate < today) {
    alert("Error: End date must be in the future");
    return false;
  }
  if (endDate < beginDate) {
    alert("Error: End date must be after begin date");
    return false;
  }

  // Checking if the employee has enough PTO
  let empPTOMs = (employees[vac.id].availablePTO) * 24 * 60 * 60 * 1000;
  let vacMs = (endDate - beginDate);
  if (vacMs > empPTOMs) {
    alert("Error: Employee does not have enough PTO");
    return false;
  }

  // Checking if the reason exists
  if (vac.reason == "" || vac.reason == undefined) {
    alert("Error: Please enter a reason");
    return false;
  }
  return true;
}

function submitVacForm() {
  let vac = {
    id: document.getElementById("empID").value,
    name: document.getElementById("empName").value,
    beginDate: document.getElementsByName("beginDate")[0].valueAsDate,
    endDate: document.getElementsByName("endDate")[0].valueAsDate,
    reason: document.getElementsByName("reason")[0].value,
    status: "Pending",
  };
  if (!validate(vac)) {
    return;
  }

  if (localStorage.getItem("vacations") == null) {
    localStorage.setItem("vacations", "{}");
  }
  let vacs = JSON.parse(localStorage.getItem("vacations"));
  //TODO later: check if employee already has a vacation request and if it intersects with this one
  if (vacs[vac.id] != null) {
    alert("Error: Employee already has vacation request");
    return;
  }
  vacs[vac.id] = vac;
  localStorage.setItem("vacations", JSON.stringify(vacs));
  localStorage.removeItem("vacId");
  window.location.href = "vacationList.html";
}

function prefillForm() {
  let vacId = localStorage.getItem("vacId");
  if (vacId != null) {
    document.getElementById("empID").value = vacId;
    let empData = JSON.parse(localStorage.getItem("employees"));
    document.getElementById("empName").value = empData[vacId].empName;
    document.getElementById("empID").disabled = true;
    document.getElementById("empName").disabled = true;
  }
}

addEventListener("change", prefillForm);