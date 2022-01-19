$(document).ready(function(){
  $.ajax({
    url : 'ajax_index_aberto',
    success: function(data){
      $('#container2').highcharts({
        title: {
            text: data['doenca']
        },
        xAxis: {
            categories: ['Detectáveis', 'Não detectáveis', 'Inconclusivo', 'Descartado', 'Vazio']
        },
        series: [{
            name: [data['total']],
            type: 'column',
            data: [data['detectados'], data['nao_detectados'], data['inconclusivo'], data['nao_realizado'], data['vazio']]
        }]
    });
    }
  });

$("#btn_filtrar").on('click', function(){
  filtrar_ano = document.getElementById('filtro_ano').value;
  filtrar_dt_inicio = document.getElementById('filtro_dt_inicio').value;
  filtrar_dt_fim = document.getElementById('filtro_dt_fim').value;
  agravo = document.getElementById('agravo').value;
    
  $.ajax({
    url: 'ajax_filtrar_index_aberto',
    data: {
      'ano':filtrar_ano,
      'inicio':filtrar_dt_inicio,
      'fim':filtrar_dt_fim,
      'agravo':agravo
    },
    success: function(data){
      $('#container2').highcharts({
        title: {
          text: data['doenca']
      },
      xAxis: {
          categories: ['Detectáveis', 'Não detectáveis', 'Inconclusivo', 'Descartado', 'Vazio']
      },
      series: [{
          name: [data['total']],
          type: 'column',
          data: [data['detectados'], data['nao_detectados'], data['inconclusivo'], data['nao_realizado'], data['vazio']]
        }]
    });
    }
  });
});

  // Limitando datas a data atual.
  var today = new Date().toISOString().split('T')[0];
  $("#filtro_dt_inicio").attr('max', today);
  $("#filtro_dt_fim").attr('max', today);

  // Ativando botao exportar.
  $("#export").on('change', function(){
    select = document.getElementById('export');
    if (select.value != ""){
      $("#btn_exportar").prop('disabled', false);
    } else {$("#btn_exportar").prop('disabled', true);};
  });

  // Limpando data inicio e fim dos filtros quando clicar no filtro anual.
  $('#filtro_ano').on('click', function(){
    $('#filtro_dt_inicio').val("");
    $('#filtro_dt_fim').val("");
  });


  

  });
  
