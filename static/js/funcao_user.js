$(document).ready(function(){
    funcoes = {
        'admin':'Admin',
        'gerencia_executiva':'Gerência Executiva',
        'gerencia_regional':'Gerência Regional',
        'gerencia_operacional':'Gerência Operacional',
        'area_tecnica':'Área Técnica',
        'chefia_nucleo':'Chefia de Núcleo',
        'municipal':'Municipal',
        'autocadastro':'Autocadastro'
    }
    
    user_funcao = $('#user_funcao').text();
    user_funcao = String(user_funcao)

    user_funcao = funcoes[user_funcao]
    console.log(user_funcao)
    $('#user_funcao').text(user_funcao)
})