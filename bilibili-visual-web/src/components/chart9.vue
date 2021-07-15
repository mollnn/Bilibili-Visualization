<template>
  <div style="width: 100%; height: 300px">
    <div id="echartContainer9" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  name: "chart9",
  data() {
    return {};
  },
  methods: {
    draw() {
      var myChart = this.$echarts.init(
        document.getElementById("echartContainer9"),
        "infographic"
      );
      myChart.setOption({
    xAxis: {
        type: 'value',
          min:0,
          max:1500000,
        // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'log',
        logbase:10,
    },
    series: [{
        data: [],
        type: 'bar'
    }],
            grid: [
            {
                top:10,
                bottom:30,
                left:"18%",
                right:"0%",
            }
        ]
}
      );
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
        .get("http://131.mollnn.com:5000/api/likes/distrib/100000/", {
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