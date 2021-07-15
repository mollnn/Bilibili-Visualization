<template>
  <div style="width: 80%; height: 300px">
    <div id="echartContainer1" style=" width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  name: "chart1",
  data() {
    return {};
  },
  methods: {
    draw() {
      var myChart = this.$echarts.init(
        document.getElementById("echartContainer1"),
        "infographic"
      );
      myChart.setOption({
        xAxis: {},
        yAxis: {},
        series: [
          {
            symbolSize: 5,
            data: [],
            type: "scatter",
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
      this.$http
        .get("http://131.mollnn.com:5000/api/demo/", {
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