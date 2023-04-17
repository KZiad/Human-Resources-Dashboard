function approveVacation(id) {
  let vacations = JSON.parse(localStorage.getItem("vacations"));
  vacations[id].status = "Approved";
  //TODO: let employees = JSON.parse(localStorage.getItem("employees"));
  // let emp = employees[id];
  // let difference = vacations[id].endDate - vacations[id].beginDate;
  // let days = difference / (1000 * 3600 * 24); // convert ms to days
  // if (days > emp.availablePTO) {
  //   alert("Not enough PTO");
  //   return;
  // }
  // emp.availablePTO -= days;
  // emp.approvedPTO += days;

  // subtract the number of days from the available PTO
  // set the approved PTO to the number of days

  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function denyVacation(id) {
  var vacations = JSON.parse(localStorage.getItem("vacations"));
  vacations[id].status = "Denied";
  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function deleteVacation(id) {
  var vacations = JSON.parse(localStorage.getItem("vacations"));
  delete vacations[id];
  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function loadVacCards() {
  if (
    localStorage.getItem("vacations") == null ||
    localStorage.getItem("vacations") == "{}"
  ) {
    document.write("<h1>No vacations to show</h1>");
  } else {
    let vacs = JSON.parse(localStorage.getItem("vacations"));
    let vacs_keys = Object.keys(vacs);
    for (var i = vacs_keys.length - 1; i >= 0; i--) {
      let k = vacs_keys[i];
      let endDate = new Date(vacs[k].endDate);
      let beginDate = new Date(vacs[k].beginDate);
      let difference = endDate - beginDate;
      let days = difference / (1000 * 3600 * 24);
      document.write(`<div class="vac">
                        <div class="cardHead ${vacs[k].status == "Approved" ? "approved" : vacs[k].status == "Denied" ? "denied" : ""}">
                            <div class="empData">${vacs[k].id} <br/> ${vacs[k].name}</div>
                            <div class="vacStatus">Status: ${vacs[k].status}</div>
                        </div>
                        <div class="cardBody">
                            <div class="vacDates">
                                ${beginDate.getDate()}/${beginDate.getMonth() + 1}/${beginDate.getFullYear()} -> 
                                ${endDate.getDate()}/${endDate.getMonth() + 1}/${endDate.getFullYear()}
                                <br/>${days} days
                            </div>
                            <div class="vacReason">
                                Reason: <br/> ${vacs[k].reason}
                            </div>
                            <div class="vacActions">
                            `);
                            if (vacs[k].status == "Pending") {
                                document.write(`
                                <button class="appBut" onclick="approveVacation(${k})">Approve</button>
                                <button class="denBut" onclick="denyVacation(${k})">Deny</button>
                                `);
                            }
                            document.write(`
                                <button class="deleteBut" onclick="deleteVacation(${k})">Delete</button>
                            
                                
                            </div>
                        </div>
                    </div>`);
    }
  }
}
