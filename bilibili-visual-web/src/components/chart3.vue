<template>
  <div style="width: 100%; height: 300px">
    <div id="echartContainer3" style="width: 100%; height: 100%"></div>
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
        document.getElementById("echartContainer3"),
        "infographic"
      );
      myChart.setOption({
    tooltip: {
        trigger: 'axis',
        position: function (pt) {
            return [pt[0], '10%'];
        }
    },
    toolbox: {
        feature: {
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'log',
        logbase:10,
        min:80,
        max:1500,
        boundaryGap: false,
        axisLabel: {
            inside: true,
            textStyle: {
                color: '#fff'
            }
        },
        show:false,
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        },

    },
    yAxis: {
        type: 'value',
        boundaryGap: false,
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
    },
    dataZoom: [
        {
            type: 'inside'
        }
    ],
    series: [
        {
            name: '播放量',
            type: 'line',
            symbol: 'none',
            sampling: 'lttb',
            itemStyle: {
                color: 'rgb(154,200,240)'
            },
            areaStyle: {
                color: this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgb(255, 158, 68)'
                }, {
                    offset: 1,
                    color: 'rgb(255, 70, 131)'
                }])
            },
            data: []
        }
    ],
    grid: [
            {
                top:20,
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
        .get("http://131.mollnn.com:5000/api/duration/distrib/20/", {
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






