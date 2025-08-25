
function addRow() {
    let table = document.getElementById("tableforschedule")
    let row = table.insertRow(-1)
    // let cell1 = row.insertCell(0);
    // let cell2 = row.insertCell(1);
    // row.insertCell(2);
    // row.insertCell(3);
    // row.insertCell(4);
    // row.insertCell(5);
    // row.insertCell(6);
    for (i=0;i<7;i++){
        let cell = row.insertCell(i)
        cell.innerHTML = "<input>"
    }

}

function changePage(){
    let redir = document.getElementById("changer")
    open("/form")
}

function getInfo() {
    let table = document.getElementById("tableforschedule")
    alert(table.item)
}

