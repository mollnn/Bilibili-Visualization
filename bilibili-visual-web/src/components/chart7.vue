<template>
  <div style="width: 100%; height: 300px">
    <div id="echartContainer7" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  name: "chart2",
  data() {
    return {};
  },
  methods: {
    draw() {
      var myChart = this.$echarts.init(
        document.getElementById("echartContainer7"),
        "infographic"
      );
      myChart.setOption({tooltip: {
        trigger: 'axis'
    },
    toolbox: {
        show: true,
        x: 200,
        y: 0,
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    calculable: true,
    xAxis: [
        {
            type: 'value',
            show: false,
            max: 10000,
            axisLabel: {
            inside: true,
            textStyle: {
                color: '#fff'
            }
        },
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        },
        z: 10
        }
    ],
    yAxis: [
        {
            type: 'value',
            splitLine: {show: false},
            axisLine: {
            show: false
        },
        axisTick: {
            show: false
        },
        axisLabel: {
            textStyle: {
                color: '#999'
            }
        }
        }
    ],
    dataZoom: [
        {
            type: 'inside'
        }
    ],
    series: [
        {
            showBackground: true,
            itemStyle: {
                color: 'rgb(154,200,240)'
            },
             emphasis: {
                itemStyle: {
                    color: this.$echarts.graphic.LinearGradient(
                        0, 0, 0, 1,
                        [
                            {offset: 0, color: '#2378f7'},
                            {offset: 0.7, color: '#2378f7'},
                            {offset: 1, color: '#83bff6'}
                        ]
                    )
                }
            },
            name: '视频量',
            type: 'bar',
            data: [],
        },
    ],
    grid: [
            {
                top:10,
                bottom:20,
                left:"10%",
                right:"10%",
            }
        ]
});
    // Enable data zoom when user click bar.
var zoomSize = 6;
myChart.on('click', function (params) {
    console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
    myChart.dispatchAction({
        type: 'dataZoom',
        startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
        endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
    });
});
      this.$http
        .get("http://131.mollnn.com:5000/api/favorite/distrib/500/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          myChart.hideLoading();
          myChart.setOption({ series: [{ data: res.data }] });
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>

