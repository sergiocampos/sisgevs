// Ativa e desativa o hospital de referencia
function active_hospital(){
    var opt=document.getElementById('hospital_transferencia');
    var radio_sim = document.getElementById("radio_sim");

    if (radio_sim.checked) {
        opt.removeAttribute("class","d-none");

    } else{
        opt.setAttribute("class","d-none")
    }
}

