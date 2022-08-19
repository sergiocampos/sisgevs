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
    data = {'alterar_agravo':true, 'id':id, 'agravos':agravos}
    sendRequest(data)
})

// Altera a função de um usuário. 
// TODO: ESCREVER O HTML.
$('.funcoes-select').on('change', function(){
    var id = this.id;
    var funcao = this.value;
    data = {'alterar_agravo':false, 'alterar_funcao':true, "id":id, "funcao":funcao}
    sendRequest(data)    
})
