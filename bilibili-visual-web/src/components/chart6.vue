<template>
  <div>
    <div id="echartContainer6" style="width: 100%; height: 300px"></div>
  </div>
</template>

<script>
export default {
  name: "chart6",
  data() {
    return {};
  },
  methods: {
    draw() {
      var myChart = this.$echarts.init(
        document.getElementById("echartContainer6"),
        "infographic"
      );
      myChart.setOption({
    color: ['rgb(0,0,139)','rgb(65,0,225)', 'rgb(65,105,225)', 'rgb(30,144,255)', 
    'rgb(70,130,180)', 'rgb(135,206,250)', 'rgb(135,206,235)','rgb(0,191,255)', 
    'rgb(173,216,230)', 'rgb(176,224,230)'],
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)",
        position:function(p){ //其中p为当前鼠标的位置
        return [p[0] + 10, p[1] - 10]},
        //extraCssText:'width:40px;height:20px;',
        //fontSize: '5px'
    },
    series: [
        {
            name: '访问来源',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['50%', '40%'],
            avoidLabelOverlap: false,
            itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
            },
            label: {
                show: false,
                position: 'center',
                
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '20',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            data: [
            ]
        }
    ]
});
this.$http.get("http://131.mollnn.com:5000/api/type/distrib10/", {
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
