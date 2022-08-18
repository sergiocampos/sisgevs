var capturando = "";
var funcao = "";
var estilo = "";

function capturar(){
    capturando = document.getElementById("layout").value;
    funcao = document.getElementById("Funcao").value;
    estilo = document.getElementById("Estilizacao").value;

    document.getElementById("valorDigitado").innerHTML = capturando;
    document.getElementById("valorFuncao").innerHTML = funcao;
    document.getElementById("valorEtilo").innerHTML = estilo;
}


//resgatar valor do layout

/*var form = document.querySelector("#formulario_versionamento");
form.addEventListener("submit",function(e){
    e.preventDefault();
    const layout = document.querySelector("#layout");

    const value = layout.value;
    const dados = e.target.value;
    console.log(dados);


    const desenvolvedor = dados[0]
    const ambiente =
    const data = {
        'desenv':desenvolvedor,
        'ambiente': ambiente
    }
    */
 /*
    $.ajax({
        url: '...',
        method: 'post',
        data: JSON.jsonify(data),
        dataType: 'json',
        beforeSend: function(){

        },
        success: function(res){
            console.log(res)
        },
        error: function(res){
            console.log(res)
        }
    })


});

*/