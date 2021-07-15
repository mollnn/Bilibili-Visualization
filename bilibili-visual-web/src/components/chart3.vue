<template>
  <div style="width: 100%; height: 300px">
    <div id="echartContainer3" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  name: "chart3",
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
          trigger: "axis",
          position: function (pt) {
            return [pt[0], "10%"];
          },
        axisPointer: {
            animation: false
        }
        },
        xAxis: {
          type: "log",
          boundaryGap: false,
          logbase:10,
          min:60,
          max:330600,
        },
        yAxis: {
          type: "value",
          boundaryGap: false,
        },
        series: [
          {
            name: "播放量量",
            type: "line",
            smooth: true,
            symbol: "none",
            areaStyle: {},
            data: [
            ],
          },
        ],
        grid: [
            {
                top:10,
                bottom:30,
                left:"10%",
                right:"10%",
            }
        ]
      });
      //   myChart.setOption({
      //     xAxis: {},
      //     yAxis: {},
      //     series: [
      //       {
      //         symbolSize: 5,
      //         data: [],
      //         type: "scatter",
      //       },
      //     ],
      //   });
      this.$http
        .get("http://131.mollnn.com:5000/api/duration/distrib/60/", {
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