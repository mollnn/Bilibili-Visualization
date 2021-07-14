<template>
  <div>
    <div id="echartContainer" style="width: 100%; height: 500px"></div>
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
        document.getElementById("echartContainer"),
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
      });
      this.$http
        .get("http://localhost:5000/api/demo/", {
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
