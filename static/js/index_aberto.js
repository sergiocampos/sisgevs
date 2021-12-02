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
                y: 25,
                drilldown: null
              },
              {
                name: "Chikungonha",
                y: 37,
                drilldown: null
              },
              {
                name: "Zika",
                y: 38,
                drilldown: null
              },
              {
                name: "Esporotricose",
                y: 70,
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
            data: [5]
        }, {
            type: 'column',
            name: 'Chikungonha',
            data: [3]
        }, {
            type: 'column',
            name: 'Zika',
            data: [4]
        }, {
            type: 'column',
            name: 'Esporotricose',
            data: [15]
        }]
    });

  });  
  var today = new Date().toISOString().split('T')[0];
  $("#filtro_dt_inicio").attr('max', today);
  $("#filtro_dt_fim").attr('max', today);
