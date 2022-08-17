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
$('.checkAgravo').on('change', function(){
    var id = this.id;
    var agravo = this.value;
    var checked = this.checked;
    data = {'alterar_agravo':true, 'id':id, 'agravo':agravo, 'checked':checked}
    sendRequest(data)
})

// Altera a função de um usuário. 
// TODO: ESCREVER O HTML.
$('.listaFuncoes').on('change', function(){
    var id = this.id;
    var funcao = this.value;
    data = {'alterar_funcao':true, "id":id, "funcao":funcao}
    sendRequest(data)
})
