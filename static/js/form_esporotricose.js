function clear_select_uc() {
    $("#select_uc_id").val("");
}

$(function () {
    $("#select_uc_id option").hide();
    $("#select_municipio_uc_id").on("change", function () {
        let municipio_uc = $("#select_municipio_uc_id").val();
        $("#select_uc_id option").hide();
        $("#select_uc_id option[data-uc=" + municipio_uc + "]").show();
    });
});

function activeInputsAutoctone() {
    $("#uf_caso_autoctone_id").prop("disabled", false);
    $("#pais_autoctone_id").prop("disabled", false);
    $("#municipio_autoctone_id").prop("disabled", false);
    $("#ibge_autoctone_id").prop("disabled", false);
    $("#distrito_autoctone_id").prop("disabled", false);
    $("#bairro_autoctone_id").prop("disabled", false);
    $("#area_provavel_infeccao_autoctone_id").prop("disabled", false);
    $("#ambiente_infeccao_autoctone_id").prop("disabled", false);
    $("#doenca_rel_trabalho_autoctone_id").prop("disabled", false);

}

function desactiveInputsAutoctone() {
    $("#uf_caso_autoctone_id").prop("disabled", true);
    $("#pais_autoctone_id").prop("disabled", true);
    $("#municipio_autoctone_id").prop("disabled", true);
    $("#ibge_autoctone_id").prop("disabled", true);
    $("#distrito_autoctone_id").prop("disabled", true);
    $("#bairro_autoctone_id").prop("disabled", true);
    $("#area_provavel_infeccao_autoctone_id").prop("disabled", true);
    $("#ambiente_infeccao_autoctone_id").prop("disabled", true);
    $("#doenca_rel_trabalho_autoctone_id").prop("disabled", true);

    $("#uf_caso_autoctone_id").val("");
    $("#pais_autoctone_id").val("");
    $("#municipio_autoctone_id").val("");
    $("#ibge_autoctone_id").val("");
    $("#distrito_autoctone_id").val("");
    $("#bairro_autoctone_id").val("");
    $("#area_provavel_infeccao_autoctone_id").val("");
    $("#ambiente_infeccao_autoctone_id").val("");
    $("#doenca_rel_trabalho_autoctone_id").val("");
}

function validaDtPrimeirosSintomas() {
    if (document.Form.dt_primeiros_s.value == "") {
        document.getElementById('alert_dt_ps').style.display = "inline";
        document.getElementById('alert_dados_gerais').style.display = "inline";
        document.getElementById('alert_notificacao_individual').style.display = "inline";
        document.getElementById('alert_data_invest').style.display = "inline";
        document.getElementById('alert_data_nasc').style.display = "inline";
        document.getElementById('alert_nome_mae').style.display = "inline";
        document.getElementById('alert_dados_residencia').style.display = "inline";
        document.getElementById('alert_telefone_paciente').style.display = "inline";


        alert("Campo obrigatorio!");
        return false;
    }
    else {
        document.getElementById('alert_dt_ps').style.display = "none";
        return true;
    }

} // FIM AJAX CEP

function activeGestante() {
    verificarNotifGeral()
    var genero = document.getElementById('span_id').value;
    let idade = document.getElementById('result').value;
    if ((idade <= 10 || idade >= 50) && (genero != "M") && (genero != "")) {
        $('#gestante_id').children('option[value=""]').hide();
        $('#gestante_id').children('option[value="1º Trimestre"]').hide();
        $('#gestante_id').children('option[value="2º Trimestre"]').hide();
        $('#gestante_id').children('option[value="3º Trimestre"]').hide();
        $('#gestante_id').children('option[value="Idade Gestacional Ignorada"]').hide();
        $('#gestante_id').children('option[value="Ignorado"]').hide();
        $('#gestante_id').children('option[value="Não"]').hide();
        $('#gestante_id').children('option[value="Não se aplica"]').prop('selected', true);
    } else if ((idade > 10 && idade < 50) || (genero != "M")) {
        $('#gestante_id').children('option[value=""]').show();
        $('#gestante_id').children('option[value="1º Trimestre"]').show();
        $('#gestante_id').children('option[value="2º Trimestre"]').show();
        $('#gestante_id').children('option[value="3º Trimestre"]').show();
        $('#gestante_id').children('option[value="Idade Gestacional Ignorada"]').show();
        $('#gestante_id').children('option[value="Ignorado"]').show();
        $('#gestante_id').children('option[value="Não"]').show();
        $('#gestante_id').children('option[value="Não se aplica"]').prop('selected', false);
        $('#gestante_id').children('option[value=""]').prop('selected', true);
    }
    if (idade <= 3) {
        $('#escolaridade').children('option[value=""]').hide();
        $('#escolaridade').children('option[value="Analfabeto"]').hide();
        $('#escolaridade').children('option[value="1ª-a-4ª-serie-incompleto"]').hide();
        $('#escolaridade').children('option[value="4ª-serie-completa"]').hide();
        $('#escolaridade').children('option[value="5ª-a-8ª-serie-incompleto"]').hide();
        $('#escolaridade').children('option[value="Ensido-Fundamental-Completo"]').hide();
        $('#escolaridade').children('option[value="Ensino-Medio-incompleto"]').hide();
        $('#escolaridade').children('option[value="Ensino-Medio-Completo"]').hide();
        $('#escolaridade').children('option[value="Superior-Incompleto"]').hide();
        $('#escolaridade').children('option[value="Superior-completo"]').hide();
        $('#escolaridade').children('option[value=""]').prop('selected', false);
        $('#escolaridade').children('option[value="Nao-se-aplica"]').prop('selected', true);
    } else if (idade > 3) {
        $('#escolaridade').children('option[value=""]').show();
        $('#escolaridade').children('option[value="Analfabeto"]').show();
        $('#escolaridade').children('option[value="1ª-a-4ª-serie-incompleto"]').show();
        $('#escolaridade').children('option[value="4ª-serie-completa"]').show();
        $('#escolaridade').children('option[value="5ª-a-8ª-serie-incompleto"]').show();
        $('#escolaridade').children('option[value="Ensido-Fundamental-Completo"]').show();
        $('#escolaridade').children('option[value="Ensino-Medio-incompleto"]').show();
        $('#escolaridade').children('option[value="Ensino-Medio-Completo"]').show();
        $('#escolaridade').children('option[value="Superior-Incompleto"]').show();
        $('#escolaridade').children('option[value="Superior-completo"]').show();
        $('#escolaridade').children('option[value=""]').prop('selected', true);
        $('#escolaridade').children('option[value="Nao-se-aplica"]').prop('selected', false);
    }

    if (genero == "F") {
        $("#gestante_id").prop("disabled", false);
    }
    if (genero == "Ignorado") {
        $("#gestante_id").prop("disabled", false);
    }
    if (genero == "M") {
        $("#gestante_id").prop("disabled", true);
        $("#gestante_id").val("");
    }
}

function activeOutraUnidade() {
    $("#outra_unidade_id").prop("disabled", false);
    $("#btn_desfaz_outra_unidade_id").prop("disabled", false);
}

function desactiveOutraUnidade() {
    $("#outra_unidade_id").prop("disabled", true);
    $("#outra_unidade_id").val("");
}

$("#municipio_id").change(function () {
    //const url = $('#Form').attr("data-unidadesaude-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_load_unidadesaude" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            $("#unidade_saude_id").html(data);
        }
    });


});

$("#municipio_id").change(function () {
    //const url = $('#Form').attr("data-ibge-url");
    const municipioId = $(this).val();
    $.ajax({
        url: '{% url "ajax_load_ibge" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            $("#ibge_cod_id").val(data);
        }
    });

});

//ajax para selects de hospitalização:
//mun_hosp_id
//cod_ibge_id
//nome_hosp_id

//data-hospitalizacao-url
//data-hospitalizacaoibge-url

$("#mun_hosp_id").change(function () {
    //const url = $('#Form').attr("data-hospitalizacao-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_hospitalizacao" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            $("#nome_hosp_id").html(data);
        }
    });


});

$("#mun_hosp_id").change(function () {
    //const url = $('#Form').attr("data-hospitalizacaoibge-url");
    const municipioId = $(this).val();
    $.ajax({
        url: '{% url "ajax_hospitalizacao_ibge" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            $("#cod_ibge_id").val(data);
        }
    });

});

//Ajax para caso autoctone: Estado, Municipio, Cód IBGE e Distrito.
$("#uf_caso_autoctone_id").change(function () {
    //const url = $('#Form').attr("data-autoctone-uf-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_autoctone_uf" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            $("#municipio_autoctone_id").html(data);
        }
    });


});

$("#municipio_autoctone_id").change(function () {
    //const url = $('#Form').attr("data-autoctone-municipio-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_autoctone_municipio" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            console.log(data);
            $("#ibge_autoctone_id").html(data);
        }
    });


});





$("#municipio_autoctone_id").change(function () {
    //const url = $('#Form').attr("data-autoctone-distrito-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_autoctone_distrito" %}',
        data: { 'municipio_id': municipioId },
        success: function (data) {
            console.log(data);
            $("#distrito_autoctone_id").html(data);
        }
    });


});

//ajax para endereço: estado e cidades

$("#uf_dados_residencia_id").change(function () {
    //const url = $('#Form').attr("data-autoctone-distrito-url");
    municipioId = $(this).val();

    $.ajax({
        url: '{% url "ajax_dados_residencia" %}',
        data: { 'uf_dados_residencia_id': municipioId },
        success: function (data) {
            console.log(data);
            $("#municipios_estado_id").html(data);
        }
    });


});

//Ajax para autoprencher o código ibge se alterar município
$("#municipios_estado_id").change(function () {
    municipioId = $(this).val();
    uf_id = $('#uf_dados_residencia_id').val();

    $.ajax({
        url: '{% url "ajax_ibge_municipio_residencia" %}',
        data: { 'municipios_estado_id': municipioId, 'uf_estado_id': uf_id },
        success: function (data) {
            $("#ibge_municipio_residencia_id").val(data);
        }
    });


});