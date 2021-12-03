$(document).ready(function(){
  $.ajax({
    url : 'ajax_index_aberto',
    success: function(data){
      $('#container2').highcharts({
        title: {
            text: ''
        },
        xAxis: {
            categories: ['casos']
        },
        series: [{
            type: 'column',
            name: 'Dengue',
            data: [0]
        }, {
            type: 'column',
            name: 'Chikungonha',
            data: [0]
        }, {
            type: 'column',
            name: 'Zika',
            data: [0]
        }, {
            type: 'column',
            name: 'Esporotricose',
            data: [data['casos']]
        }]
    });
    }
  });
  //1919   803

  //624   266

$("#btn_filtrar").on('click', function(){
  filtrar_ano = document.getElementById('filtro_ano').value;
  filtrar_dt_inicio = document.getElementById('filtro_dt_inicio').value;
  filtrar_dt_fim = document.getElementById('filtro_dt_fim').value;
  $.ajax({
    url: 'ajax_filtrar_index_aberto',
    data: {
      'ano':filtrar_ano,
      'inicio':filtrar_dt_inicio,
      'fim':filtrar_dt_fim
    },
    success: function(data){
      $('#container2').highcharts({
        title: {
            text: ''
        },
        xAxis: {
            categories: ['casos']
        },
        series: [{
            type: 'column',
            name: 'Dengue',
            data: [0]
        }, {
            type: 'column',
            name: 'Chikungonha',
            data: [0]
        }, {
            type: 'column',
            name: 'Zika',
            data: [0]
        }, {
            type: 'column',
            name: 'Esporotricose',
            data: [data['casos']]
        }]
    });

    }
  });
});
// AJAX exportar arquivos csv xls.
/*
$("#btn_exportar").on('click', function(){
  var option = $('#export').find(":selected").val();
  $.ajax({
    url: 'ajax_exportar_index_aberto',
    data: {'option':option},
    success: function(data){
      console.log(data);
    }

  });
});
*/
$(function(){
    // Primeiro Grafico
    $('#container').highcharts({
      chart: {
        type: 'pie'
        },
        title: {
          text: ''
        },
        subtitle: {
          text: ''
        },

        accessibility: {
          announceNewData: {
            enabled: true
          },
          point: {
            valueSuffix: '%'
          }
        },

        plotOptions: {
          series: {
            dataLabels: {
              enabled: true,
              format: '{point.name}: {point.y:.1f}%'
            }
          }
        },

        tooltip: {
          headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
          pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },

        series: [
          {
            name: "Doenças",
            colorByPoint: true,
            data: [
              {
                name: "Dengue",
                y: 0,
                drilldown: null
              },
              {
                name: "Chikungonha",
                y: 0,
                drilldown: null
              },
              {
                name: "Zika",
                y: 0,
                drilldown: null
              },
              {
                name: "Esporotricose",
                y: 100,
                drilldown: null
              }]
          }]/*,
        drilldown: { 
          series: [
              {
                name: "Dengue",
                id: "Dengue",
                data: [["João Pessoa", 56.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },{
                name: "Zika",
                id: "Zika",
                data: [["João Pessoa", 56.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },{
                name: "Chikungonha",
                id: "Chikungonha",
                data: [["João Pessoa", 36.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },
        ]}*/
    });
    // Segundo Grafico
    

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
  
