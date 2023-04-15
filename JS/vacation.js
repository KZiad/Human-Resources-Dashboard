function validate(vac) {
  // Check if id is a number
  if (vac.id == "" || vac.id == undefined) {
    alert("Error: Please write a valid ID");
    return false;
  }

  // Checking if the name exists
  if (vac.name == "" || vac.name == undefined) {
    alert("Error: Please enter a name");
    return false;
  }

  // Checking if the dates are valid
  var today = new Date();
  var beginDate = vac.beginDate;
  var endDate = vac.endDate;
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

  // Checking if the reason exists
  if (vac.reason == "" || vac.reason == undefined) {
    alert("Error: Please enter a reason");
    return false;
  }
  return true;
}

function submitVacForm() {
  var vac = {
    id: document.getElementById("empID").value,
    name: document.getElementById("empName").value,
    beginDate: document.getElementsByName("beginDate")[0].value,
    endDate: document.getElementsByName("endDate")[0].value,
    reason: document.getElementsByName("reason")[0].value,
    status: "Pending",
  };
  if (!validate(vac)) {
    return;
  }

  if (localStorage.getItem("vacations") == null) {
    localStorage.setItem("vacations", "[]");
  }
  var vacs = JSON.parse(localStorage.getItem("vacations"));

  vacs[vacs.length] = vac;
  localStorage.setItem("vacations", JSON.stringify(vacs));

  window.location.href = "vacationList.html";
}

function prefillForm() {
  let vacid = localStorage.getItem("vacid");
  let vacname = localStorage.getItem("vacname");
  if (vacid != null && vacname != null) {
    document.getElementById("empID").value = vacid;
    document.getElementById("empName").value = vacname;
    document.getElementById("empID").disabled = true;
    document.getElementById("empName").disabled = true;
  }
}
