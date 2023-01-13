// Função para envio de requisiçao ajax.
const sendRequest = (data) => {
    $.ajax({
        url:'',
        type:'post',
        data: {'data':JSON.stringify(data)},
        dataType:'json',
        success:function(){
            window.location.href = '/usuarios'
        }
    })
}

// Altera os agravos permitidos de um usuário.
$('.agravos-select').on('change', function(){
    var id = this.id;
    var agravos = this.value;
    var req_user_agravos = document.getElementById('req_user_agravos').value;
    req_user_agravos = req_user_agravos.replace("[", '').replace("]",'').replaceAll("'","").replaceAll(' ','').split(',')
    data = {'alterar_agravo':true, 'id':id, 'agravos':agravos, 'req_user_agravos':req_user_agravos};
    sendRequest(data);
})

// Altera a função de um usuário. 
$('.funcoes-select').on('change', function(){
    var id = this.id;
    var funcao = this.value;
    data = {'alterar_agravo':false, 'alterar_funcao':true, "id":id, "funcao":funcao}
    sendRequest(data)    
})

// Altera a unidade de saúde de um usuário.
$('.hospital-select').on('change', function(){
    const id = this.id;
    const hosp = this.value;
    data = {'alterar_agravo':false, 'alterar_funcao':false, 'alterar_hosp': true, "id":id, "hosp":hosp}
    sendRequest(data)
})