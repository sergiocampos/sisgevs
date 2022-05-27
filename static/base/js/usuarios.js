// AJAX para autorizar ou desautorizar o agravo de um usuário
$('.checkAgravo').on('change', function(){
    var id = this.id;
    var agravo = this.value;
    var checked = this.checked;
    data = {'id':id, 'agravo':agravo, 'checked':checked}

    $.ajax({
        url:'',
        type:'post',
        data: {'data':JSON.stringify(data)},
        dataType:'json',
        success:function(){
            window.location.href = '/usuarios'
        }
    })
})